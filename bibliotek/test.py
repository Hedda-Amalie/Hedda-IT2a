bøker = ["harry potter", "the hobbit", "moby dick"]

bokNavn = input("navn på bok: ")

count = 1
for x in bøker:
    if(bokNavn == x):
        print("boken finnes")