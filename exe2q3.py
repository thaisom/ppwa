#Recebe um valor em minutos, retorna o equivalente em horas e minutos.
def hora_minuto(m):
    h = m //60
    n = m % 60
    return "%d horas e %d minutos" % (h,n)
m = int(input("Digite o tempo:"))
print(m,"minutos equivalem a",hora_minuto(m))