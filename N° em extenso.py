def numero_por_extenso():
    unidades = ("Zero", "Um","Dois","Três","Quatro","Cinco", "Seis" ,"Sete", "Oito","Nove" )
    especiais = ("Dez", "Onze", "Doze","Treze", "Quartoze", "Quinze", "Dezesseis", "Dezessete","Dezoito", "Dezenove")
    dezenas = ("Dez", "Vinte", "Trinta","Quarenta", "Cinquenta", "Sessenta","Setetenta","Oitenta","Noventa")
    centenas  = ("Cem","Cento", "Duzentos", "Trezentos", "Quatrocentos", 
                 "Quinhentos", "Seiscentos", "Setecentos", "Novecentos", "Mil")
    while True:
            numero = int(input("Digite um número entre 0 - 99 : "))
            if 0 <= numero < 10:
                return unidades[numero]
                #Validando o número digitado pelo usuário
            elif 10 <= numero < 20:
                return especiais[numero - 10]
            elif 20 <= numero < 100:
                dezena = dezenas[numero // 10 - 1]
                unidade = numero % 10 
                if unidade > 0:
                    return dezena + " e " + unidades[unidade]
                else:
                    return dezena
            elif 100 <= numero <1000:
                centena = centenas[numero // 100]
                dezena = (numero%100) // 10
                unidade = numero % 10 
extenso = numero_por_extenso()
print(extenso)
