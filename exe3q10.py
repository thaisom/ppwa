# 10. Escreva uma função que recebe a distância(em Km) e o tempo (em horas)
# de uma viagem, e retorne a velocidade	média da viagem.

def Distancia(s,t):
    vm = s // t
    return vm
s = int(input("Digite a distancia(em Km) da viagem:"))
t = int(input("Digite o tempo(em hora) da viagem:"))
print("A velocidade media é:", Distancia(s,t), "Km/h")
