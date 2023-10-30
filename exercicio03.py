#inicia um array vazio para armazenar os números digitados
array_num = []

#recebe 3 numeros digitados pelo usuário
for i in range(3):
    numero=int(input("Digite um numero.\n"))
    array_num.append(numero)
#percorre o array, determina qual o menor valor e insere na variável "menor"
menor = min(array_num)

print("O menor número é: \n", menor)