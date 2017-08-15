#05. Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo
# até que o usuário informe um valor válido.

n = int(input("Digite um valor entre 0 e 10:"))
while n < 0 or n > 10:
    n = int(input("Digite um valor entre 0 e e 10:"))