#06. Crie uma função que recebe um valor real e retorna a mensagem
#“Vá ao cinema” se o valor recebido for superior a R$20,00 ou
#“Fique vendo TV” caso contrário

def Sair(n):
    if n > 20:
        return "Vá ao cinema"
    else:
        return "Fique vendo TV"
n = float(input("Digite um valor real (R$):"))
print(Sair(n))