###
# EXERCICIS
###

# Exercici 1: Comparar nombres
# Donats els nombres:
# nombre_a = 8
# nombre_b = 5
# Mostra el resultat de comparar si nombre_a és més gran, més petit o igual
# que nombre_b.

# if nombre_a > nombre_b:
#     print(f"El nombre {nombre_a} és major que el nombre {nombre_b}")
# elif nombre_a < nombre_b:
#     print(f"El nombre {nombre_a} és més petit que el nombre {nombre_b}")
# else:
#     print(f"Els dos nombres són {nombre_a}")



# Exercici 2: Comparar cadenes de text
# Donades les cadenes:
# paraula_a = "Hola"
# paraula_b = "hola"
# Mostra si són iguals i si paraula_a és igual a "Hola".
# Observa si Python distingeix entre majúscules i minúscules.

# if paraula_a == paraula_b:
#     print(f"La paraula {paraula_a} és igual a la paraula {paraula_b}")
# else:
#     print(f"La paraula {paraula_a} és diferent a la paraula {paraula_b}")

# Exercici 3: Connexió de xarxa
# Donats els valors booleans:
# router_encès = True
# connexio_activa = False
# Crea una variable anomenada xarxa_disponible que sigui True només si el
# router està encès i la connexió està activa. Mostra'n el resultat.

# if router_encès == True and connexio_activa == True:
#     xarxa_disponible = True
# else:
#     xarxa_disponible = False
# print(f"La xarxa està disponible? {xarxa_disponible}")

# Millor:

# xarxa_disponible = router_encès and connexio_activa
# print(f"Xarxa disponible: {xarxa_disponible}")


# Exercici 4: Avisos pendents
# Donats els valors booleans:
# actualitzacio_disponible = False
# alerta_critica = True
# Crea una variable anomenada cal_avisar que sigui True si hi ha una
# actualització disponible o una alerta crítica. Mostra'n el resultat.

# if actualitzacio_disponible==False and alerta_critica==False:
#     cal_avisar=False
# else:
#     cal_avisar=True
# if cal_avisar == True:
#     print("Cal avisar!!!")

# Millor:
# cal_avisar = actualitzacio_disponible or alerta_critica
# print(f"Cal avisar: {cal_avisar}")

# Exercici 5: Accés a un compte
# Donats els valors booleans:
compte_actiu = True
contrasenya_correcta = True
codi_correcte = False
dispositiu_de_confiança = True
compte_bloquejat = False
# Crea una variable anomenada accés_permes que sigui True si el compte està
# actiu, la contrasenya és correcta, el compte no està bloquejat i, a més,
# el codi és correcte o el dispositiu és de confiança. Fes servir and, or i not.
# Mostra'n el resultat.

accés_permès = compte_actiu and contrasenya_correcta and not compte_bloquejat and (codi_correcte or dispositiu_de_confiança)
print(f"Accés permès? {accés_permès}")