#2. Construa um programa que receba do usuário a variação do deslocamento de um objeto (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o programa deve calcular a velocidade média, em m/s, do objeto.
deslocamento_em_m = float(input("Insira seu deslocamento em metros: "))
tempo_em_seg = float(input("Insira o tempo do deslocamento em segundos: "))
velocidade_media = deslocamento_em_m/tempo_em_seg
print(f"A velocidade média é de {velocidade_media} m/s.")
