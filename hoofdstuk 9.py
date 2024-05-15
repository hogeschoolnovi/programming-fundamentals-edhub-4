# Opgave 1:
# Gegeven de verzameling {3, 44, 17, 23, 58, 9, 36}

set = {3, 44, 17, 23, 58, 9, 36}

# Voer de volgende opdrachten uit:

#     Voeg de waarde 27 aan de verzameling toe.
set.add(27)
#     Verwijder de waarde 23 uit de verzameling’.
set.remove(23)
#     Druk alle waarden in de verzameling tussen 20 en 50 af.
for i in set:
    if 20 < i < 50:
        print(i)


# Opgave 2:
# Gegeven de verzamelingen {11, 22, 33} en {5, 11, 16, 22}
# Gebruik wiskundige verzamelingsoperatoren om de volgende verzamelingen te creëren:

#     {33}
#     {5, 16, 33}
#     {5, 11, 16, 22, 33}
#     {11, 22}

set1 = {11, 22, 33}
set2 = {5, 11, 16, 22}

print(set1 - set2)
print(set2 - set1)
print(set1 | set2)
print(set1 & set2)

# Opgave 3:
# Maak 2 verzamelingen met kleuren aan en controleer dat het symmetrisch verschil van die verzamelingen gelijk is aan de
# vereniging van de verschillen tussen beide verzamelingen. In een wiskundige formule: : A B = (A ∖ B) (B ∖ A)
set1_colors = {'red', 'blue', 'green'}
set2_colors = {'yellow', 'blue', 'green'}

# checkt of de kleuren in set1_colors zitten maar niet in set2_colors
set3 = set1_colors.difference(set2_colors)
print(set3)
# checkt welke kleuren niet in beide sets zitten
print(set1_colors ^ set2_colors)

# Opgave 4:
# Maak nogmaals 2 verzamelingen met kleuren aan en controleer dat het symmetrisch verschil van die verzamelingen gelijk
# is aan het verschil tussen de vereniging en de doorsnede van beide verzamelingen. In een wiskundige formule: : A B = (A B) ∖ (A B)

set1_colors = {'red', 'blue', 'green'}
set2_colors = {'blue', 'green', 'yellow'}

set3_colors = set1_colors ^ set2_colors
print(set3_colors)
