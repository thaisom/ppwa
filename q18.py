# Questão 18:   P(x) = Ax4 + Bx3 + Cx2 + Dx + E
a = int(input('Digite o valor do coeficiente de A:'))
b = int(input('Digite o valor do coeficiente de B:'))
c = int(input('Digite o valor do coeficiente de C:'))
d = int(input('Digite o valor do coeficiente de D:'))
e = int(input('Digite o valor do coeficiente de E:'))
x = int(input('Digite o valor de x:'))
p = a*x*4 + b*x*3 + c*x*2 + d*x + e
print('O valor do polinômio P(x) é:', p)