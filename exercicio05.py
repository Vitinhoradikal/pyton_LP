def inverte_frase(frase):

    palavras = frase.split() #divide a frase em palavras

    palavras_invertidas = [palavra[::-1] for palavra in palavras] #inverte cada palavra

    nova_frase = ' '.join(palavras_invertidas) #junta todas as palavras em uma frase nova

    return nova_frase

frase =str(input("Digite uma frase.\n")) #pede ao usuário para digitar a frase
frase2 = inverte_frase(frase) #inverte a frase e armazena na variável frase2
print(frase2) #imprime a frase