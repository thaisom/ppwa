#Recebe o ano de nascimento de uma pessoa e escreva na tela a sua idade em 31/12/2013.
def idade(x):
    return 2013 - x
x = int(input("digite seu ano de nascimento:"))
print(idade(x))