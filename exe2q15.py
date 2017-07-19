#Recebe um número no formato CDU e imprima na forma UDC. Exemplo: 123, sairá 321. O número deve ser armazenado em
# outra variável antes de ser impresso.
def inverte(n):
    num = str(n)
    if len(num) == 3:
        return num
    else:
        return 0
n = int(input("Forneça um número de três algarismos: "))
print(inverte(n)[::-1])