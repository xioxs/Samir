import re
from collections import Counter


def inlezen_file(file):
    f = open(file, "r")
    lijst = list()

    if f.mode == "r":
        for line in f:
            aa=re.compile(r'\s*([0-9]+(?:\.[0-9]+){3})').findall(line)
            if len(aa)>2:
                source=aa[0]
            else:
                source=aa[0]
            lijst.append(source)
    return lijst

uniekelijst = set()
lijst = inlezen_file("log.txt")

#tel het aantal zelfde IP-adressen in de lijst
lijst = Counter(lijst)

#ga doorheen de lijst en maak er een simpele CSV van voor in Excel op te nemen
for i in lijst.elements():
    aantal = "{};{}".format(i,lijst[i])
    uniekelijst.add(aantal)

#Schrijf output naar file
with open("output.txt", encoding='utf-8-sig', mode='w+') as f:
    for x in uniekelijst:
        f.write(x+"\n")



