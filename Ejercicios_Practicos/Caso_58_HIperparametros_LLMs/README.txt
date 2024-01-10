Parametros: 
	Temperatura: controla la aleatoriedad de las respuestas generada. Cuanto más baja sea, hace que las respuestas seahn más coherentes y predecibles
	mientras que una temperatura más alta, hace que la respuesta sea más creativa y diversa, pero menos precisa.
	Top_p: se establece entre un rango entre 0 y 1, representando una fracción acumulativa de probabilidad. Permitirá al modelo calcular las palabras
	más probables en funcion de ese valor y generar texto en funcion de esas palabras. 
	Frequency penalty: numero entre -2.0 y 2.0. Los valores positivos, penalizan nuevos tokens en funcion de la frecuencia en el texto hasta ese momento,
	disminuyendo la probabilidad del modelo de repetir la misma linea de manera identica.
	