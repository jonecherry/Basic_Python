#coding=utf-8
line = raw_input()
line = line.split()
newline =''
for i in range(len(line)):
    newline = newline +line[len(line)-i-1]+' '
print newline