import turtle
import math

def desenha_quadrado(tart, lado):
    for _ in range(4):
        tart.forward(lado)
        tart.right(90)
    
def desenha_retangulo(tart, lado1, lado2):
    for _ in range(2):
        tart.forward(lado1)
        tart.right(90)
        tart.forward(lado2)
        tart.right(90)
        
def desenha_triangulo_isoceles(tart, base, lado):
    # cosseno(alfa) = cateto_oposto / hipotenusa
    angulo_base = math.degrees(math.acos(base/2 / lado))
    angulo_topo = 180 - 2*angulo_base
    
    tart.forward(base)
    tart.left(180 - angulo_base)
    tart.forward(lado)
    tart.left(180 - angulo_topo)
    tart.forward(lado)
    tart.left(180 - angulo_base)

def desenha_corpo(tart, x):
    tart.fillcolor('LightBlue')
    tart.begin_fill()
    desenha_retangulo(tart, 2*x, x)
    tart.end_fill()

def desenha_porta(tart, x):
    tart.right(90)
    tart.forward(x)
    tart.left(90)
    tart.forward(x/3)
    tart.left(90)
    desenha_retangulo(tart, 2*x/3, x/3)

def desenha_janelas(tart, x):
    tart.up()
    tart.right(90)
    tart.forward(2*x/3)
    tart.left(90)
    tart.forward(x/3)
    tart.down() 
    desenha_quadrado(tart, x/3)
    
    tart.up()
    tart.right(90)
    tart.forward(x/3 + x/6)
    tart.left(90)
    tart.down()
    desenha_quadrado(tart, x/3)
        
def desenha_telhado(tart, x):
    tart.up()
    tart.forward(2*x/3)
    tart.left(90)
    tart.forward(x + 2*x/3)
    tart.right(180)
    tart.down()
    
    tart.fillcolor('Brown')
    tart.begin_fill()
    desenha_triangulo_isoceles(tart, 2*x + x/3, x*math.sqrt(2))
    tart.end_fill()

# -------------------------------------------

construtor = turtle.Turtle()
vx = 100
desenha_corpo(construtor, vx)
desenha_porta(construtor, vx)
desenha_janelas(construtor, vx)
desenha_telhado(construtor, vx)
