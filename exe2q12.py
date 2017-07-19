#Recebe quatro números e imprima a média ponderada, sabendo-se que os pesos são respectivamente 1, 2, 3 e 4.
def media_ponderada(a,b,c,d):
    m = (a*1 + b*2 + c*3 + d*4)// (1+2+3+4)
    return (m)
a = int(input("qual o primeiro número?:"))
b = int(input("qual o segundo número?"))
c = int(input("qual o terceiro número?:"))
d = int(input("qual o quarto número?:"))
print("a média ponderada dos números digitados é:",media_ponderada(a,b,c,d))