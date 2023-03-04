import pywhatkit
import pandas as pd
import time
# Definir lista de contactos
df = pd.read_excel('personas.xlsx')
personas = df.values
minutes = 00
hour= 17
image = "Image_broadcast.jpeg"

# Enviar el mismo mensaje a cada contacto en la lista
for persona in personas:
    number = '+' + str(persona[3])
    message = f"""Hola {persona[0]}, ¿Como estas?

Este es un mensaje automatizado que te estoy enviando desde python, y tomando la lista desde un excel"""

    pywhatkit.sendwhats_image(number,image,message,10,True,2)
    time.sleep(2)
