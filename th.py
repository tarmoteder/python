from random import randint

var = randint(1,2)
loto = int(input("Kas kull (1) või kiri (2)?"))

if var == 1 & loto == 1:
    print ("On kull jah, võitja on selgunud")
elif var == 1 & loto == 2:
    print("Kull on, kaotasid")
elif var == 2 & loto == 2:
    print ("On kiri jah, võitja on selgunud")
else:
    print("Kiri on, kaotasid")
    

