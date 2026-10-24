###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

# nivell = float(input("Introdueix el nivell de senyal rebut en dBm: "))
# if(nivell>=-50):
#     print("Excel·lent")
# elif(-67<=nivell<-50):
#     print("Bona")
# elif(-75<=nivell<-67):
#     print("Feble")
# else:
#     print("Molt feble")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.



# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

# consum = float(input("Consum de dades en GB: "))
# if (consum<20):
#     print("Està dins el límit")
# else:
#     print(f"Ha superat el límit per {consum-20} GB addicionals")



# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("L'indicador LOS del terminal òptic està encès? (sí/no)")
internet = input("L'indicador d'Internet del router està encès? (sí/no)")

if los == 'no' and internet == 'sí':
    print("Revisar el cable de fibra")
elif los == 'sí' and internet == 'no':
    print("Comprovar el servei del proveïdor")
elif los == 'no' and internet == 'no':
    print("Revisar el cable de fibra i comprovar el servei del proveïdor")
else:
    print("La conneció funciona correctament")



# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.