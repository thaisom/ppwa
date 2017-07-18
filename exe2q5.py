#Recebe uma velocidade em m/s, retorne esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)
def velocidade(m):
    k =  m * 3.6
    return k
m = int(input("Digite a velocidade em m/s:"))
print(m,"m/s equivale a ",velocidade(m),"Km/h")