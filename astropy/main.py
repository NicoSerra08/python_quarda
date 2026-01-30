# main.py
import time
import numpy as np
from scipy.stats import iqr
from datetime import datetime
import cv2
import math
from orbit import ISS
from picamera import PiCamera
from sense_hat import SenseHat

RESOLUTION_X = 4056
RESOLUTION_Y = 3040
EARTH_RADIUS = 6372.795477598
G = 6.674 * (10 ** -11)  # costante gravitazionale G
M = 5.972 * (10 ** 24)   # massa della terra in kg
F = 5
sw_x = 6.287
sw_y = 4.712
H = 400
gAttrazione = G * M / ((EARTH_RADIUS + H) * 1000) ** 2
target = 7.666666666666666

val = list()

def accel():
    """
    Measures the centripetal acceleration using the Sense HAT's accelerometer,
    calculates the orbital speed of the ISS, and returns the average orbital speed over 30 cycles.
    """
    sense = SenseHat()
    sampling_period = 0.5  # in seconds

    velocita_totale = 0
    conteggio_velocita = 0
    cicli = 0

    while cicli < 30:
        # Get the raw accelerometer data
        accel_data = sense.get_accelerometer_raw()
        a_z = accel_data['z']
        
        aSensore = a_z
        aSensore = aSensore * 9.81  # Convert the z-axis acceleration to m/s^2
        # Calculate the centripetal acceleration
        a_c = gAttrazione - aSensore

        # Calculate the orbital speed of the ISS
        velocita_2 = math.sqrt((G * M) / math.sqrt(G * M / a_c)) / 1000
        velocita_totale += velocita_2
        conteggio_velocita += 1

        # Wait for the sampling period
        time.sleep(sampling_period)
        cicli += 1

    return velocita_totale / conteggio_velocita

def gradi_a_radianti(gradi):
    """Converts an angle given in degrees to radians."""
    return gradi * math.pi / 180

def distanza_coordinata(lat1, lon1, lat2, lon2, radius=EARTH_RADIUS):
    """
    Calculates the distance between two coordinates using the Haversine formula.
    """
    # Convert coordinates from degrees to radians
    lat1 = gradi_a_radianti(lat1)
    lon1 = gradi_a_radianti(lon1)
    lat2 = gradi_a_radianti(lat2)
    lon2 = gradi_a_radianti(lon2)

    # Calculate the difference in angles between the latitudes and longitudes
    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    # Apply the Haversine formula
    a = math.sin(d_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2)**2
    d = radius * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return d

def convert_to_cv(image_1, image_2):
    """Converts two images to grayscale using OpenCV."""
    image_1_cv = cv2.imread(image_1, 0)
    image_2_cv = cv2.imread(image_2, 0)
    return image_1_cv, image_2_cv

def calculate_features(image_1, image_2, feature_number):
    """Calculates the keypoints and descriptors using ORB algorithm."""
    orb = cv2.ORB_create(nfeatures=feature_number)
    keypoints_1, descriptors_1 = orb.detectAndCompute(image_1, None)
    keypoints_2, descriptors_2 = orb.detectAndCompute(image_2, None)
    return keypoints_1, keypoints_2, descriptors_1, descriptors_2

