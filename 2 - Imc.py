peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print("Seu IMC é de ", imc)

if imc < 18.5:
    print("Abaixo do peso normal.")
elif imc >= 18.5 and imc < 25:
    print("Peso normal.")
elif imc >= 25 and imc < 30:
    print("Excesso de peso")
elif imc >= 30 and imc < 35:
    print("Obesidade Classe I")
elif imc >= 35 and imc < 40:
    print("Obesidade Classe II")
else:
    print("Obesidade Classe III")