# Calcular b elevado a n:
b = int(input("Digite valores inteiros (b >= 2):"))
n = int(input("Digite valores inteiros (n > 1):"))
while b < 2 or n < 1:
    try:
        b = int(input("Digite valores inteiros (b >= 2): "))
        n = int(input("Digite valores inteiros (n > 1):" ))
    except:
        print("Não foram fornecidos valores inteiros.")
print(b,"elevado a",n,"é:",pow(b,n))