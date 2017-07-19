#. Recebe um número inteiro de 3 dígitos e mostre na tela o dígito da casa das dezenas.
def dezenas(d):
    n = str(d)
    if len(n)==3:
        c = d//100
        n = (d - (c * 100)) // 10
        return n
    else:
        return "numero digitado não possui três algarismos"
d = int(input("Digite um numero inteiro com 3 algarismos:"))
print("o algarismos das dezenas do numero digitado é:",dezenas(d))
