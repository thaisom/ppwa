#Recebe o valor do lado de um quadrado e imprima a sua área e o seu perímetro
def perimetro(l):
    p = l*4
    a = l**l
    return (p,a)
l = int(input("digite o lado de um quadrado"))
print("o perimetro e a área do quadrado são respectivamente:",perimetro(l))