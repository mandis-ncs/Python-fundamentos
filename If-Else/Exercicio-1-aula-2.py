#Escreva um programa que solicite ao usuário a estatura de 3 pessoas. Ao fim, o programa deve imprimir as estaturas em ordem decrescente. 

est1 = input("Insira a 1º estatura:")
est2 = input("Insira a 2º estatura:")
est3 = input("Insira a 3º estatura:")

#Comparação, revela a maior estatura
if est1 == est2 or est2 == est3 or est1 == est3:
    exit() #encerra programa 
elif est1 > est2 and est1 > est3:
    print("a pessoa de estatura n° 1 é mais alta")
elif est2 > est1 and est2 > est3:
    print("a pessoa de estatura n° 2 é mais alta")
elif est3 > est1 and est3 > est2:
    print("a pessoa de estatura n° 3 é mais alta")

#cria array estatura e printa com o método sort em ordem crescente
#array.sort(reverse=True) -> usa o reverse para ordenar decrescente
estatura = [est1, est2, est3]
estatura.sort(reverse=True)
print(estatura)