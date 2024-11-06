import uuid
import json

brukere = []
bøker = []
rentals = []

with open("bibliotek/brukere.json", "r") as file:
    brukere = json.load(file)

with open("bibliotek/bøker.json", "r") as file:
    bøker = json.load(file)

with open("bibliotek/rentals.json", "r") as file:
    rentals = json.load(file)   

    # funksjon for å legge til leietaker
def leggTilBruker():
    bruker = {
        "forNavn": input("skriv inn fornavn: "),
        "etterNavn": input("skriv inn etternavn: "),
        "ID": str(uuid.uuid4()),
        "e-post":  input("skriv inn epost: "),
        "tlf":  input("skriv inn tlf: "),
    }
    brukere.append(bruker)
    with open("bibliotek/brukere.json", "w") as file:
        json.dump(brukere, file, indent=4)


    # funksjon for legg til bøker
def leggTilBøker():
    bok = {
        "id": str(uuid.uuid4()),
        "tittel": input("tittel på bok: "),
        "forfatter": input("forfatter på bok: "),
        "forlag": input("Utgiver: "),
        "sjanger": input("eventyr: "),
        "utgivelsesÅr": input("2000: "),
        "utleid": False
    }
    bøker.append(bok)
    with open("bibliotek/bøker.json", "w") as file:
        json.dump(bøker, file, indent=4)

    # funksjon for boksøk
def leggTilBoksøk():
    pass


    # funksjon for søk opp leietaker
def leggTilLeietaker():
    pass



    # funksjon for lei ei bok
def lei():
    bokNavn = input("navn på bok: ")
    rental = {
        "bokID": "",
        "brukerID": ""
    }

    for x in bøker: 
        if(bokNavn == x["title"]):
            print("boken finnes")
            x["rented"] = True
            rental["bokID"] = x["ID"]
    
    leietaker = input("Navn på leietaker: ")

    for x in brukere: 
        if(leietaker == x["forNavn"]):
            print("leietaker finnes")
            rental["brukerID"] = x["ID"]
    
    rentals.append(rental)
    with open("bibliotek/rentals.json", "w") as file:
        json.dump(rentals, file, indent=4)

    with open("bibliotek/bøker.json", "w") as file:
        json.dump(bøker, file, indent=4)
        
    #print(bokNavn)

    # funksjon for lever inn bok
    # funksjon for tilgjengelige bøker
    # funksjon for Se alle utleide bøker
    # funksjon for å se alle bøker
    #
    # Trenger en meny
def menu():
    print("|-------hovedmeny-------|")
    print("|  1. legg til brukere  |")
    print("|  2. legg til bok      |")
    print("|  3. søk opp bruker    |")
    print("|  4. søk opp bok       |")
    print("|  5. lei bok           |")
    print("|  6. lever inn bok     |")
    print("|  7. se ledige bøker   |")
    print("|  8. se utleid bøker   |")
    print("|  9. se alle bøker     |")
    print("|  0. Avslutt program   |")
    print("|-----------------------|")
    valg = input("| Velg ett nummer: ")
    return valg

# hovedprogram
def main():
    run = True
    while run:
        myChoise = menu()
        if(myChoise == "1"):
            leggTilBruker()
        elif(myChoise == "2"):
            leggTilBøker()
        elif(myChoise == "3"):
            pass
        elif(myChoise == "4"):
            pass
        elif(myChoise == "5"):
            lei()
        elif(myChoise == "6"):
            pass
        elif(myChoise == "7"):
            pass
        elif(myChoise == "8"):
            pass
        elif(myChoise == "9"):
            pass
        elif(myChoise == "0"):
            pass


main()
