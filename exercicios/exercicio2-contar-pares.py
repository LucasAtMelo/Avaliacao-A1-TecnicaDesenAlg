from time import sleep # função do módulo python que faz "o computador esperar"

print("""
1. Contador com For 
2. Contador com While 
""") #interface para escolha de método 

escolha = int(input('Digite a forma como você quer contar: ')) # escolha do usuário atribuido a uma váriavel 

if escolha == 1:  #se a escolha for com For 
    for contador in range(1, 101, 1): #o contador for conta de 1 até 100(descartando 1 ) com passo 1 
        print(contador) #mostra o passo atual do laço 
        sleep(0.5) #espera metade de um segundo 
    print('Fim :)') # mensagem final

elif escolha == 2:  #se a escolha for com While 
    contador = 0  #contador atribuido a uma variavel 
    while contador < 100: # enquanto o contador for menor que 100
        contador += 1  #adiciona um ao contador 
        print(contador) #mostra o passo atual do laço 
        sleep(0.5) #espera metade de um segundo 
    print('Fim :)') # mensagem final 
