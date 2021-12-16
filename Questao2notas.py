n=int(input("Insira o número total de notas: "))

i=0

Notas=[]

for i in range(i,n):

    Notas.append(int(input("Insira o valor das notas: ")))

print(Notas)

Xi = 0

N = len(Notas)
for notasi in Notas:
    Xi +=notasi

print ("Esta é a média aritmética: ", Xi/N)

pi = []
xi = []

notaponderai = []

for i in range (i,n):
    pi.append(int(i=i+1))
    app2=float(pi*xi)
    notaponderai.append(app2)

PiXi = 0
Nponderadai = len(notaponderai)

for pixi in notaponderai:
    PiXi += pixi

Mpond = string(float(PiXi/Nponderadai))

print ("Este é a quantidade de notas para a média ponderada", Nponderadai)
print ("Esta é a média ponderada", Mpond)