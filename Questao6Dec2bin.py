Numero = int(input('Entre com o valor decimal: '))

k = []

while (Numero > 0):
    a = int(float(Numero%2))
    k.append(a)
    Numero = (Numero-a) / 2
k.append(0)
string=""

for j in k[::-1]:
    string=string+str(j)

print('Em binário: %s'%(string))