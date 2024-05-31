import turtle 
t = turtle.Turtle() 
s = int(input("Enter the length of the side of the square: ")) 
col = input("Enter the color name or hex value of color(# RRGGBB): ") 
t.fillcolor(col) 
t.begin_fill() 
for _ in range(4): 
  t.forward(s) 
  t.right(90) 
t.end_fill()