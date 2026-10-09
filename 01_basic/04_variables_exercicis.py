###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.

nom = input("Introdueix el nom de l'encaminador: ")
ubicacio = input("Introdueix la ubicació de l'encaminador: ")
ports = int(input("Introdueix el nombre de ports: "))
encès = input("Introdueix si està encès (sí/no): ") == "sí"

print(f"El {nom} està a {ubicacio} i té {ports} ports. Està encès: {encès}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

GB_inclosos = int(input("Introdueix els GB inclosos en el pla de dades: "))
GB_consumits = int(input("Introdueix els GB consumits: "))
GB_restants = GB_inclosos - GB_consumits
print(f"Queden {GB_restants} GB disponibles.")

GB_consumits = int(input("Introdueix els GB consumits actualitzats: "))
GB_restants = GB_inclosos - GB_consumits
print(f"Queden {GB_restants} GB disponibles després de l'actualització.")