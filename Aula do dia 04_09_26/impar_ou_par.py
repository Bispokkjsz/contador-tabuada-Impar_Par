# crie um programa que leia um numero se a pessoa quer impar ou par
# E de os impares ou pares em sequencia
# ex: 3 e a pessoa escolheu um impar 
# 1, 3, 5

numero = int(input('Escolha a quantidade: '))
escolha = str(input('Voce quer impar ou par? '))
 
contador = 1

contador_par = 2

contador_impar = 1

if escolha == 'par':
    while contador <= numero:
        print(f"{contador_par}")
        contador_par +=2
        contador +=1
if escolha == "impar":
    while contador <= numero:
        print(f"{contador_impar}")
        contador_impar +=2
        contador +=1