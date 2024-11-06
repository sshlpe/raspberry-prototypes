#example basic use for oled display

from machine import Pin, SoftI2C
import ssd1306

# Configuración de los pines I2C
i2c = SoftI2C(scl=Pin(7), sda=Pin(6))

# Inicialización de la pantalla OLED
oled_width = 64
oled_height = 48
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Limpiar la pantalla antes de escribir
oled.fill(0)
oled.show()

# Escribir texto en ∂la pantalla con menos caracteres por línea
oled.text('12:30', 10, 20)

# Actualizar la pantalla para mostrar el texto
oled.show()