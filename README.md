Análisis de Datos Sintéticos de un Reactor Químico

Descripción:
El proyecto consiste en un pipeline de procesamiento de datos científicos para un reactor químico simulado. El sistema genera un dataset sintético con mediciones de Temperatura (°C) y Presión (psi), calcula estadísticas descriptivas, elimina valores atípicos (outliers) mediante el método estadístico de 3 sigmas, y finalmente exporta los datos limpios junto con una visualización comparativa.

El pipeline sigue las siguientes etepas de secuencia:
-Generación doonde el generador.py crea el archivo de los datos del reactor con 5000 muestras y un 2% de outliers artificiales.
-Carga el script en data_carga.py lee el archivo CSV utilizando librerias Pandas, aplicando un manejo grande de errores.
-Estadísticas: El script estadisticas.py calcula la media, la desviación estándar, el máximo y el mínimo para cada columna numérica.
-El script filtrado.py aplica la regla de 3 sigmas usando NumPy, descartando cualquier fila cuyo valor se encuentre fuera del rango permitido.
-El script Grupo1/exportacion.py guarda el DataFrame purificado en el archivo datos_limpios_final.csv
-Visualización: El script Grupo1/visualizacion.py genera el archivo de imagen comparativa_reactor.png, el cual contiene dos gráficas superpuestas para analizar las señales de temperatura y presión.

¿Qué fue utilizado?
-NumPy (1.21+)
-Pandas (1.3+)
-Matplotlib (3.4+)
-csv (stdlib)
-os (stdlib)
-Python

Aspectos técnicos destacados: 
-El sistema garantiza que el dataset sintético sea idéntico en cada ejecución mediante el uso de una semilla fija (np.random.seed(42)), lo que permite comparar resultados de manera consistente.
-El motor de filtrado opera directamente sobre matrices completas sin utilizar bucles de Python explícitos, maximizando la velocidad gracias a NumPy. 
