import time
from Button import ButtonClass

def personal_function():
    print("funcion personal")
    
def personal_function2():
    print("funcion personal2")

# Crear instancias de botones
button2 = ButtonClass(15, personal_function2)
button1 = ButtonClass(14, personal_function)


# Mantener el programa en ejecución
while True:
    time.sleep(1)