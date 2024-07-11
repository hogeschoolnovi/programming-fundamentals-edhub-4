# ==========================================
# Voorbeeld Opdracht
#
# Maak een woordenboek genaamd 'fruit' met daarin de sleutels 'appel' en 'banaan'.
# Geef 'appel' de waarde 'rood' en 'banaan' de waarde 'geel'.
# Print vervolgens de kleur van de banaan door de sleutel 'banaan' te gebruiken.
#
# Verwachte uitkomst:  geel
# ==========================================

# dictionary met kleuren als waarden
fruit = {'appel': 'rood', 'banaan': 'geel'}

# print de kleur van de banaan
print(fruit['banaan'])  # Het resultaat is: geel



# ==========================================
# Opdracht 1:
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat krijgt.

# Opdracht 1a:
# Maak een woordenboek met daarin de domeinnamen van de landen Nederland, Verenigde Staten en Duitsland.
# De waarden zijn respectievelijk de landcodes 'nl', 'us' en 'de'.
#
# Opdracht 1b:
# Controleer of de woordenboek het land 'Nederland' bevat. Zo ja, print 'True', zo nee, print 'False'.
# Doe dit ook voor de landen 'Verenigde Staten' en 'India'.
#
# Verwachte uitkomst: True, True, False
#
# Opdracht 1c:
# Itereer door de sleutel-waarde paren en toon per regel de sleutel en de waarde.
# Gebruik hierbij een for-loop en de items() methode.
#
# Verwachte uitkomst:
#
#   Nederland nl
#   Verenigde Staten us
#   Duitsland de
#
# Opdracht 1d:
# Voeg het sleutel-waarde paar ‘Zweden’ : ‘sw’ toe aan het woordenboek 'domeinen'.
# Wijzig de waarde van de sleutel ‘Zweden’ in ‘se’.
# Het sleutel waarde paar ‘Zweden’ : ‘se’ moet nu in het woordenboek staan.
# Print het woordenboek na deze wijzigingen.
#
# Verwachte uitkomst: {'NL': 'Nederland', 'US': 'Verenigde Staten', 'DE': 'Duitsland', 'SE': 'Zweden'}

# Opdracht 1e:
# Gebruik een dictionary comprehension om de sleutels en waarden van het woordenboek te verwisselen.
# Gebruik vervolgens een dictionary comprehension om alle landnamen te converteren naar hoofdletters.
# Print het woordenboek na deze wijzigingen.
#
# Verwachte uitkomst: {'NL': 'Nederland', 'US': 'Verenigde Staten', 'DE': 'Duitsland', 'SE': 'Zweden'}
# ==========================================

# Opdracht 1a: woordenboek met domeinnamen en landcodes
domeinen = {'Nederland': 'nl', 'Verenigde Staten': 'us', 'Duitsland': 'de'}

# Opdracht 1b: controleer of het woordenboek de landen bevat
print(domeinen.get('Nederland') != None)  # Het resultaat is: True
print(domeinen.get('Verenigde Staten') != None)  # Het resultaat is: True
print(domeinen.get('India') != None)  # Het resultaat is: False

# Opdracht 1c: itereer door de sleutel-waarde paren en toon per regel de sleutel en de waarde
for key, value in domeinen.items():
    print(key, value)

# Verwachte uitkomst:
#   Nederland nl
#   Verenigde Staten us
#   Duitsland de

# Opdracht 1d: voeg een sleutel-waarde paar toe en wijzig de waarde van de sleutel
#     Voeg het sleutel-waarde paar ‘Zweden’ : ‘sw’ toe.
domeinen['Zweden'] = 'sw'
#     Wijzig de waarde van de sleutel ‘Zweden’ in ‘se’.
domeinen['Zweden'] = 'se'


# Opdracht 1e:
# in deze dictionary comprehension worden de sleutels en waarden van het woordenboek verwisseld
domeinen = {value: key for key, value in domeinen.items()}  # Uitkomst: {'nl': 'Nederland', 'us': 'Verenigde Staten', 'de': 'Duitsland', 'se': 'Zweden'}
# landnamen worden omgezet naar hoofdletters
domeinen = {key: value.upper() for key, value in domeinen.items()}  # Uitkomst: {'NL': 'Nederland', 'US': 'Verenigde Staten', 'DE': 'Duitsland', 'SE': 'Zweden'}

print(domeinen)



