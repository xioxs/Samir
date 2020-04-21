import re
from Stream import Stream
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
tel_lijst = Counter(lijst)
for i in tel_lijst.elements():
    aantal = "{};{}".format(i,tel_lijst[i])
    uniekelijst.add(aantal)

with open("output.txt", encoding='utf-8-sig', mode='w+') as f:
    for x in uniekelijst:
        f.write(x+"\n")







