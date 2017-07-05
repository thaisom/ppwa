#19. Escreva uma função que recebe a cor de um sinal de trânsito(“V” é verde; “A” é amarelo; “E” é vermelho)
# e retorne a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.
def SinalDeTransito(x):
    if x == "v":
        return "Siga"
    elif x == "a":
        return "Atenção"
    elif x == "e":
        return "Pare"
x = input("Digite a cor do sinal de transito(v, a ou e):")
print(SinalDeTransito(x))