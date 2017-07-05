#07. Crie uma função que recebe o nome e o sexo de uma pessoa,
# e	retorne a mensagem “Ilmo Sr.”, caso seja informado o sexo masculino,
# ou “Ilma Sra.”, caso seja informado o	sexo feminino. Retorne junto com cada
# mensagem	de	saudação o nome que foi informado.

def SrOuSra(n,s):
    if s == "F":
        return "Ilma Sra."
    else:
        return "Ilmo Sr."
n = input("Digite seu nome:")
s = input("Sexo (M ou F):")
print(SrOuSra(n,s))