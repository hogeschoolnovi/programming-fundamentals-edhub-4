# ==========================================
# Voorbeeld Opdracht
# Gegeven is een set met de getallen 1, 2 en 3.
# Voeg het getal 1 toe aan de set en daarna het getal 4.
#
# Print de set 'getallen'.
# Het getal 1 stond al in de set, dus wordt niet nogmaals toegevoegd. Het getal 4 wordt wel toegevoegd.
# ==========================================

# set met getallen
getallen = {1, 2, 3}

# getal 1 en 4 worden toegevoegd aan de set
getallen.add(1)
getallen.add(4)

print('getallen: ', getallen)  # Het resultaat is: {1, 2, 3, 4}


# ==========================================
# Opgave 1:
# Gegeven de verzameling {3, 44, 17, 23, 58, 9, 36}
# Voer de volgende opdrachten uit:
# - Voeg de value 27 aan de verzameling toe.
# - Verwijder de value 23 uit de verzameling.
# - Druk alle values in de verzameling tussen 20 en 50 af.
#
# Verwachte uitkomst: 36, 27, 44
# ==========================================

verzameling = {3, 44, 17, 23, 58, 9, 36}

#     Voegt de value 27 aan de verzameling toe.
verzameling.add(27)
#     Verwijdert de value 23 uit de verzameling.
verzameling.remove(23)
#     Loopt door alle values in 'verzameling' en drukt de values af die tussen 20 en 50 liggen.
#     In de if wordt er gecheckt of de linker value kleiner is dan de rechter value. Dus is 20 minder dan 'i' EN is 'i' minder dan 50.
for i in verzameling:
    if 20 < i < 50:
        print(i)



# ==========================================
# Opgave 2:
# Gegeven de verzamelingen {red, blue, green} en {yellow, blue, green}
# Zoek uit met behulp van wiskundige verzamelingsoperatoren of methodes:
# - Welke kleur zit wel in verzameling_colors1 maar niet in verzameling_colors2?
# - Welke kleuren zitten niet in beide sets? ('red' en 'yellow')
#
# Print de resultaten.
# ==========================================

verzameling_colors1 = {'red', 'blue', 'green'}
verzameling_colors2 = {'yellow', 'blue', 'green'}

#   checkt of de kleuren in verzameling_colors1 zitten maar niet in verzameling_colors2
print(verzameling_colors1 - verzameling_colors2)
print(verzameling_colors1.difference(verzameling_colors2))
#   checkt welke kleuren niet in beide sets zitten
print(verzameling_colors1 ^ verzameling_colors2)
print(verzameling_colors1.symmetric_difference(verzameling_colors2))



# ==========================================
# Opgave 3:
# Gegeven de verzamelingen {11, 22, 33} en {5, 11, 16, 22}
# Gebruik wiskundige verzamelingsoperatoren om de volgende verzamelingen te printen:
#     {33}
#     {5, 16}
#     {5, 11, 16, 22, 33}
#     {11, 22}
#
# (De volgorde van de values in de verzamelingen is niet belangrijk, die kan namelijk veranderen omdat een set unordered is.)
# ==========================================


verzameling1 = {11, 22, 33}
verzameling2 = {5, 11, 16, 22}

#     Haalt de values uit verzameling1 die niet in verzameling2 zitten.
print(verzameling1 - verzameling2)
#     Haalt de values uit verzameling2 die niet in verzameling1 zitten.
print(verzameling2 - verzameling1)
#     Voegt de values van verzameling1 en verzameling2 samen.
print(verzameling1 | verzameling2)
#     Haalt de values uit verzameling1 en verzameling2 die in beide sets zitten.
print(verzameling1 & verzameling2)







