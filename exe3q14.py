#14. Crie uma função que recebe o ano de nascimento de uma pessoa e retorna uma mensagem
# que diga se ela poderá ou não votar em uma eleição para prefeito,
# não é necessário considerar o mês ou o dia que ela nasceu.
def Idade(i):
    x = 2017 - i
    if x >= 18:
        return "Pode votar"
    else:
        return "Não pode votar"
i = int(input("Digite seu ano de nascimento:"))
print(Idade(i))