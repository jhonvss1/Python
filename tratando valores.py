contador = 0
numero = 0 
somavalores = 0 
while numero != 999:
    contador +=1
    numero = int(input("Digite um número: [999] para parar "))
    somavalores = somavalores+numero
print (f"Você digitou {contador} números e a soma entre eles é {somavalores}")
if numero == 999:
        print("Finalizando...")
print("Programa Finalizado!")
     