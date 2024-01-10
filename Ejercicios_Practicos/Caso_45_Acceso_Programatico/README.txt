1. Instalacion de librerias externas
2. Incorporar la api key usando un archivo externo para evitar fugas de seguridad
3. Seleccionarr el modelo para que trabaje el LLM.
def obtener_completion(prompt, model="gpt-3.5-turbo"):
  mensaje = [{"role": "user", "content": prompt}]
  respuesta = openai.ChatCompletion.create(
      model=model,
      messages=mensaje,
      temperature=0, # Este hiperparámetro controla la aleatoriedad del modelo
  )
  return respuesta.choices[0].message["content"]
	- En el parametro de model, se tendrá que elegir el modelo que usara el LLM. 
	- promt, será una variable que se dará como valor la pregunta que se quiere proporcionar al LLM
	
