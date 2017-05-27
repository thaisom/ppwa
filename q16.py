# Questão 16:Efetue o cálculo e a apresentação do valor de uma
# prestação em atraso utilizando a fórmula PRETAÇÃO =
# VALOR + (VALOR * (TAXA / 100) * TEMPO)
valor,taxa,tempo = float(input('Digite o valor da prestação:')), float(input('Digite a taxa da prestação:')), float(input('Digite o tempo da prestação em meses:'))

p = valor + (valor * (taxa / 100) * tempo)
print('O valor da prestação em atraso é:', p)
