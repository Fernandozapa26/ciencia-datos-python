
/*
 * PROYECTO INTEGRADO - SEMANA 5
 * Ciencia de Datos + MongoDB (NoSQL)
 *
 * Archivo: nosql/academico/crud.js
 *
 * Objetivo:
 * Demostrar las operaciones CRUD de MongoDB:
 * CREATE, READ, UPDATE y DELETE.
 *
 * IMPORTANTE:
 * Las pruebas se realizan con registros temporales.
 * Los 19 registros académicos originales no deben modificarse.
 */

// =====================================================
// 1. CONEXIÓN Y CONFIGURACIÓN
// =====================================================

// Seleccionamos la base de datos de nuestro proyecto.
const dbAcademica = db.getSiblingDB("academico_sena_p05");

// Seleccionamos la colección de registros académicos.
const coleccion = dbAcademica.getCollection("s05_registros");

// Identificador del conjunto de datos de la Semana 5.
const dataset = "S05_ACADEMICO_V1";

// Identificadores exclusivos de nuestros documentos de prueba.
const ids = ["CRUD-S5-01", "CRUD-S5-02", "CRUD-S5-03"];


// 2. FUNCIÓN PARA VALIDAR LOS RESULTADOS


// Si una operación no cumple lo esperado,
// detenemos la prueba mostrando un error.
function verificar(condicion, mensaje) {
  if (!condicion) {
    throw new Error(mensaje);
  }
}

// Filtro para identificar únicamente nuestros registros
// temporales y evitar eliminar documentos académicos.
const filtroTemporal = {
  _id: { $in: ids },
  dataset: dataset,
  temporal: true
};

// Contamos los registros antes de iniciar las pruebas.
const totalAntes = coleccion.countDocuments({ dataset });

// Verificamos que estén los 19 registros originales.
verificar(
  totalAntes === 19,
  "ERROR: Se esperaban 19 registros académicos"
);

// Comprobamos que los identificadores de prueba estén libres.
verificar(
  coleccion.countDocuments({ _id: { $in: ids } }) === 0,
  "ERROR: Ya existen documentos con los IDs de prueba"
);

print("Registros originales antes del CRUD:", totalAntes);

// 3. CREATE - CREAR DOCUMENTOS


try {


const estudiantes = ids.map((id, i) => ({
  // Identificador único del documento temporal.
  _id: id,

  // Conjunto académico al que pertenece la prueba.
  dataset: dataset,

  // Permite distinguir los documentos de prueba.
  temporal: true,

  // Identificador único de fila para respetar
  // el índice compuesto de MongoDB.
  // Usamos valores negativos para separarlos
  // de las filas académicas originales (1 a 19).
  fila_fuente_integracion: -(i + 1),

  // Información ficticia del estudiante.
  documento: `PRUEBA-${i + 1}`,
  nombre: `Estudiante temporal ${i + 1}`,
  programa_normalizado: "ADSO",

  // Campo numérico utilizado en updateOne().
  intentos_contacto: 0
}));


  // INSERT ONE:
  // Inserta un único documento en MongoDB.
  let resultado = coleccion.insertOne(estudiantes[0]);

  verificar(
    resultado.acknowledged,
    "ERROR en insertOne"
  );

  print("CREATE - insertOne OK");

  // INSERT MANY:
  // Inserta varios documentos en una sola operación.
  resultado = coleccion.insertMany(estudiantes.slice(1));

  verificar(
    Object.keys(resultado.insertedIds).length === 2,
    "ERROR en insertMany"
  );

  print("CREATE - insertMany OK");


  // 4. READ - CONSULTAR DOCUMENTOS


  // FIND:
  // Recupera los tres estudiantes temporales.
  const encontrados = coleccion.find(filtroTemporal).toArray();

  verificar(
    encontrados.length === 3,
    "ERROR: No se encontraron los tres documentos"
  );

  print("READ - find OK:", encontrados.length);


  // 5. UPDATE - ACTUALIZAR DOCUMENTOS


  // UPDATE ONE:
  // Modifica el nombre de un estudiante.
  // $set reemplaza el valor de un campo.
  // $inc incrementa un valor numérico.
  resultado = coleccion.updateOne(
    {
      _id: ids[0],
      dataset: dataset,
      temporal: true
    },
    {
      $set: {
        nombre: "Estudiante actualizado"
      },
      $inc: {
        intentos_contacto: 1
      }
    }
  );

  verificar(
    resultado.modifiedCount === 1,
    "ERROR en updateOne"
  );

  print("UPDATE - updateOne OK");

  // UPDATE MANY:
  // Modifica simultáneamente los otros dos estudiantes.
  resultado = coleccion.updateMany(
    {
      _id: { $in: ids.slice(1) },
      dataset: dataset,
      temporal: true
    },
    {
      $set: {
        estado_revision: "Validado"
      }
    }
  );

  verificar(
    resultado.modifiedCount === 2,
    "ERROR en updateMany"
  );

  print("UPDATE - updateMany OK");


  // 6. DELETE - ELIMINAR DOCUMENTOS


  // DELETE ONE:
  // Elimina únicamente el primer estudiante temporal.
  resultado = coleccion.deleteOne({
    _id: ids[0],
    dataset: dataset,
    temporal: true
  });

  verificar(
    resultado.deletedCount === 1,
    "ERROR en deleteOne"
  );

  print("DELETE - deleteOne OK");

  // DELETE MANY:
  // Elimina los otros dos estudiantes temporales.
  resultado = coleccion.deleteMany({
    _id: { $in: ids.slice(1) },
    dataset: dataset,
    temporal: true
  });

  verificar(
    resultado.deletedCount === 2,
    "ERROR en deleteMany"
  );

  print("DELETE - deleteMany OK");

} finally {


  // 7. LIMPIEZA DE SEGURIDAD


  // Si ocurre un error durante las pruebas,
  // intentamos eliminar los documentos temporales
  // que hayan quedado pendientes.
  coleccion.deleteMany(filtroTemporal);
}


// 8. VALIDACIÓN FINAL


// Contamos nuevamente los documentos académicos.
const totalDespues = coleccion.countDocuments({ dataset });

// El total debe ser igual al inicial.
verificar(
  totalDespues === totalAntes,
  "ERROR: Cambió la cantidad de registros académicos"
);

// Verificamos que no queden documentos temporales.
verificar(
  coleccion.countDocuments(filtroTemporal) === 0,
  "ERROR: Quedaron documentos temporales"
);

print("Registros originales después del CRUD:", totalDespues);
print("CRUD OK: 19 registros originales conservados.");
