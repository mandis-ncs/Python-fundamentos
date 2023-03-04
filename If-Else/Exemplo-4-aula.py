print("##Programa de emprestimos##. responda: 0 - nao ou 1 - sim")
nomenegativo = int(input("possui nome negativo?"))
if nomenegativo == 1:
    print("##nao pode realizar emprestimos")
else:
    carteiraassinada = int(input("possui carteira assinada"))
    if carteiraassinada == 0:
        print("##nao pode realizar emprestimos")
    else:
        possuicasapropria = int(input("possui casa propria"))
        if possuicasapropria == 0:
            print("##nao pode realizar emprestimos")
        else:
            print("##conceder emprestimos")