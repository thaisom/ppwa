# 12. Escreva	uma	função	que	recebe	um	número	inteiro	e
# retorna	a mensagem	“O	número	é	múltiplo	de	7”
# ou	“O	número	não	é	múltiplo	de	7”.

def Multiplo(n):
    if n % 7 == 0:
        return "O numero e multiplo de 7"
    else:
        return "O numero não e multiplo de 7"
n = int(input("Digite um numero:"))
print(Multiplo(n))