#Variable de control
numero=0

#Acumulador
suma=0

#Declaro el ciclo 
while(numero>=0):    
    #Pedir un número
    numero=int(input("Digite un número: "))

    if(numero>=0):  
        suma=suma+numero
    else:
        print(f'La suma fue: {suma}')
        break
print(f'La suma fue: {suma}')