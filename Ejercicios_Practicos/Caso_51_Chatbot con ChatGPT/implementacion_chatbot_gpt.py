# -*- coding: utf-8 -*-
"""Implementacion_ChatBot_GPT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cxyzx9nJSXIp0s569kUwnpYxh8iYR7wW

# Caso Práctico: Implementación de un ChatBot con GPT

<div style="background-color:#D9EEFF;color:black;padding:2%;">
<h2>Enunciado del caso práctico</h2>

En este caso práctico, se propone al alumno el desarrollo de un ChatBot que permita interactuar con los clientes de un restaturante y recopilar los pedidos de comida que realicen para entregar a domiciolio o recoger en las instalaciones.

Para ello, el alumno debe implementar un progorama en Python que acceda de manera programática a los servicios de OpenAI y permita interactuar con uno de los LLMs que ofrecen.

</div>

# Resolución del caso práctico

## 0. Instalación de librerías externas
"""

!pip install openai==0.28

"""## 1. Lectura de la API Key"""

import openai

with open("/content/drive/MyDrive/api-keys/secret-key.txt") as f:
  openai.api_key = f.readline()

"""## 2. Selección del modelo

En la función `obtener_completion` que habíamos implementado para casos prácticos anteriores, únicamente hacíamos uso del `role` de `user`:

```python
def obtener_completion(prompt, model="gpt-3.5-turbo"):
  mensaje = [{"role": "user", "content": prompt}]
  respuesta = openai.ChatCompletion.create(
      model=model,
      messages=mensaje,
      temperature=0, # Este hiperparámetro controla la aleatoriedad del modelo
  )
  return respuesta.choices[0].message["content"]
```

En este caso práctico, vamos a tener que explorar el [resto de roles que nos proporcionar OpenAI](https://platform.openai.com/docs/guides/gpt/chat-completions-api) para sus LLMs y la función que tienen cada uno de ellos:


*  Rol `user`: Representa al usuario final que interactúa con el LLM a través de un chat.
*  Rol `assistant`: Representa al LLM que estemos utilizando, en este caso, `gpt-3.5-turbo`.
*  Rol `system`: Este rol representa al desarrollador de sistema. Permite proporcionar instrucciones "root" al LLM para que se sigan durante la conversación con el usuario.
"""

def obtener_completion(mensajes, model="gpt-3.5-turbo"):
  respuesta = openai.ChatCompletion.create(
      model=model,
      messages=mensajes,
      temperature=0, # Este hiperparámetro controla la aleatoriedad del modelo
  )
  return respuesta.choices[0].message["content"]

"""## 3. Predicción/Generación de texto"""

mensajes = [
    {'role': 'system', 'content':'Eres un ChatBot amigable con un conocimiento experto sobre Ciberseguridad. Responde detalladamente a las preguntas de los usuarios'},
    {'role': 'user', 'content':'Buenos días. Acabo de recibir un SMS sospechoso. ¿Crees que puede ser phishing?. El SMS es: "Estimado cliente, su paquete no se ha podido entregar el 02/09 porque no se han pagado las tasas de aduanas (? 1). siga las instrucciones: http:/67m.us/9OYpR'}
]
respuesta = obtener_completion(mensajes)
print(respuesta)

"""Si intentamos continuar una conversación manteniendo este esquema de preguntas/respuestas, nos daremos cuenta de que el LLM no preserva el contexto"""

mensajes = [
    {'role': 'system', 'content':'Eres un ChatBot amigable. Responde a las preguntas de los usuarios.'},
    {'role': 'user', 'content':'Buenos días. Me llamo Santiago.'}
]
respuesta = obtener_completion(mensajes)
print(respuesta)

mensajes = [
    {'role': 'system', 'content':'Eres un ChatBot amigable. Responde a las preguntas de los usuarios.'},
    {'role': 'user', 'content':'¿Podrías decirme de dónde proviene mi nombre?'}
]
respuesta = obtener_completion(mensajes)
print(respuesta)

