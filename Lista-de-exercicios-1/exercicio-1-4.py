#pedir valor do salario minimo, pedir valor salario do user, calcular qnts salarios minimos ele recebe
salmin= float(input("Digite o valor atual do salário mínimo: "))
salatual= float(input("Digite o valor do seu salário atual: "))

qtdesalarios= int(salatual/salmin)
print(f"Você recebe o equivalente a {qtdesalarios} salários mínimos.")