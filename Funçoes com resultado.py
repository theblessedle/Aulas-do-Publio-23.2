#import math
#def soma(n1,n2,n3):
 #   print(n1 + n2 + n3)

#soma(1,2,3)
#soma(3,6,1)


def numero_de_0_a_10(n):
    if 0 <= n <= 10:
        return 0 <= n <= 10
    elif n < 0 or n > 10:
        return "Não válido, digite apenas um número entre 0 e 10"

print(input("Digite um valor de 0 a 10:  "))