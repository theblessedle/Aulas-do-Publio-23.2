import turtle
a = float(input("valor da largura:  "))
b = float(input("valor da altura:  "))
c = str(input("cor da linha:  "))
d = str(input("cor do preenchimento:  "))
taruga = turtle.Turtle()
ws = turtle.Screen()
#window_size 

#aqui fizemos o preenchido
taruga.fillcolor(d)
taruga.begin_fill()
taruga.forward(a)
taruga.right(90)
taruga.forward(b)
taruga.right(90)
taruga.forward(a)
taruga.right(90)
taruga.forward(b)
taruga.right(90)
taruga.end_fill()

#aqui fizemos as bordas
taruga.color(c)
taruga.forward(a)
taruga.right(90)
taruga.forward(b)
taruga.right(90)
taruga.forward(a)
taruga.right(90)
taruga.forward(b)


turtle.done()