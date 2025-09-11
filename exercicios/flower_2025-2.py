#do the imports first
import math
import turtle

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """    
    for i in range(n):
        t.forward(int(length))
        t.left(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1 
    step_length = arc_length / n 
    step_angle = float(angle) / n 
    polyline(t, n, step_length, step_angle)

def leaf(t):
    arc(t, 80, 90)
    t.left(90)
    arc(t, 80, 90)
    
def flower(t, n_leaves):
    for i in range(n_leaves):
        leaf(t)
        t.left(int(360/n_leaves))

if __name__ == '__main__':
    # This block only executes when the script is run directly.
    # It will not execute if the script is imported as a module into another script.
    #main()
    jn = turtle.Screen()      # Abre uma janela onde as tartarugas vão caminhar

    tarta = turtle.Turtle()
    tarta.speed(50)
    
    flower(tarta, 8)

    jn.mainloop()             # Espera o usuário fechar a janela