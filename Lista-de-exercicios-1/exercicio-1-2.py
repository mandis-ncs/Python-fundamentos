#converter km/h em m/s. O fator de conversão é 3.6 km/h -> (divisao) -> m/s ou m/s -> (produto) -> km/h
escolha = int(input("Escolha: 1) para converter km/h em m/s ou 2) para converter m/s em km/h: "))
if escolha==1:
    conversao1= float(input("Digite o valor em km/h: "))
    resultado=conversao1/3.6
    print(f"O valor em m/s é igual a {resultado:.2f} m/s")
else:
    conversao2 = float(input("Digite o valor em m/s: "))
    resultado = conversao2*3.6
    print(f"O valor em km/h é igual a {resultado:.2f} km/h")