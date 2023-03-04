n1 = int(input("digite o 1 n:"))
n2 = int(input("digite o 2 n:"))
n3 = int(input("digite o 3 n:"))
if n1 == n2 or n2 == n3 or n1 == n3:
    exit() #encerra programa 
elif n1 > n2 and n1 > n3:
    print("o n1 é maior")
elif n2 > n1 and n2 > n3:
    print("o n2 é maior")
elif n3 > n1 and n3 > n2:
    print("o n3 é maior")