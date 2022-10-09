
import time

print("Informe o tempo em segundos para a bomba detonar:")

tempo = int(input())

print("====Iniciando contagem regressiva====\n")


for item in range(tempo, 0, -1):
   
    print(item)
    time.sleep(1)
    
print("BUUUMMM!!!!")