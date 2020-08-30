# Faça um algoritmo que peça dois números e imprima o maior deles

numero1 = input('Digite o primeiro valor: ')
numero2 = input('Digite o primeiro valor: ')

numero1 = int(numero1)
numero2 = int(numero2)

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
elif numero1 < numero2:
    print(f'{numero2} é maior que {numero1}')
else:
    print('Os dois números são iguais!')
