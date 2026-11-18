// Ejecutar: mongosh academico_sena_p05 nosql/academico/consultas.js
// Consultas de integración académica: no sustituyen el catálogo P05 original sin homologación docente.
const c=db.getCollection('s05_registros'); const d={dataset:'S05_ACADEMICO_V1'};
const q=[
 ['Q01', {...d,programa_normalizado:'ADSO'}],
 ['Q02', {...d,conflicto_identidad:true}],
 ['Q03', {...d,completo_para_revision:false}],
 ['Q04', {...d,asistencia:{$lt:80}}],
 ['Q05', {...d,promedio_dos_notas:{$gte:3,$lte:4}}],
 ['Q06', {...d,estado_revision:'Revisar identidad'}],
 ['Q07', {...d,codigo_programa:'CDP'}],
 ['Q08', {...d,nota_python:{$exists:true,$ne:null}}],
 ['Q09', {...d,$or:[{asistencia:{$lt:80}},{promedio_dos_notas:{$lt:3.5}}]}],
 ['Q10', {...d,estado_revision:'Sin alerta didáctica'}],
];
q.forEach(([id,f])=>print(id,JSON.stringify(c.find(f,{_id:0,fila_fuente_integracion:1,documento:1}).sort({fila_fuente_integracion:1}).toArray())));
