#16. Crie uma função que recebe um número inteiro e retorne qual mês do ano o mesmo corresponde.
# Se o valor for maior que doze ou menos que um, diga que o valor não corresponde a nenhum mês.
def Mes(n):
    if n == 1:
        return "Janeiro"
    elif n == 2:
        return "Fevereiro"
    elif n == 3:
        return "Março"
    elif n == 4:
        return "Abril"
    elif n == 5:
        return "Maio"
    elif n == 6:
        return "Junho"
    elif n == 7:
        return "Julho"
    elif n == 8:
        return "Agosto"
    elif n == 9:
        return "Setembro"
    elif n == 10:
        return "Outubro"
    elif n == 11:
        return "Novembro"
    elif n == 12:
        return "Dezembro"
    else:
        return "O valor digitado não corresponde a um mês do ano"
n = int(input("Digite um número de 1 a 12:"))
print(Mes(n))