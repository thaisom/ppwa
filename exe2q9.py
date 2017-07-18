#Recebe um número inteiro e imprima na tela seu antecessor e o seu sucessor
def suc_ant(x):
    s = x+1
    a = x-1
    return (s,a)
x = int(input("Digite um número:"))
print("O sucessor e o antecessor de",x,"são respectivamente:",suc_ant(x))