from random import randint
usuario= 0
tentativas = 0 
print ("--------------- VAMOS JOGAR -------------------")
computador = randint(1,50)
print("Acabei de pensar em um número. ")
while usuario != computador:
        usuario = int(input("Adivinhe o número que estou pensando entre 1 - 50: "))
        if usuario > computador:
                print("Menos...")
        elif usuario < computador:
                print("Mais...")
        if usuario == computador:
                    print("Você venceu. Parabéns!")
        elif usuario != computador:
                tentativas+=1
print("Você tentou {} vezes".format(tentativas))
