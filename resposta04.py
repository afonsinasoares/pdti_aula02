nota1 = input("Digite a nota do NPC1: ")
nota2 = input("Digite a nota do NPC2: ")
nota1 = int(nota1)
nota2 = int(nota2)
media = (nota1 + nota2) /2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")