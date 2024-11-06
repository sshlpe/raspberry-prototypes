from machine import SoftI2C, Pin
import ssd1306
import time

class OledDisplay:
    def __init__(self, width, height, sda_pin, scl_pin):
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        self.oled = ssd1306.SSD1306_I2C(width, height, self.i2c)
        self.width = width
        self.height = height
    
    def clear(self):
        self.oled.fill(0)
        
    def show(self):
        self.oled.show()
    
    def draw_pixel(self, x, y):
        self.oled.pixel(x, y, 1)
    
    def scroll(self, dx, dy):
        self.oled.scroll(dx, dy)
    
    def text(self, string, x, y):
        self.oled.text(string, x, y)
    
    def line(self, x1, y1, x2, y2):
        self.oled.framebuf.line(x1, y1, x2, y2, 1)
    
    def vline(self, x, y, h):
        self.oled.framebuf.vline(x, y, h, 1)
    
    def hline(self, x, y, w):
        self.oled.framebuf.hline(x, y, w, 1)
    
    def rect(self, x, y, w, h, f=False):
        self.oled.framebuf.rect(x, y, w, h, 1, f)
    
    def ellipse(self, x, y, xr, yr, f=False, Q=[]):
        if Q:
            bits = {
                "q1": 0b0001,  # Cuadrante superior derecho
                "q2": 0b0010,  # Cuadrante superior izquierdo
                "q3": 0b0100,  # Cuadrante inferior izquierdo
                "q4": 0b1000   # Cuadrante inferior derecho
            }
            q = 0
            for qn in Q:
                q |= bits[qn]
                
            self.oled.framebuf.ellipse(x, y, xr, yr, 1, f, q)
        else:
            self.oled.framebuf.ellipse(x, y, xr, yr, 1, f)
    
    def draw_sprite(self, sprite, x, y):
        for row in range(len(sprite)):
            for col in range(len(sprite[row])):
                if sprite[row][col] == 1:
                    self.draw_pixel(x+col, y+row)
        
        
#oled_display = OledDisplay(64, 48, 6, 7)


