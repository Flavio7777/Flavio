valor = float(input('Entre com o valor: '))

notas = [50,20, 10, 5, 2, 1]

i = 0

if valor > 387:
	print('Não possível retornar o troco')

else:

	while valor > 0:
		n = valor/notas[i]
		valor = valor%notas[i]
		if int(n) != 0:
			print('%d notas de R$ %.2f' %(n, notas[i]))
		i += 1