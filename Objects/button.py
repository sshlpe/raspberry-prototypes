from machine import Pin
import time

class Button:
    def __init__(self, pin_number, callback):
        self.button = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        self.last_press_time = 0
        self.callback = callback
        self.button.irq(trigger=Pin.IRQ_FALLING, handler=self.button_handler)
    
    def debounce(self):
        current_time = time.ticks_ms()
        if time.ticks_diff(current_time, self.last_press_time) > 200:
            self.last_press_time = current_time
            return True
        return False
    
    def button_handler(self, pin):
        if self.debounce():
            self.callback()