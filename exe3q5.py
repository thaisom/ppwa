# 05. Crie uma função que recebe um número por parâmetro
# e retorna o valor booleano verdadeiro se o número	for	par

def Par(n):
    if n % 2 == 0:
        return "Verdadeiro"
    else:
        return "Falso"

n = int(input("Digite um numero:"))
print(Par(n))