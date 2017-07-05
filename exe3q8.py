#08. Crie	uma	função	que	recebe	um	número	inteiro	e
# retorne	a	mensagem	positivo,	negativo	ou	igual
# a	zero,	de	acordo	com	o	valor	recebido

def sinal(n):
    if n > 0:
        return "positivo"
    if n < 0:
        return "negativo"
    else:
        return "zero"
n = int(input("Digite um numero:"))
print(sinal(n))