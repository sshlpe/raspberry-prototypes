from oled import OledDisplay
from button import Button
import time

# Inicializar la pantalla OLED
oled_display = OledDisplay(64, 48, 6, 7)

# Posición inicial del pixel
x = 10
y = 10
velx = 1
vely = 0

def move_up_right():
    global vely, velx
    if velx != 0:  # Si se mueve en el eje x
        velx = 0
        vely = -1  # Cambia dirección hacia arriba
    else:  # Si se mueve en el eje y
        velx = 1
        vely = 0  # Cambia dirección hacia la derecha

def move_down_left():
    global vely, velx
    if velx != 0:  # Si se mueve en el eje x
        velx = 0
        vely = 1  # Cambia dirección hacia abajo
    else:  # Si se mueve en el eje y
        velx = -1
        vely = 0  # Cambia dirección hacia la izquierda

# Crear instancias de botones con sus respectivas funciones de callback
button_up_right = Button(15, move_up_right)
button_down_left = Button(14, move_down_left)

# Bucle principal
while True:
    x += velx
    y += vely
    
    # Mantener la serpiente dentro de los límites de la pantalla
    if x >= oled_display.width:
        x = 0
    elif x < 0:
        x = oled_display.width - 1
    
    if y >= oled_display.height:
        y = 0
    elif y < 0:
        y = oled_display.height - 1

    oled_display.clear()
    oled_display.draw_pixel(x, y)
    oled_display.show()
    time.sleep(0.05)
