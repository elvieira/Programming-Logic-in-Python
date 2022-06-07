veloc = int(input("Digite a sua velocidade: "))
if veloc <= 80:
    print("Não houve multa!")
elif veloc in range(81,90):
    print("Levou multa leve!")
elif veloc in range(91,100):
    print ("Levou multa grave!")
elif veloc >= 101:
    print ("Levou multa gravíssima!")