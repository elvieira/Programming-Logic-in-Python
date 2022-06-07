import random

va = random.randint(1,10)
print("TENTE ACERTAR O NÚMERO QUE FOI GERADO")
vu = int(input("Digite um número de 1 a 10: "))

while True:
    if vu >= 11 & vu == 0:
        vu = int(input("Número inválido! Digite um número de 1 a 10: "))
    elif vu < va:
        vu = int(input("Chute foi menor que o valor gerado! Digite outro número: "))
    elif vu > va:
        vu = int(input("Chute foi maior que o valor gerado! Digite outro número: "))
    elif vu == va:
        print("Parabéns, você acertou!")
        break