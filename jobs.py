f = open('C:/Users/Jackson Ferreira/Desktop/companies email/allLinks.txt', 'r')
# esse programa diz o numero de repetidos
dic = {}
for line in f:
    if not (line in dic):
        dic[line] = 1
    else:
        dic[line] = dic[line] + 1
print(dic)

f = open('C:/Users/Jackson Ferreira/Desktop/companies email/allLinks.txt', 'r')
# esse programa não inclui repetidos
tes = []
for line in f:
    if not (line in tes):
        tes.append(line)

#print(sorted(tes))
print(tes)

arq = open('C:/Users/Jackson Ferreira/Desktop/companies email/uniqueLinks.txt', 'w')
for linha in tes:
    arq.write(linha)

arq.close()