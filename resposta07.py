#Faça um algoritmo que leia três números e mostre o maior deles.
numero1 = int(input("Digite um valor inteiro: "))
numero2 = int(input("Digite um valor inteiro diferente do primeiro: "))
numero3 = int(input("Digite um valor inteiro diferente dos outros dois: "))

if numero1 < numero2:
    if numero2 < numero3:
        maior = numero3
        menor = numero1
    else:
        maior = numero2
        menor = numero1
else: #numero1 é maior que numero2
    if numero1 > numero3:
        maior = numero1
        menor = numero3
    elif numero2 < numero3:
        maior = numero3
        menor = numero2
    else:
        maior = numero2
        menor = numero3

print("Maior valor é: ",maior)
print("Menor valor é: ", menor)