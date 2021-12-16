litros = int(input("Digite quantos litros o cliente abasteceu: "))
combustivel = input("Digite E para Etanol ou G para Gasolina (maiusculo): ")
preco = 0
if combustivel == "E":
    preco = litros * 3.5
    if litros <= 5:
        preco -= 3.5 * litros * 0.035
    else:
        preco -= 3.5 * litros * 0.07
elif combustivel == "G":
    preco = litros * 5.25
    if litros <= 5:
        preco -= 5.25 * litros * 0.0432
    else:
        preco -= 5.25 * litros * 0.0832
print(f"O preço é R${preco:.2f}")