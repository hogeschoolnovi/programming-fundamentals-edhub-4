# Opgave 1:
# Gegeven een woordenboek van Internet toplevel domeinen:

tlds = {'Nederland':'nl', 'Verenigde Staten':'us', 'Duitsland':'de'}

# Voer de volgende opdrachten uit en toon de resultaten:

#     Controleer of het woordenboek de sleutel ‘Duitsland’ bevat.
print(tlds.get('Duitsland') != None)
#     Controleer of het woordenboek de sleutel ‘Frankrijk’ bevat.
print(tlds.get('Frankrijk') != None)
#     Itereer door de sleutel-waarde paren en toon ze in 2-kolommen.
for key, value in tlds.items():
    print(key, value)
#     Voeg het sleutel-waarde paar ‘Zweden’ : ‘sw’ toe.
tlds['Zweden'] = 'sw'
#     Wijzig de waarde van de sleutel ‘Zweden’ in ‘se’.
tlds['Zweden'] = 'se'
#     Gebruik een dictionary comprehension om sleutels en waarden te verwisselen.
tlds = {value: key for key, value in tlds.items()}
#     Uitgaande van het resultaat van f) gebruik een dictionary comprehension om alle landnamen te converteren naar hoofdletters.
tlds = {key: value.upper() for key, value in tlds.items()}

print(tlds)


# Opgave 2:
# Maak een woordenboek van vrienden met hun voornaam als sleutel en hun leeftijd als waarde (we nemen even aan dat alle voornamen verschillend zijn).

friends = {'Kees':25 , 'Amber': 30, 'Bart': 28, 'Johan': 27, 'Eva': 26}
# Voer de volgende opdrachten uit en toon de resultaten:
#     Druk naam en leeftijd af van al je vrienden, alfabetisch gesorteerd op naam.
for key in sorted(friends.keys()):
    print(key, friends[key])
#     Druk de naam af van al je vrienden die 30 jaar of ouder zijn.
for key, value in friends.items():
    if value >= 30:
        print(key)
#     Verhoog alle leeftijden in het woordenboek met 1.
for key in friends.keys():
    friends[key] += 1
#     Verwijder alle vrienden waarvan de naam begint met de letter ‘B’
for key in list(friends.keys()):
    if key.startswith('B'):
        del friends[key]

print(friends)



# Opgave 3:
# Breid het programma waarin we de zoeksnelheid in een lijst en woordenboek vergelijken uit
# zodat je 1000 random gehele getallen tussen 0 en 1 miljoen genereert en die probeert op te zoeken in de lijst
# en het woordenboek. Wat is het resultaat?

import random
import time

random_numbers = [random.randint(0, 1000000) for _ in range(1000)]
random_numbers_dict = {i: None for i in random_numbers}

start = time.time()
for i in range(1000000):
    if i in random_numbers:
        pass
end = time.time()
print(f"List: {end - start}")

start = time.time()
for i in range(1000000):
    if i in random_numbers_dict:
        pass
end = time.time()
print(f"Dictionary: {end - start}")