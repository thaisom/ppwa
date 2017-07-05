#20. Faça uma função que retorna o IMC de uma pessoa, e depois, exiba uma das seguintes mensagens:
# < 18,5 Abaixo	do	peso
# < 25 Peso	normal
# < 30 Sobrepeso
# < 35 Obeso leve
# < 40 Obeso moderado
# >=40 Obeso mórbido
def Imc(m,h):
    i = m / (h ** 2)
    if i < 18.5:
        return "Abaixo	do	peso"
    elif i < 25:
        return "Peso normal"
    elif i < 30:
        return "Sobrepeso"
    elif i < 35:
        return "Obeso leve"
    elif i < 40 :
        return "Obeso moderado"
    elif i >= 40:
        return "Obeso mórbido"
m = float(input("Digite seu peso:"))
h = float(input("Digite sua altura:"))
print(Imc(m,h))