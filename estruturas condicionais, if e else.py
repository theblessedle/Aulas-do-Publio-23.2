#def valor_de_x(n):
    #if n < 5:
     #   return "valor baixo"
    #elif 5 < n < 10:
     #   return "valor médio"
    #elif n > 10:
     #   return "valor alto"
#print(valor_de_x(2))
#print(valor_de_x(11))
#print(valor_de_x(7))



nome_do_curso = "Introdução a Informática para Controle"
codigo_do_curso = "DAS5334"

x = input("Matéria: ")
y = input("Código: ")

if x == nome_do_curso and y == codigo_do_curso:
    print("Matéria correta")
elif x == nome_do_curso and y != codigo_do_curso:
    print("Nome correto, porém código errado")
elif x != nome_do_curso and y == codigo_do_curso:
    print("Nome errado, porém código correto")
else:
    print("Matéria errada")

