#Construa um programa que solicite ao usuário dois números positivos. Em seguida, o programa deve apresentar o seguinte menu.1  Média ponderada, com pesos 2 e 3, respectivamente / 2. Quadrado da soma dos 2 números / 3. Cubo do menor número / Escolha uma opção:De acordo com a opção informada, o programa deve calcular a operação apresentada no menu. Se a opção escolhida for inválida, o programa deve mostrar a mensagem “Opção inválida” e ser encerrado. 

n1 = float(input("Digite o 1° numero: "))
n2 = float(input("Digite o 2° numero: "))

print("\n1. Média ponderada \n2. Quadrado da soma dos 2 números \n3. Cubo do menor número\n ")

i = int(input("Escolha a opção: "))

while i != 0:
    if i == 1:
        res = (n1*2 + n2*3)/5
        print("A média ponderada é de ".res)
    elif i == 2:
        print()
    elif i == 3:
        print()
    else:
        exit()
