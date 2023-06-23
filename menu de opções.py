valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
opcao = 0
resultado = 0 
while opcao != 5:
    print("""        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa""")
    opcao = int(input(">>>>>>>> Qual a sua opção?  "))
    if opcao == 1:
        resultado = valor1+valor2
        print("O resultado da soma entre {} + {} é {}".format(valor1, valor2,resultado))
    elif opcao ==2: 
        resultado = valor1 * valor2
        print("O resultado da multiplicaçao entre {} x {} é {}".format(valor1, valor2, resultado))
    elif opcao == 3:
        if valor1 > valor2:
            resultado = valor1
            print("O maior número é {}".format(resultado))
        else:
            resultado = valor2
            print("O maior número é {}".format(resultado))
    elif opcao == 4:
        valor1 = int(input("Novo primeiro valor: "))
        valor2 = int(input("Novo segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção Inválida")
    print("-=-"*20)
print("Fim do programa") 