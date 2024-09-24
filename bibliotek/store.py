import json

brukere = {}

with open("bibliotek/brukere.json") as f:
    file = json.load(f)
    print(file)
    
print(brukere["fornavn"])

with open("bibliotek/brukere.json", "w") as f:
    json.dump()