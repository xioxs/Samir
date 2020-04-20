import re
def inlezen_file(file):
    f = open(file, "r")
    uniekelijst = set()
    if f.mode == "r":
        for line in f:
            aa=re.compile(r'\s*([0-9]+(?:\.[0-9]+){3})').findall(line)
            if len(aa)>2:
                source=aa[0]
                destination=aa[3]
            else:
                source=aa[0]
                destination=aa[1]
            uniek = "src;{};dest;{}".format(source,destination)
            uniekelijst.add(uniek)
    return uniekelijst


lijst = inlezen_file("log.txt")
f=open("output.txt", "w+")
for line in lijst:
    f.write(line+"\n")



