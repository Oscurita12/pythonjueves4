numero = 5
'''
while(numero<10):    
    print("Estoy a dentro de la cuerda")
    numero+=1
else:   
    print("El ciclo terminó")
  
print("Estoy por fuera de la cuerda")
'''

opcion=1
print("*****Menu*****")
print("1. SUMAR")
print("2. RESTAR")
print("0. SALIR")

while(opcion != 0): 
    opcion=int(input("Digite una opción: "))
    if(opcion==1):  
        print("Sumando")
    elif(opcion==2):    
        print("Restando")
    elif(opcion==0):    
        break
    else:   
        print("Digite una opción válida")
