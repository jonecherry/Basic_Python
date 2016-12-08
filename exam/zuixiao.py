#coding=utf-8
line = raw_input()
cuan = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
NEWCUAN = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
arr = []

def quzifu(cc,ci):
    newcc = []
    yichuguo = 0
    for ccc in cc:
        newcc.append(ccc)
    for cccc in newcc:
        if ci== cccc:
            newcc.remove()
if 'X' in line:
    arr.append("SIX")
    for zi in "SIX":
        line = line.replace(zi,'')
if 'V' in line:
    arr.append("SEVEN")
    for zi in "SEVEN":
        line = line.replace(zi,'')
if 'Z' in line:
    arr.append("ZERO")
    for zi in "ZERO":
        if zi in line:
            line = line.replace(zi,'')
print line
if 'G' in line:
    arr.append("EIGHT")
    for zi in "EIGHT":
        if zi in line:
            line = line.replace(zi,'')

for i in NEWCUAN:
    isin = True
    for cha in i:
        if cha not in line:
            isin =False
    if isin:
        arr.append(i)
    for zi in i:
        line = line.replace(zi,'')

print arr