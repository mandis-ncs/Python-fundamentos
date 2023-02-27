#solicitar nome do corretor, qtde imoveis vendidos, valor total de vendas
#calcular salario total
#salario base = 1500; comissao de 200 por imovel vendido; 5% do valor de cada venda

salbase=1500
comissao=200
taxa=0.05

nome=input("Digite o nome do corretor: ")
qtdeimoveis= int(input("Digite a quantidade de imoveis vendidos: "))
valorvendas= int(input("Digite a o valor total de vendas: "))

saltotal= (qtdeimoveis*comissao)+(valorvendas*taxa)+salbase
print(f"O salario total do corretor {nome} é de R${saltotal:.2f}.")