# ==========================================
# Opdracht 2:
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat krijgt.
#
# Opdracht 2a:
# Maak een woordenboek van de volgende vriendengroep met hun voornaam als sleutel en hun leeftijd als waarde.
# Kees is 25, Amber is 30, Bart is 28, Johan is 27 en Eva is 26.
#
# Opdracht 2b:
# Druk naam en leeftijd af van al je vrienden, alfabetisch gesorteerd op naam.
#
# Verwachte uitkomst:  Amber 30, Bart 28, Eva 26, Johan 27, Kees 25
#
# Opdracht 2c:
# Druk de naam af van al je vrienden die 30 jaar of ouder zijn.
#
# Verwachte uitkomst: Amber
#
# Opdracht 2d:
# Verhoog alle leeftijden in het woordenboek met 1.
#
# Verwachte uitkomst: {'Kees': 26, 'Amber': 31, 'Bart': 29, 'Johan': 28, 'Eva': 27}
#
# Opdracht 2e:
# Verwijder alle vrienden waarvan de naam begint met de letter ‘B’.
# Voor het verwijderen van items kun je het keyword 'del' gebruiken.
#
# Verwachte uitkomst: {'Kees': 26, 'Amber': 31, 'Johan': 28, 'Eva': 27}

# ==========================================

friends = {'Kees': 25, 'Amber': 30, 'Bart': 28, 'Johan': 27, 'Eva': 26}

# Opdracht 2a:
#     De for loop gaat alle keys van het woordenboek langs en sorteert deze op alfabetische volgorde.
for key in sorted(friends.keys()):
    print(key, friends[key])

# Opdracht 2b:
#     De for loop gaat alle keys en values van het woordenboek langs en print de keys van de vrienden die 30 jaar of ouder zijn.
#     .items() geeft een lijst van tuples terug met de key en value van het woordenboek.
for key, value in friends.items():
    if value >= 30:
        print(key)
#     friends[key] verwijst naar de value van de key in het woordenboek. += verhoogt de huidige waarde met de waarde die na het += teken staat.
for key in friends.keys():
    friends[key] += 1
#     De for loop gaat alle keys van het woordenboek langs . .startswith() geeft True terug als de string begint met de meegegeven waarde.
for key in list(friends.keys()):
    if key.startswith('B'):
        del friends[key]

print(friends)



# ==========================================
# Opgave 3:

# We gaan kijken wat we sneller kunnen doorzoeken: Een lijst of een woordenboek.
# De libraries 'random' en 'time' hebben we nodig. Die mag je alvast importeren.
# Maak hiervoor de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat krijgt.
#
# Opdracht 3a:
# Genereer een lijst met 1000 random getallen tussen 0 en 1 miljoen.
# Genereer een woordenboek die dezelfde random getallen heeft als de lijst. De keys zijn de random getallen en alle values zijn None.
#
# Opdracht 3b:
# Maak een variabele counter_list aan en zet deze op 0
# Maak een for loop die 1000000 keer loopt.
# In de for loop controleer je of de loop variabele i in de random_list voorkomt. Zo ja, verhoog dan de counter_list met 1.
# time.time() geeft de huidige tijd in seconden terug. Reken met behulp van deze methode uit hoe lang de loop duurde.
# Print de counter_list en de tijd die de loop duurde.
#
# Doe hetzelfde voor het woordenboek.
# ==========================================

# Let op! Normaal zet je de imports bovenaan je bestand, maar voor de duidelijkheid van de opdracht zetten we ze hier.
import random
import time

#   random.randint() genereert een random getal tussen de 2 meegegeven waarden (hier dus tussen de 0 en 1000000).
#   We willen 1000 keer een random getal genereren. Dat doet de for loop.
#   In een for loop moet je altijd een naam geven aan de loop variabele.
#   In dit geval gebruiken we de loop variabele verder niet, het is dan conventie om deze als underscore '_' te schrijven.
random_list = [random.randint(0, 1000000) for _ in range(1000)]

#   Vult de dictionary met dezelfde random getallen als keys en None als values.
#   Voor de opdracht maakt het niet uit wat de waarden zijn.
#   We loopen alleen over de keys heen dus de waarden worden niet gebruikt.
random_dict = {i: None for i in random_list}


# time.time() geeft de huidige tijd in seconden terug.
# Door voor en na de loop de tijd op te vragen, en tegen elkaar weg te strepen (end - start), weet je hoe lang de loop duurde.
start = time.time()
# counter_list gaat bijhouden hoe vaak een random getal in de lijst voorkomt.
# We willen namelijk dubbelchecken of de loop wel 1000 random getallen vind
counter_list = 0
# De for loop loopt 1000000 keer.
for i in range(1000000):
    # Als de loop variabele i overeenkomt met een random getal in de random_list, dan verhogen we de counter_list met 1.
    if i in random_list:
        counter_list += 1
# hier vragen we nogmaals de tijd op zodat we de eindtijd van de loop hebben.
end = time.time()
# Print de counter en de tijd die de loop duurde.
print(f"List; Counter: {counter_list}  Time: {end - start}")


# We doen hier hetzelfde maar dan voor het woordenboek. Hierna kunnen we zien of de list of het woordenboek sneller te doorzoeken is.
start = time.time()
counter_dict = 0
for i in range(1000000):
    if i in random_dict:
        counter_dict += 1
end = time.time()
print(f"Dictionary; Counter: {counter_dict}  Time: {end - start}")

