#Em época de pouco dinheiro os comerciantes estão procurando aumentar suas vendas oferecendo desconto. Recebe o valor de
# um produto e o percentual de desconto concedido e imprima o valor do produto com desconto
def desconto(p,i):
    v = p - i/100
    return v
p = float(input("Digite o preço da mercadoria:"))
i = float(input("Digite o percentual de desconto:"))
print(desconto(p,i))