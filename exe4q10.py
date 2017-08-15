n = []
soma = 0
x = int(input("x = "))
i = 1
while i <= x:
    if i % 5 == 0:
        soma += i
    i += 1
print("A soma dos números múltiplos de cinco no intervalo entre 1 e %d é %d." % (x, soma))