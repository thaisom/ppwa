# Recebe 2 números inteiros, retorne o quociente e o resto da divisão do 1º pelo 2º.
# Recebe um número inteiro e imprima de volta na tela.
def quociente_resto(x,y):
    d = x // y
    q = x % y
    return (d,q)
x = int(input("Digite um número inteiro:"))
y = int(input("Digite outro número inteiro:"))
print("O quociente e o resto dessa divisão são respectivamente:",quociente_resto(x,y))