def calculate_matches(descriptors_1, descriptors_2):
    """Calculates matches between descriptors using Brute-Force Matcher."""
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = brute_force.match(descriptors_1, descriptors_2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

def find_matching_coordinates(keypoints_1, keypoints_2, matches):
    """Finds the coordinates of matching keypoints."""
    coordinates_1 = []
    coordinates_2 = []
    for match in matches:
        image_1_idx = match.queryIdx
        image_2_idx = match.trainIdx
        (x1, y1) = keypoints_1[image_1_idx].pt
        (x2, y2) = keypoints_2[image_2_idx].pt
        coordinates_1.append((x1, y1))
        coordinates_2.append((x2, y2))
    return coordinates_1, coordinates_2

def calculate_height(coordinates_1, coordinates_2, km):
    """Calculates the average distance from the point of image capture."""
    all_distances = 0
    merged_coordinates = list(zip(coordinates_1, coordinates_2))
    for coordinate in merged_coordinates:
        x_difference = coordinate[0][0] - coordinate[1][0]
        y_difference = coordinate[0][1] - coordinate[1][1]
        all_distances += math.hypot(x_difference, y_difference)
    px = all_distances / len(merged_coordinates)
    h1 = altitude(calc_kmImg(px, km, RESOLUTION_X), sw_x)
    h2 = altitude(calc_kmImg(px, km, RESOLUTION_Y), sw_y)
    return (h1 + h2) / 2

def calc_kmImg(px, km, resolution):
    """Calculates the distance in kilometers per pixel."""
    return (resolution * km) / px

def altitude(km, sw):
    """Calculates the altitude of the camera."""
    return ((km / 2) * F) / (sw / 2)

def mainPhotos(cam):
    """Captures two images and calculates orbital speed."""
    try:
        # Capture first image
        cam.capture("image1.jpg")
        point = ISS.coordinates()
        lat1 = point.latitude.degrees
        long1 = point.longitude.degrees
        capture_time1 = datetime.now()

        time.sleep(3)

        # Capture second image
        cam.capture("image2.jpg")
        point = ISS.coordinates()
        lat2 = point.latitude.degrees  
        long2 = point.longitude.degrees
        capture_time2 = datetime.now()

        time_difference = (capture_time2 - capture_time1).total_seconds()

        # Calculate distance between coordinates
        dist_km = distanza_coordinata(lat1, long1, lat2, long2)

        # Calculate average distance between features
        img1, img2 = convert_to_cv("image1.jpg", "image2.jpg")
        keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(img1, img2, 1000)
        matches = calculate_matches(descriptors_1, descriptors_2)
        coordinates_1, coordinates_2 = find_matching_coordinates(keypoints_1, keypoints_2, matches)
        heigh = calculate_height(coordinates_1, coordinates_2, dist_km)

        print(f"Calculated height: {heigh}")
        return math.sqrt(G * M / ((EARTH_RADIUS + heigh) * 1000)) / 1000
    
    except FileNotFoundError as e:
        print(f"Photo not available in replay: {e}")
        return None
    except Exception as e:
        print(f"Error in mainPhotos: {e}")
        return None

def weightedAvrg(listValues, target):
    """Calculates the value in the list closest to the target."""
    npValues = np.array(listValues)
    diff = np.abs(npValues - target)
    iClosetValues = np.argmin(diff)
    avrg = npValues[iClosetValues]
    return avrg

def mediaValori(listValues):
    """Calculates the average of values within a certain range using IQR."""
    moltiplicatore = 0.1
    misurazioni = np.array(listValues)
    q1 = np.percentile(misurazioni, 45) 
    q3 = np.percentile(misurazioni, 55) 

    iqr_value = iqr(misurazioni) 

    soglia_inf = q1 - moltiplicatore * iqr_value 
    soglia_sup = q3 + moltiplicatore * iqr_value

    # Filter values
    misurazioni_filtrate = misurazioni[(misurazioni >= soglia_inf) & (misurazioni <= soglia_sup)]

    return np.mean(misurazioni_filtrate)

def main():
    durata_minuti = 8
    durata_secondi = durata_minuti * 60

    # Initialize camera ONCE at the start
    cam = PiCamera()
    cam.resolution = (RESOLUTION_X, RESOLUTION_Y)

    start_time = time.time()

    try:
        while time.time() - start_time < durata_secondi:
            ret = accel()
            val.append(ret)
            
            vel1 = mainPhotos(cam)
            # Only add valid measurements
            if vel1 is not None:
                val.append(vel1)

        # Only calculate if we have measurements
        if len(val) > 0:
            estimate_kmps = mediaValori(val)
            
            file_path = "result.txt"
            with open(file_path, 'w') as file:
                file.write("{:.5g}".format(estimate_kmps))
            print(f"Result written: {estimate_kmps} km/s")
        else:
            print("No valid measurements collected")
    
    finally:
        # Always close the camera when done
        cam.close()

if __name__ == "__main__":
    main()