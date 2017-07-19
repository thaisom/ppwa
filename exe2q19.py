#Recebe a hora atual no formado HHMM e mostre quantos minutos passaram-se desde início do dia
def horas(h,m):
    a = (h*60)+m
    return a
h = float(input("que horas são agora?:"))
m = float(input("e quantos minutos?:"))
print("Desde o inicio do dia se passaram %d minutos" % horas(h,m))