"""## 4. Predicción/Generación de texto preservando el contexto

Para preservar el contexto de la conversación, necesitamos almacenar las interacciones con el LLM en la lista de mensajes y proporcionárselo en las nuevas interacciones.
"""

mensajes = [
    {'role': 'system', 'content':'Eres un ChatBot amigable. Responde a las preguntas de los usuarios.'},
    {'role': 'user', 'content':'Buenos días. Me llamo Santiago.'},
    {'role': 'assistant', 'content':'¡Buenos días, Santiago! ¿En qué puedo ayudarte hoy?'},
    {'role': 'user', 'content': '¿Podrías decirme de dónde proviene mi nombre?'}
]
respuesta = obtener_completion(mensajes)
print(respuesta)

"""## 5. Implementación de un ChatBot interactivo"""

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = obtener_completion(context)
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, styles={'background-color': '#F6F6F6'})))
    return pn.Column(*panels)

def end_chat(event):
    panels.append(pn.pane.Alert("Chat terminado por el usuario.", alert_type='success'))
    # Solicito al LLM que me genere un JSON con toda la conversación
    context.append({'role': 'system', 'content':"""Genera un resumen del pedido en formato JSON. La salida debe ser únicamente el JSON sin nada más. \
  El JSON debe incluir las siguientes claves:
  "pizzas": <lista de pizzas solicitadas>
  "tamaño_pizzas": <tamaño de las pizzas solicitadas>
  "precios_pizzas"> <precios de las pizzas solicitadas>
  "ingredientes_extras": <lista de ingredientes extra solicitados>
  "tamaño_extras": <tamaño de los ingredientes extra seleccionados>
  "precios_extras": <precios de los ingredientes extra solicitados>
  "bebidas": <lista de bebidas solicitadas>
  "precios_bebidas": <precios de las bebidas solicitadas>
  "direccion_entrega", <En el caso de entrega a domicilio, direccion de entrega, en caso contrario, pones NA>"""})
    pedido_json = obtener_completion(context)
    print(f"\nEl pedido realizado es:\n{pedido_json}")

import panel as pn  # GUI
pn.extension()

panels = []

context = [ {'role':'system', 'content':"""
Eres un OrderBot, un servicio automatizado para recopilar pedidos para un restaurante de pizza. \
Primero saludas al cliente, luego recopilas el pedido, \
y luego preguntas si es para recoger o entregar. \
Esperas a recopilar todo el pedido, luego lo resumes y verificas una última vez \
si el cliente quiere agregar algo más. \
Si es para entrega, preguntas por una dirección. \
Finalmente, recopilas el pago. \
Asegúrate de aclarar todas las opciones, extras y tamaños para identificar de manera única \
el artículo del menú. \
Respondes de manera corta, muy amigable y conversacional. \
El menú incluye los siguientes productos al siguiente precio en euros:
pizza de pepperoni 12.95, 10.00, 7.00
pizza de queso 10.95, 9.25, 6.50
pizza de berenjena 11.95, 9.75, 6.75
papas fritas 4.50, 3.50
ensalada griega 7.25
Ingredientes extra:
queso 2.00
champiñones 1.50
salchicha 3.00
tocino canadiense 3.50
salsa AI 1.50
pimientos 1.00
Bebidas:
coca-cola 3.00, 2.00, 1.00
sprite 3.00, 2.00, 1.00
agua embotellada 5.00
"""} ]


inp = pn.widgets.TextInput(value="Hola", placeholder='Introduce texto aqui...')
button_conversation = pn.widgets.Button(name="Chat!")
button_end_chat = pn.widgets.Button(name="Terminar Chat")

button_end_chat.on_click(end_chat)

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation, button_end_chat),
    pn.panel(interactive_conversation, loading_indicator=True, sizing_mode="stretch_both"),
)

dashboard

