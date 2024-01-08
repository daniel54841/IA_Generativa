# IA_Generativa(Notas)
Inteligencia Artificial Generativa: sistema que es capaz de generar contenido que imita o se aproxima a la habilidad humana.
   Se forma de un subconjunto de tecnicas de Machine Learning, concretamente al Deep Learning y se entrenan con varios millones
   de modulos neuronales.
Ejemplos de tecnicas de IAG:
	GANs
	VAEs
	DMs
	LLMs
LLMs:(Large Language Models) algoritmos  de procesamiento de lenguaje natural que genera texto coherente y contextualmente
 relevante. Tiene una arquitectura con muchos parametros. Existen LLMs de proposito general que pueden adaptarse para mejorar
 en usos concretos.
Funcionamiento de LLMs:
	- Promt, contexto que se le proporciona al LLM para que genere la respuesta usando la información proporcionada.
	- Completion, respuesta generada usando el contexto proporcionado.
 Inferencia: proceso de generación de la información.

Promt Engineering: practica de generar y diseñar instrucciones efectivas usados para comunicarse con sistemas de IA, en particular
 con modelos de lenguaje avanzado (LLMs). Es un proceso uteratuvo. Es muy improbable encontrar un promt adecuado en un primer intento.
	(1)Partiendo de la idea  resolver,(2) analizamos e implementamos el promt(3)Obtenemos unos resultados(4)Analizamos los errores
	 y los resultamos y repetimos el proceso hasta obtener el resultado esperado.
 Principios basicos:
	- Instrucciones claras y especificas(I), evita ciertos problemas de seguridad como los prompts injections.
		Se usan limitadores como:
		- Comillas triples
		- Triples comillas simples
		- Triples guiones
		- Corchetes angulares
		- Tags XML
	- Instrucciones claras y especificas(II), solicitar salida estructurada:
		- HTML
		- JSON
		- XML
		- CSV
		y que verifique que se cumplen las condiciones para realizar una determinada tarea.
	
	- Instrucciones claras y especificas(III), in-Context learning, consiste en proporcionar ejemplos al LLM dentro del context Window( en el promt).
		Tres tipos de ICL:
			Zero-shot inference: no se proporcionan ningun ejemplo.
			One-shot inference: se proporcionan un único ejemplo.
			Few-shot inference: se proporcionan multiples ejemplos.
		Los usos depende del tipo de LLM y su proceso de entrenamiento.
	- Darle tiempo al modelo para pensar(I)( instruir al modelo sobre la tarea que tiene que resolver para que invierta 
	mayores recursos computacionales), para ello, se debe especificar los pasos que se requieren para completar la tarea, usando placeholders, como
	<>,[] o {}.
	- Darle tiempo al modelo para pensar(II), instruir al modelo para que trabaje en su propia solucion antes de llegar a la conclusion.

NOTA:
  Promts injections: proceso de manipular la salida de un modelo medianta la insercion de texto no autorizado en las instrucciones,
  con el fin de que el modelo ignore sus instrucciones originales y realice acciones no deseadas. Puede provocar acceso no autorizado,
  ,violaciones de datos o manipulacion de las respuestas del modelo ademas de permitir hacer que el modelo genere cualquier contenido de su eleccion, a        	menudo con intenciones maliciosas.  
La mayoria de LLMs públicos tienen incorporadas ciertas restricciones que limitan su comportamiento.
  Hay dos tipos:
	Directos, ocurre cuando el atacante manipula directamente el promt para obtener el resultado deseado de la IA. Por ejemplo, si un atacante conoce
	la estructura de una aplicacio, puede crear un promt "malicioso" que engañe a la IA para generar una respuesta dañina.
	En un contexto mas amplio, el potencial de estos ataques, crece a medida que los LLMs se integran en diversas aplicaciones, teniendo que conocer
        estas vulnerabilidades y salvaguardar los sistemas y a los usuarios.
	Indirectos, ocurre cuando el atacante no manipula directamente el prompt, sino que explota el comportamiento del modelo proporcionando entradas 	que hacen que el modelo ignore sus instrucciones anteriores aprovechando fuentes de datos externas para lograr el resultado deseado.
