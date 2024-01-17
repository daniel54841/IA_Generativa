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
Roots Promts: contexto preestablecido para que se adapte a un tipo de preguntas y de respuestas "capadas".
Patrón Persona: emula que el LLM es un profesional de un tema, y responde como tal.
Chain of Thought: emitir una respuesta paso a paso.
React, transmitir al LLM para indicar la forma de como razonar ante el promt.
	Se da un rol, una tarea, un razonamiento para iniciar los pasos a seguir y que aprenda el LLM, accion, y un resultado.
Ejemplo de Prompt:
	----- Prompt 1 -----

Actúa como si fueses un experto en Ciberseguridad.

Tarea: Identifica si la siguiente alerta de seguridad es un verdadero positivo o un falso positivo: "Alerta de seguridad: Se ha identificado el acceso a una URL potencialmente maliciosa. La URL identificada es: https://clientes.empresa1.com"
Razonamiento: Voy a comenzar evaluando la URL de la alerta para identificar posibles elementos sospechosos desde el punto de vista de la Ciberseguridad.
Acción: Analizo la URL que aparece en la alerta.
Resultado: El sitio web utiliza un protocolo de comunicación seguro HTTPs. El sitio web tiene un nombre de dominio. El nombre de dominio parece de una entidad fiable.
Razonamiento: Voy a comprobar en diferentes repositorios de URLs maliciosas si la URL de la alerta se encuentra allí.
Acción: Consulto https://www.urlvoid.com/scan/clientes.empresa1.com
Resultado: URLVoid indica que la URL no es maliciosa
Razonamiento: La URL no parece maliciosa. La alerta se corresponde con un falso positivo.

Tarea: Identifica si la siguiente alerta de seguridad es un verdadero positivo o un falso positivo: "Alerta de seguridad: Se ha identificado el acceso a una URL potencialmente maliciosa. La URL identificada es: https://udemy.com"


----- Prompt 2 -----

Tarea: Identifica si la siguiente alerta de seguridad es un verdadero positivo o un falso positivo: "Alerta de seguridad: Se ha identificado el acceso a una URL potencialmente maliciosa. La URL identificada es: http://15.30.12.134/programa.exe"


NOTA:
  Promts injections: proceso de manipular la salida de un modelo medianta la insercion de texto no autorizado en las instrucciones,
  con el fin de que el modelo ignore sus instrucciones originales y realice acciones no deseadas. Puede provocar acceso no autorizado,
  ,violaciones de datos o manipulacion de las respuestas del modelo ademas de permitir hacer que el modelo genere cualquier contenido de su eleccion, a
  menudo con intenciones maliciosas.  
La mayoria de LLMs públicos tienen incorporadas ciertas restricciones que limitan su comportamiento.
  Hay dos tipos:
	Directos, ocurre cuando el atacante manipula directamente el promt para obtener el resultado deseado de la IA. Por ejemplo, si un atacante conoce
	la estructura de una aplicacio, puede crear un promt "malicioso" que engañe a la IA para generar una respuesta dañina.
	En un contexto mas amplio, el potencial de estos ataques, crece a medida que los LLMs se integran en diversas aplicaciones, teniendo que conocer
        estas vulnerabilidades y salvaguardar los sistemas y a los usuarios.
	Indirectos, ocurre cuando el atacante no manipula directamente el prompt, sino que explota el comportamiento del modelo proporcionando entradas
	que hacen que el modelo ignore sus instrucciones anteriores aprovechando fuentes de datos externas para lograr el resultado deseado.
GPT-4:
	GPT: modelar un "chatGPT" personalizado, compartir con otros usuarios. Tienen las caracteristicas de ChatGPT en los aspectos de seguridad.
	En caso de usar una API de terceros, se eligirá si los datos se pueden enviar a esa API. Al construir el GPT se podrá elegir si los datos se pueden enviar
	para mejorar y entrenar el modelo, basandose en los controles de privacidad que tienen los usuarios.
	Se podrá definir acciones personalizadas poniendo una o más APIs, pudiendo integrar datos externos o interactuar con el mundo real, conectando a base de datos
	, conectando a correos electronicos o siendo un asistente de compras.
Solo en GPT-4
NOTA: Se va a poner el codigo, aportado en el curso, pero no se va a poder ejecutar ni usar la API Key debido a que no se va a usar la parte premium.
	
Redes Neuronales Recurrentes: precursora de los LLMs.Son un tipo de arquitectura diseñada para trabajar con datos secuenciales o datos que tienen una relacion temporal.
Presentan conexiones recurrentes, con salidas que retroalimentan entradas futuras, permitiendo el manejo de datos secuenciales y la captura de dependencias temporales.
Tienen memoria interna, que captura patrones en secuencias largas, permitiendo que se pueda generar nuevas secuencias que sigan estructuras similares a las que se han 
sido entrenadas.
Manejan secuencias de entrada y salida de longitud variable.
Las arquitecturas avanzadas de RRNNs son las LSTM( Long Short-Term Memory) y las GRU( Gated Recurrent Unit)
