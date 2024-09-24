import uuid

brukere = []
bøker = []


    # funksjon for å legge til leietaker
def leggTilBruker():
    bruker = {
        "forNavn": input("skriv inn fornavn: "),
        "etterNavn": input("skriv inn etternavn: "),
        "ID": uuid.uuid4(),
        "e-post":  input("skriv inn epost: "),
        "tlf":  input("skriv inn tlf: "),
    }
    brukere.append(bruker)

    # funksjon for legg til bøker
def leggTilBøker():
    print("hello")

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

    # funksjon for boksøk

    # funksjon for søk opp leietaker
    # funksjon for lei ei bok
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
            pass
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
