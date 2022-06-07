print("CALCULANDO O FATORIAL DE UM NÚMERO")
num = int(input("Digite um número para descobrir o seu fatorial: "))

if num > 0:
    fat = 1
    for item in range(1,num + 1):
        fat = fat * item
print("O fatorial de", num, "é igual a:", fat)