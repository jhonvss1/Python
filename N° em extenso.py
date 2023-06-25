numero = 0
def numeros_por_extenso(numero):
    unidades = ("Zero", "Um","Dois","Três","Quatro","Cinco", "Seis" ,"Sete", "Oito","Nove" )
    especiais = ("Dez", "Onze", "Doze","Treze", "Quartoze", "Quinze", "Dezesseis", "Dezessete","Dezoito", "Dezenove")
    dezenas = ("Dez", "Vinte", "Trinta","Quarenta", "Cinquenta", "Sessenta","Setetenta","Oitenta","Noventa")
    while True:
        numero = int(input("Digite um número entre 0 - 99 : "))
        if 0 <= numero < 10:
            break
            return unidades[numero]
            #Validando o número digitado pelo usuário
        elif 10 <= numero < 20:
            return especiais[numero - 10]
        elif 20 <= numero < 100:
            dezena = dezenas[numero // 10 - 1] # Atribuindo o valor da dezena e encontrando ela no índice das dezenas
            unidade = numero % 10 # Encontrando o valor da unidade  
            if unidade > 0:
                return dezena + " e " + unidades[unidade]
            else:
                return dezena
extenso = numeros_por_extenso(numero)
print(extenso)
