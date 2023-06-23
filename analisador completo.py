somaidade = 0
maioridadehomem = 0
maisvelho = ""
for p in range(1,5):
    print('-'*20)
    nome = str(input("Informe o seu nome: ")).strip().capitalize()
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe seu sexo [M/F]: ")).upper()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem += 1
    if sexo in "Mm" and idade < maioridadehomem:
        maisvelho = nome

mediaidade = somaidade/4
print("A média de idade nesse grupo é de : {}".format(mediaidade))
print("O homem mais velho se chama {} e tem {} anos".format(maisvelho,maioridadehomem))