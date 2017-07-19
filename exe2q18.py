# Recebe dois valores para as variáveis A e B, efetuar a troca dos valores de forma que a variável A passe a ter o valor de B e
# que a variável B passe a ter o valor de A. Mostrar na tela os valores trocados.
def trocar(a,b):
    a,b=b,a
    return a,b
a= int(input("Digite um valor de a:"))
b= int(input("Digite um valor de b:"))
print(trocar(a,b))