numero = int(input('DIGITE UM NUMERO: '))

contador = 0

while(contador <= 10):      # while significa ENQUANTO
    resultado = numero * contador
    print(f'{numero}x{contador}={resultado}')
    contador += 1    # variavel += 1 sigifica: variavel = variavel + 1
    