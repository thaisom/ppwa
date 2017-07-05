# 13. Escreva uma função que retorne “verdadeiro”
# se um número recebido for par e divisível por 3.
def div3(x):
    return x % 3 == 0

x = int(input("Digite um numero:"))
print(div3(x))