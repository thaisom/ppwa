#Recebe uma velocidade em km/h, retorne esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)
def velocidade(m):
    k =  m // 3.6
    return k
m = int(input("Digite a velocidade em Km/h:"))
print(m,"Km/h equivale a ",velocidade(m),"m/s")