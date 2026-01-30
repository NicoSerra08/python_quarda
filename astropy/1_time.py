from datetime import datetime, timedelta
from time import sleep

start_time = datetime.now()
now_time = datetime.now()

a =0

while(now_time < start_time + timedelta(minutes=5)):
    a += 1
    print(f"{a} - hello from the ISS")
    sleep(0.5)
    now_time = datetime.now()

print(f"passati 5 secondi e {a} sequenze")



# -moto circolare
# -velocità angolare
# -accellerazione centrifuga e centripeta
# -leggi di gravitazoine universale
