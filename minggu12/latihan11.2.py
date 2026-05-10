lista = ['red', 'green', 'blue']
Listb = ['#FF0000','#008000', '#0000FF']

kamus = dict()

for i in range(len(lista)):
    kamus[lista[i]] = Listb[i]

print(kamus)