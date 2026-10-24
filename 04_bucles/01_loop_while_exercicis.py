###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
# num=10
# while (num>0):
#     print(num)
#     num=num-1 #millor: num -= 1


# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
# i=1
# sum=0
# while(i<=20):
#     if(i%2 == 0):
#         sum += i
#     i += 1
# print(sum)

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

# enter = int(input("Introdueix un número enter positiu: "))
# i=enter
# factorial=1
# while (i>0):
#     factorial *= i
#     i -= 1
# print(factorial)


# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

# contra = input("Introdueix una contrasenya: ")
# while len(contra) < 8:
#     contra = input("La contrasenya ha de tenir almenys 8 caràcters: ")
# print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

# num=int(input("Introdueix un número: "))
# i=0
# while (i<=10):
#     print(f"{num} per {i}: {num*i}")
#     i += 1



# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

# n = int(input("Introdueix un número enter positiu N: "))

# numero = 2
# while numero <= n:
#   es_primer = True  # Assumim que el número és primer fins que es demostri el contrari
#   divisor = 2
#   while divisor * divisor <= numero:  # Optimitzem: no cal provar divisors fins a numero
#     if numero % divisor == 0:
#       es_primer = False  # Si trobem un divisor, no és primer
#       break  # Sortim del bucle interior
#     divisor += 1
#   if es_primer:
#     print(numero)

#   numero += 1


# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.

# num =int(input("Introdueix nombres enters: "))
# sum = num
# while (num != 0):
#     num = int(input("Introdueix nombres enters: "))
#     sum += num
# print(f"Suma= {sum}")


# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.


# numero = int(input("Introdueix un número enter positiu: "))
# comptador = 0

# while numero > 0:
#   numero //= 10  #divisió entera!
#   comptador += 1

# print(f"El número té {comptador} xifres.")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

# termes = int(input("Quants termes de Fibonacci vols veure? "))
# anterior = 0
# actual = 1
# comptador = 0

# while comptador < termes:
#   print(anterior)
#   seguent = anterior + actual
#   anterior = actual
#   actual = seguent
#   comptador += 1



# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

secret=7

trobar = int(input("Endevina: "))
while (trobar != secret):
  if secret>trobar : print("Secret és més gran")
  else: print ("Secret és més petit")
  trobar = int(input("Endevina: "))

