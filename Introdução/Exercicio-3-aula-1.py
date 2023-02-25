#3. Construa um programa para calcular a área de convivência de uma escola cujo formato é circular. Para isso, o usuário deve informar o valor do raio

from math import pi
raio = float(input("Insira o raio: "))
area = pi*raio**2 #poderia usar pi*pow(raio,2)
print(f"A área do círculo é de {area:.2f}.")
