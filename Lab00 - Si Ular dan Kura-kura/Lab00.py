import turtle 
  
turtle.shape("turtle") 
turtle.penup() 
turtle.goto(-100,0)
 
# Membuat huruf C dengan warna biru
turtle.pendown() 
turtle.color("blue")
turtle.begin_fill() 

turtle.forward(100) 
turtle.left(90) 
turtle.forward(25) 
turtle.left(90) 
turtle.forward(80) 
turtle.right(90) 
turtle.forward(50) 
turtle.right(90) 
turtle.forward(80) 
turtle.left(90) 
turtle.forward(25) 
turtle.left(90) 
turtle.forward(100) 
turtle.left(90) 
turtle.forward(100)

turtle.end_fill() 
  
# Memindahkan koordinat posisi turtle 
turtle.penup() 
turtle.left(90) 
turtle.forward(130) 
  
# membuat huruf S dengan warna merah
turtle.pendown() 
turtle.color("red")
turtle.begin_fill() 

turtle.forward(100) 
turtle.left(90) 
turtle.forward(60) 
turtle.left(90) 
turtle.forward(80) 
turtle.right(90) 
turtle.forward(20) 
turtle.right(90) 
turtle.forward(80) 
turtle.left(90) 
turtle.forward(20) 
turtle.left(90) 
turtle.forward(100) 
turtle.left(90) 
turtle.forward(60) 
turtle.left(90) 
turtle.forward(80) 
turtle.right(90) 
turtle.forward(20) 
turtle.right(90) 
turtle.forward(80) 
turtle.left(90) 
turtle.forward(20) 

turtle.end_fill() 
 
# Menyembunyikan ikon turtle dan menutup window saat diclick
turtle.hideturtle() 
turtle.exitonclick()
