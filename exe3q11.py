# 11. Crie uma função que recebe temperatura de uma pessoa
# e retorna “Está	 com	 febre”	 ou	 “Sem	 febre”.
# Considere o valor base como 36.5

def Febre(t):
    if t > 36.5:
        return "Está com febre"
    else:
        return "Sem febre"
t = float(input("Digite sua temperatura:"))
print(Febre(t))