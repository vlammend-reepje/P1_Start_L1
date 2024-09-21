# Schrijf een Python-programma dat aan de gebruiker twee vragen stelt:
# 1. Hoeveel mensen gaan er naar het concert?
# 2. Wat is de prijs per ticket?
#
# Bereken het totaalbedrag en print dat bedrag.
#
# Voorbeeldinvoer:
# Hoeveel mensen gaan er naar het concert?  3
# Wat is de prijs per ticket?  10.55
#
# Voorbeelduitvoer:
# De totale prijs bedraagt 31.65 euro.
prijs_per_ticket = float( input("hoeveel kost 1 ticket: "))
aantal_mensen = int(input("met hoe veel mensen ga je? "))
print("dat grapje kost jou. ", prijs_per_ticket * aantal_mensen)