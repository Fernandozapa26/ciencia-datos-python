
# Ciencia de Datos con Python - Semana 1

## Descripción
Proyecto académico desarrollado para la asignatura Ciencia de Datos del programa de Análisis y Desarrollo de Software (ADSO) del SENA.

## Objetivo
Comprender los conceptos fundamentales de ciencia de datos, el uso responsable de la información y la configuración de un ambiente de trabajo reproducible con Python.

## Tecnologías utilizadas
- Python 3.12
- Visual Studio Code
- Pandas
- NumPy
- Jupyter Notebook
- OpenPyXL
- Faker

## Estructura del proyecto
- data/raw: almacenamiento de datos originales.
- data/processed: almacenamiento de datos procesados.
- notebooks: cuadernos de análisis y ejercicios.
- outputs: resultados y reportes.
- docs: documentación del proyecto.
- scripts: archivos de código Python reutilizables.
- requirements.txt: dependencias necesarias.

## Instalación
1. Crear el entorno virtual: python -m venv .venv
2. Activar el entorno: .venv\Scripts\Activate.ps1
3. Instalar las dependencias: pip install -r requirements.txt

## Buenas prácticas
1. No modificar directamente los datos originales.
2. Documentar los procedimientos realizados.
3. Proteger la información personal.
4. Utilizar rutas relativas.
5. Mantener el código organizado y comentado.

## Autor
Fernando José Zapa Portillo

Programa: Análisis y Desarrollo de Software - SENA.



## Ejecución del proyecto

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Activar el entorno virtual de Python.
3. Abrir el archivo notebooks/semana_01_contexto_ambiente.ipynb.
4. Seleccionar el intérprete de Python del entorno .venv.
5. Ejecutar las celdas del notebook.
6. Verificar que se muestren las versiones de Python, Pandas y NumPy y que se compruebe la estructura de carpetas.

## Evidencias de aprendizaje

La documentación de las actividades de la Semana 1 se encuentra en la carpeta docs.

Incluye:
- Diagnóstico de conocimientos previos.
- Matriz dato-información-decisión.
- Mapa conceptual.
- Ciclo de vida del dato.
- Caso integrador y preguntas analíticas.
- Reflexión ética y bitácora de aprendizaje.
- Capturas del ambiente de desarrollo.






## Semana 3 - Perfilamiento y calidad de datos

Durante la tercera semana se desarrolló un laboratorio práctico
de perfilamiento, limpieza y validación de datos utilizando
Python y Pandas.

### Actividades realizadas

- Carga y exploración de archivos CSV.
- Identificación de valores faltantes.
- Detección y tratamiento de duplicados exactos.
- Identificación de documentos repetidos.
- Conversión segura de tipos de datos.
- Normalización de categorías.
- Aplicación de reglas de calidad.
- Tratamiento justificado de datos inválidos.
- Exportación y verificación de resultados.
- Documentación de decisiones de limpieza.

### Resultados obtenidos

- Registros originales: 20.
- Duplicados exactos retirados: 1.
- Registros preparados: 19.
- Registros con incidencias: 7.
- Incidencias detectadas: 10.

### Archivos principales

- `notebooks/semana_03_calidad_datos.ipynb`
- `data/raw/seguimiento_academico_semana3_con_errores.csv`
- `data/processed/seguimiento_academico_semana3_preparado.csv`
- `outputs/reporte_incidencias_semana3.csv`
- `outputs/duplicados_exactos_retirados.csv`
- `docs/Ciencia_de_Datos_Semana_3_CON_EVIDENCIAS.docx`

### Conclusión

Se aplicaron técnicas de perfilamiento y calidad de datos,
conservando la trazabilidad de las transformaciones.

El conjunto preparado todavía contiene anomalías que requieren
verificación antes de utilizarse en un sistema real.

## Semana 5 · Transformación y cierre del bloque 1

El [informe de cierre](docs/Semana_5_Cierre_Bloque_1.md) reúne el diccionario, los resultados, el cuestionario y la sustentación. El caso usa datos ficticios y conserva la fuente preparada de Semana 3.

- Abra `notebooks/Laboratorio_Semana_05_Transformacion_Cierre_Bloque1.ipynb` y ejecute todas las celdas desde la raíz del proyecto o desde `notebooks`. El laboratorio exporta el CSV transformado, los indicadores y la bitácora.
- Ejecute `python -m app.reto_semana5` desde la raíz para reproducir el reto y comparar el filtro S4-01 con el CSV versionado.
- Ejecute `python -m app.analisis` para volver a generar los dos CSV usados por la integración con MongoDB.
- Consulte el [registro de ejecución](evidencias/semana_05/ejecucion.txt). Esta revisión se ejecutó con Python 3.12.14, Pandas 2.2.3 y NumPy 2.3.5, en un entorno ya disponible. La instalación limpia desde `requirements.txt` queda por comprobar.
