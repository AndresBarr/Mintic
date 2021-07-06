A= input() 
B= input() 
C= input()
A_float =float(A)
B_float =float(B)
C_float =float(C)

triangle=(A_float*C_float)/2
Circle= 3.14159*C_float*C_float
Trapezium=(A_float+B_float/2)*C_float
Square=B_float*B_float
Rectangle=A_float*B_float
print('TRIANGULO: {0:.3f}'.format(triangle))
print('CIRCULO: {0:.3f}'.format(Circle))
print('TRAPEZIO: {0:.3f}'.format(Trapezium))
print('QUADRADO: {0:.3f}'.format(Square))
print('RETANGULO: {0:.3f}'.format(Rectangle))