#04. Faça uma função que recebe	três números por parâmetro
# e imprime na tela em	ordem crescente.
def imprimeOrdemCrescente(a, b, c):
    if a < b and a < c:
        if b < c:
            return(a,b,c)
        else:
            return(a, c, b)
    elif b < a and b < c:
        if a < c:
            return(b,a,c)
        else:
            return(b,c,a)
    elif c < a and c < b:
        if a < b:
            return(c, a, b)
        else:
            return(c, b, a)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print("A ordem crescente dos numeros digitados e:",imprimeOrdemCrescente(a,b,c))