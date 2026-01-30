
mac = "A0-FF-51-B3-D1-FF"
gruppo = mac.split("-")

for element in gruppo:
    if element != "FF":
        print(element)