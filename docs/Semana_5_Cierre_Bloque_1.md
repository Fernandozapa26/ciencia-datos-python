# Semana 5 · Transformación de datos y cierre del bloque 1

**Proyecto académico de Fernando José Zapa Portillo · ADSO, SENA**

Este informe y la verificación de Semana 5 se prepararon con asistencia de Codex a partir del repositorio y del laboratorio del SENA. Corte didáctico del conjunto de datos: 18 de octubre de 2026.

## Preguntas y portafolio

¿Qué registros de seguimiento ficticio requieren verificación antes de construir indicadores? ¿Cuántas filas cuentan con las dos calificaciones y asistencia? ¿El filtro de asistencia baja de ADSO sigue seleccionando las mismas filas después de la transformación?

| Semana | Material para la sustentación |
| --- | --- |
| 1 | [Fundamentos y entorno](../notebooks/semana_01_contexto_ambiente.ipynb) y [entrega de Semana 1](Ciencia_de_Datos_Semana_1_RESUELTA.docx) |
| 2 | [Lectura e inspección de CSV y Excel](../notebooks/semana_02_estructuras_pandas.ipynb) |
| 3 | [Perfilamiento](../notebooks/semana_03_calidad_datos.ipynb) y [reporte de incidencias](../outputs/reporte_incidencias_semana3.csv) |
| 4 | [Laboratorio de filtros](../notebooks/Laboratorio_Semana_04_Seleccion_Filtrado_Pandas.ipynb) y consultas exportadas de [programas](../outputs/semana4_reto_consulta1_programas.csv), [notas](../outputs/semana4_reto_consulta2_notas.csv) y [operadores](../outputs/semana4_reto_consulta3_operadores.csv) |
| 5 | [Laboratorio](../notebooks/Laboratorio_Semana_05_Transformacion_Cierre_Bloque1.ipynb), [reto autónomo](../app/reto_semana5.py) y [registro de ejecución](../evidencias/semana_05/ejecucion.txt) |

## Diccionario de variables

| Campos | Significado y tratamiento |
| --- | --- |
| `fila_fuente`, `archivo_fuente` | Número de fila y archivo de origen. Permiten rastrear cada registro. |
| `documento`, `nombre`, `ficha` | Identificador ficticio, nombre de ejemplo y grupo. Los documentos repetidos se marcan para revisión. |
| `programa`, `ciudad` | Texto original. Las equivalencias verificadas se guardan en campos derivados. |
| `nota_python`, `nota_datos` | Calificaciones de 0 a 5. Un nulo indica un dato ausente. |
| `asistencia` | Porcentaje de 0 a 100. La brecha se expresa en puntos porcentuales. |
| `fecha_actualizacion`, `fecha_corte` | Fechas para controlar la vigencia de un registro. Las fechas ausentes y posteriores al corte se marcan. |
| `promedio_dos_notas` | Media aritmética de las dos notas. Queda vacía si falta una. |
| `ciudad_normalizada`, `ciudad_pendiente_revision` | Equivalencia conocida y marca para valores presentes sin correspondencia. |
| `prioridad_revision` | Primera condición aplicable según el orden de las reglas. Sirve para revisar registros sintéticos. |

## Resultados y sustentación

El laboratorio conservó las 19 filas, marcó dos registros con conflicto de identidad y detectó una actualización posterior al corte. Once de 19 registros cumplieron los requisitos del ejemplo analítico: documento presente, sin conflicto, fechas verificables y vigentes, dos notas y asistencia. Su promedio fue 3,99 sobre 5, a partir de 43,9 puntos acumulados en 11 registros. Para el reto de completitud se usaron las 19 filas y solo se exigieron las dos notas y la asistencia: 14 de 19, equivalentes a 73,68 %.

El reto normaliza Medellín, Bello, Itagüí y Envigado mediante equivalencias explícitas. `BELL0` queda pendiente y el campo vacío se conserva como dato ausente. `np.select()` evalúa en orden identidad contradictoria, ciudad sin equivalencia, datos incompletos y revisión didáctica. El laboratorio también controla corte y fechas no verificables. Al comparar con el CSV validado de Semana 4, S4-01 devuelve las filas fuente 5 y 9 antes y después de agregar columnas. Las validaciones comprobaron los identificadores de procedencia, el corte y la huella SHA-256 de la fuente después de exportar.

Los umbrales de 80 % y 3,5 son didácticos. Para el siguiente bloque conviene contrastar primero la identidad, las fechas y `BELL0` con la fuente autorizada. Una recomendación automática de acompañamiento basada en un documento conflictivo atribuiría datos dudosos a una persona sin verificación humana.

## Cuestionario 6.3

1. Seleccionar reduce las filas consultadas, como filtrar ADSO con asistencia inferior a 80 % en S4. Derivar agrega información por fila, como calcular la brecha de asistencia en S5.
2. `mean(axis=1)` puede omitir el nulo y devolver la única nota disponible como si representara ambas evaluaciones.
3. La vectorización aplica la misma operación a columnas completas y reduce el trabajo ejecutado en ciclos de Python.
4. Con un diccionario, `replace()` conserva el valor sin correspondencia y `map()` genera un valor ausente para esa clave.
5. `str.strip()` elimina espacios en los extremos y `str.casefold()` homogeneiza el uso de mayúsculas. Las equivalencias dudosas requieren validación externa.
6. `np.where()` sirve para dos resultados, como distinguir un dato presente de uno ausente. `np.select()` sirve para varias condiciones ordenadas.
7. Se usa el resultado de la primera condición verdadera. Por eso el conflicto de identidad va antes que los umbrales didácticos.
8. `BELL0` puede ser un error de digitación o una categoría distinta. Debe mantenerse pendiente hasta contrastarla con la fuente.
9. Una actualización posterior al 18 de octubre queda fuera del universo del ejemplo. Se conserva la fila y se documentan la fecha y el motivo de exclusión.
10. Una misma clave aparece en más de una fila y hay documentos ausentes. Contar filas mide registros.
11. La procedencia vincula cada resultado con su origen. La huella comprueba si cambiaron los bytes de la fuente.
12. Una regla debe identificar campos, transformación, tratamiento de nulos, unidades, umbrales, corte, control, limitación y responsable de revisión.
13. Se vuelve a leer el CSV y se comparan filas, procedencia, fechas y campos relevantes. La huella valida por separado la integridad de la fuente.
14. Un indicador necesita definición, unidad, fecha de corte, universo, numerador, denominador, exclusiones y limitaciones.
15. En un sistema real, los reportes compartidos deben usar datos agregados y restringir el acceso a identificadores personales.

## Autoevaluación 6.4

Cada valoración corresponde al aprendiz. Estas son las evidencias para sustentarla con la escala Logrado, En proceso o Requiero apoyo.

| Criterio | Evidencia para valorar |
| --- | --- |
| Recupero el proyecto desde cero | Instrucciones del README y ejecución secuencial del laboratorio. Falta comprobar la instalación limpia. |
| Explico tres transformaciones | Promedio, equivalencia de ciudad y prioridad. |
| Distingo dato faltante y dato negativo | Asistencia ausente frente a asistencia observada bajo el umbral. |
| Documento precedencia y denominador | Bitácoras del laboratorio y del reto, con 19 filas como universo de completitud. |
| Identifico los límites | La sección de sustentación explica el conflicto de identidad y la revisión humana. |
