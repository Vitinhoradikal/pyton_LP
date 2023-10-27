import math

a = int(input("Digite o primeiro valor.\n"))
b = int(input("Digite o segundo valor.\n"))
c = int(input("Digite o terceiro valor.\n"))

#a area está sendo calculada com a fórmula de Heron que calcula a área de qualquer triangulo válido
# a condição do if verifica se os valores inseridos formam um triangulo ou não
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("A área do triângulo é", area)
else:
    print("Os valores fornecidos não formam um triângulo\n a = ",a,"\n b = ",b,"\n c = ", c)