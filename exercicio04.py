def primo(numero):

        if numero <= 1:
            return False #se um numero for igual ou menor que 1 ele não é primo
        if numero <=3:
            return True # se o número for 2 ou 3 ele é primo
        if numero % 2 == 0 or numero % 3 == 0:
            return False # se o resto da divisão dele por 2 ou 3 for 0 ele não é um primo

        i = 5 # teste para os números maiores
        while i * i <= numero: #enquanto o a multiplicação dos indices for menor ou igual ao número verifique:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6

        return True

array = list(range(1,101))

primos = 0

n_primos = 0

for i in range(100):
   print(array[i],": ", primo(array[i]))