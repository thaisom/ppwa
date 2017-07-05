# 09. Escreva uma função que recebe e retorne
# o valor booleano "verdadeiro" caso o numero
# seja múltiplo de 5, ou "Falso" caso contrário.

def MultiploDeCinco(n):
    if n % 5 == 0:
        return "Verdadeiro"
    else:
        return "Falso"
n = int(input("Digite um numero:"))
print(MultiploDeCinco(n))