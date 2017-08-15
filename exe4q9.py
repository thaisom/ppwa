soma = 0
n = []

for c in range(24, 200, 2):
    n.append(c)

for c in range(0, len(n)):
    soma += c

print("A soma dos números pares entre 25 e 200 é %d." % soma)