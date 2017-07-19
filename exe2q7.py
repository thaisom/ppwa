# Recebe 2 números, retorne a divisão da soma pela subtração dos números lidos
def divisao(x,y):
    return (x+y)//(x-y)
x = int(input("Digite um valor:"))
y = int(input("Digite outro valor:"))
print(divisao(x,y))