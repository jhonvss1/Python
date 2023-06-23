print('----------------------CALCULADORA-----------------------------')
continuar = "S"
while continuar == "S":
    num1 = float(input('Digite o numero: '))
    op = str(input('Qual operação deseja realizar? [+ - * / // %] '))
    num2 = float(input('Digite o outro numero: '))
    if op == '+':
        print('O resultado de {} + {} =  {}'.format(num1,num2,num1+num2))
    if op == '-':
        print('O resultado de {} - {} = {}'.format(num1,num2,num1-num2))
    if op == '*':
        print('O resultado de {} * {} = {}'.format(num1,num2,num1*num2)) 
    if op == '/':
        print('O resultado de {} / {} = {:.2f}'.format(num1,num2,num1/num2))
    if op == '//':
        print('O resultado entre {} // {} = {}'.format(num1,num2,num1//num2))
    if op == '%':
        print('O resultado entre {} % {} = {}'.format(num1,num2,num1%num2))
    continuar = str(input("Deseja realizar outra operação? [S/N]: ")).upper()
if continuar == "N":
    print("-----------------------------")
    print ("Programa Finalizado")
print('-----------------------------')