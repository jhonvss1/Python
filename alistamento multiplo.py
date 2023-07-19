from datetime import datetime
pessoas_cadastradas = []

print('ALISTAMENTO MILITAR')
print("-="*30)
while True:
    pessoas = {}
    pessoas['nome'] = str(input("Nome e sobrenome: ")).title()
    
    nome_sem_espaço = pessoas['nome'].replace(" ", "")

    if not isinstance(pessoas['nome'], str) or len(pessoas['nome'])  <=2 or not nome_sem_espaço.isalpha():

        print("Nome inválido")

        break

    pessoas['sexo'] = str(input("Sexo: Masculino [M] - Feminino [F]: ")).strip().upper()

    while pessoas['sexo'] not in "MF":

        pessoas['sexo'] = str(input("Sexo: Masculino [M] - Feminino [F]: ")).strip().upper()

        if pessoas['sexo'] == "M":

            pessoas['sexo'] = "Masculino"

        elif pessoas['sexo'] == "F":

            pessoas['sexo'] = "Feminino"

    pessoas['ano'] = int(input("Ano de nascimento: "))

    pessoas['idade'] = datetime.now().year - pessoas['ano']

    if pessoas['idade'] == 18:

        pessoas['situação'] = "Alistado"

    elif pessoas['idade'] > 18 and pessoas['idade'] <= 24:

        pessoas['situação'] = "Vá a uma junta mais próxima e se aliste"

    elif pessoas['idade'] <= 17:

        anos_de_espera = 17 - pessoas['idade']  

        pessoas['situação'] = f"Ainda não está no tempo volte daqui a {anos_de_espera} anos"

    pessoas_cadastradas.append(pessoas)

    continuação = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]

    if continuação == "N":
            
            break
for contador,pessoas in enumerate (pessoas_cadastradas,1):
    print(f"\nInformações do {contador}°: ")
    print("-="*30)
    for key,value in pessoas.items():
        
        print(f"{key} : {value}")
print("-="*30)
# Falta fazer a cópia das informações das pessoas e printar elas na tela