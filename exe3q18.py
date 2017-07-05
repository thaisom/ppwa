#18. Crie uma função que recebe três valores inteiros e retorna o maior delas. Suponha não haver empates.
def Maior(a,b,c):
    if a > b and a > c:
        return (a)
    elif b > a and b > c:
        return (b)
    elif c > a and c > b:
        return (c)
a = int(input("Digite um numero:"))
b = int(input("Digite um numero:"))
c = int(input("Digite um numero:"))
print("O maior numero eh:",Maior(a,b,c))