import random
import time
from datetime import datetime

#Hatarertekek

MIN_HOMERSEKLET=-50
MAX_HOMERSEKLET=50

MIN_PARATARTALOM=30
MAX_PARATARTALOM=70

print("Homerseklet es paratartalom monitor")

while True:

    homerseklet=round(random.uniform(-25,45),2)
    paratartalom=round(random.uniform(0,100),2)

    ido=datetime.now()

    print("\n Idopont:",ido)
    print("Homerseklet:",homerseklet,"'C")
    print("Paratartalom",paratartalom,"%")

    if homerseklet<0:
        print("Tul hideg")

    elif homerseklet>30:
        print("Tul meleg")

    else:
        print("Normalis homerseklet")

    if paratartalom>70:
        print("Tul magas")

    elif paratartalom<30:
        print("Tul alacsony")

    else:
        print("Normalis paratartalom")

    with open("meresek.txt","a",encoding="utf-8") as f:
        f.write(f"{ido} {homerseklet} {paratartalom}")

    print("Adatok elmentve!")