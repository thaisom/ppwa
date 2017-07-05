#03.Faça uma função que recebe dois números
#por parâmetro e retorna o maior

def Maior(n1, n2):
    if n1 > n2 :
        return n1
    else:
        return n2

n1 = int(input("Digite um numero:"))
n2 = int(input("Digite um numero:"))
print("O maior numemro digitado foi:", Maior(n1, n2))