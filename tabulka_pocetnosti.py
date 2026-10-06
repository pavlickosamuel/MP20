fr = open("tabulka_pocetnosti.txt", "r")

text = fr.read()
fr.close()

print(text)
 
abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter = {}
for znak in abeceda:
    counter[znak] = 0
 
for znak in text.upper():
    if znak in counter:
        counter[znak] += 1
 
print("\nPočty jednotlivých znakov v texte:")
for znak in abeceda:
    print(znak, "-", counter[znak])
 
chybajuce = []
for znak in abeceda:
    if counter[znak] == 0:
        chybajuce.append(znak)
 
print("\nZnaky, ktoré sa v texte nevyskytli:")
if chybajuce:
    print(", ".join(chybajuce))
else:
    print("Vyskytli sa všetky znaky abecedy.")