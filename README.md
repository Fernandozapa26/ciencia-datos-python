# Ciencia de Datos con Python - Proyecto Integrador SENA
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






## Semana 6 - Agrupación, estadísticas e indicadores KPI

Durante la Semana 6 se desarrolló un laboratorio de análisis estadístico utilizando Python y Pandas, dando continuidad a los datos académicos ficticios procesados durante la Semana 5.

### Objetivo

Aplicar técnicas de agrupación, agregación y análisis estadístico para obtener indicadores que permitan describir el comportamiento de los registros académicos, conservando la calidad, trazabilidad y limitaciones de los datos.

### Actividades realizadas

- Carga y validación del archivo procesado de la Semana 5.
- Selección de registros aptos para el análisis.
- Agrupación de datos mediante `groupby()`.
- Cálculo de estadísticas utilizando `agg()`.
- Análisis de frecuencias y porcentajes con `value_counts()`.
- Construcción de tablas cruzadas con `crosstab()`.
- Elaboración de tablas dinámicas mediante `pivot_table()`.
- Cálculo de media, mediana, desviación estándar y rango.
- Construcción y validación de indicadores KPI.
- Desarrollo de los cuatro retos autónomos.
- Exportación de resultados en formato CSV.

### Resultados obtenidos

| Indicador | Resultado |
|---|---:|
| Registros originales | 19 |
| Registros aptos | 11 |
| Registros excluidos | 8 |
| Cobertura analítica | 57,89 % |
| Media general de notas | 3,991 |
| Mediana general | 4,100 |
| Desviación estándar muestral | 0,664 |
| Participación de prioridad alta | 18,18 % |
| Registros con asistencia ≥ 80 % | 81,82 % |

Los resultados corresponden únicamente a registros ficticios y se utilizan con fines académicos.

### Retos autónomos

**Reto A:** Agrupación de registros por ciudad para calcular cantidad, media y mediana.

**Reto B:** Construcción de una tabla cruzada entre ciudad y prioridad de revisión, incluyendo porcentajes por ciudad.

**Reto C:** Creación de un KPI adicional para calcular la proporción de registros aptos con asistencia igual o superior al 80 %.

**Reto D:** Comparación de media y mediana entre los programas ADSO y Ciencia de Datos con Python, considerando las limitaciones de las muestras.

### Archivos generados

**Notebook:**

`notebooks/Laboratorio_Semana_06_Agrupacion_KPI_Pandas (1).ipynb`

**Resultados exportados:**

- `outputs/semana6_agrupacion_programa.csv`
- `outputs/semana6_crosstab.csv`
- `outputs/semana6_tabla_dinamica.csv`
- `outputs/semana6_kpis.csv`
- `outputs/semana6_reto_c_kpi_asistencia.csv`

### Metodología y limitaciones

El análisis utilizó los 11 registros que cumplieron los criterios de calidad establecidos. Se conservaron las categorías de información faltante y se evitaron modificaciones al archivo original.

La fecha de corte utilizada fue el 18 de octubre de 2026.

Los umbrales de calificación y asistencia son supuestos didácticos y no corresponden a criterios oficiales del SENA.

Las diferencias estadísticas identificadas no permiten establecer relaciones causales ni tomar decisiones individuales sobre los aprendices.

### Conclusión

La Semana 6 permitió fortalecer las habilidades de análisis de datos mediante el uso de herramientas estadísticas de Pandas. Se comprobó la importancia de validar los registros, definir correctamente los denominadores y documentar las limitaciones de los indicadores antes de interpretar sus resultados.