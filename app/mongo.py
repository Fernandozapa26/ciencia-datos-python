"""Carga opcional de registros académicos a MongoDB local, sin alterar la fuente."""
from pathlib import Path
from datetime import datetime
import pandas as pd
from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
from .analisis import procesar

DB_NAME="academico_sena_p05"
DATASET="S05_ACADEMICO_V1"

def importar(uri="mongodb://localhost:27017"):
    raiz=Path(__file__).resolve().parents[1]
    df,_=procesar(raiz/"data"/"processed"/"seguimiento_academico_semana3_preparado.csv",raiz/"outputs")
    client=MongoClient(uri,serverSelectionTimeoutMS=4000)
    client.admin.command("ping")
    db=client[DB_NAME]
    coleccion=db["s05_registros"]
    coleccion.create_index([("dataset",ASCENDING),("fila_fuente_integracion",ASCENDING)],unique=True)
    for i,(_,fila) in enumerate(df.iterrows(),start=1):
        doc={"dataset":DATASET,"fila_fuente_integracion":i,"schema_version":1}
        for k,v in fila.items():
            if pd.isna(v):doc[k]=None
            elif isinstance(v,(pd.Timestamp,datetime)):doc[k]=v.to_pydatetime() if isinstance(v,pd.Timestamp) else v
            elif hasattr(v,"item"):doc[k]=v.item()
            else:doc[k]=v
        coleccion.update_one({"dataset":DATASET,"fila_fuente_integracion":i},{"$setOnInsert":doc},upsert=True)
    print("MongoDB:",DB_NAME,"Registros:",coleccion.count_documents({"dataset":DATASET}))
    client.close()

if __name__=="__main__":importar()
