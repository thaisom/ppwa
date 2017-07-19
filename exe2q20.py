# Um algoritmo para realizar os saques de um caixa eletrônico deve possuir algum mecanismo para decidir o número de notas
# de cada valor que deve ser disponibilizado para o cliente que realizou o saque. Um possível critério seria o da "distribuição
# ótima" no sentido de que as notas de menor valor disponíveis fossem distribuídas em número mínimo possível. Por exemplo,
# se a máquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo
# deveria indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que
# receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o critério da distribuição ótima.
def saque(s):
    n50 = s // 50
    s = s % 50

    n10 = s // 10
    s %= 10

    n5 = s // 5
    s %= 5

    n1 = s

    return (
        "R$ 50,00: %d notas;\n" % n50 +
        "R$ 10,00: %d notas;\n" % n10 +
        "R$ 5,00: %d notas;\n" % n5 +
        "R$ 1,00: %d notas;\n" % n1
    )
s = float(input("Digite o valor a ser sacado:"))
print(saque(s))