"""Reto autónomo S5: transformación trazable sobre una copia de datos ficticios."""
from pathlib import Path
import hashlib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def ejecutar():
    fuente = ROOT / 'data/processed/seguimiento_academico_semana3_preparado.csv'
    destino = ROOT / 'outputs'
    destino.mkdir(exist_ok=True)
    huella = hashlib.sha256(fuente.read_bytes()).hexdigest()
    df = pd.read_csv(fuente, encoding='utf-8-sig')
    original = df.copy(deep=True)
    ciudades = df['ciudad'].astype('string').str.strip().str.casefold()
    equivalencias = {'medellín': 'Medellín', 'medellin': 'Medellín', 'bello': 'Bello', 'itagüí': 'Itagüí', 'itagui': 'Itagüí'}
    df['ciudad_original'] = df['ciudad']
    df['ciudad_normalizada'] = ciudades.map(equivalencias)
    df['ciudad_pendiente_revision'] = ciudades.notna() & df['ciudad_normalizada'].isna()
    for c in ['nota_python', 'nota_datos', 'asistencia']:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    completas = df[['nota_python', 'nota_datos', 'asistencia']].notna().all(axis=1)
    df['notas_completas'] = df[['nota_python','nota_datos']].notna().all(axis=1)
    df['promedio_dos_notas'] = (df['nota_python'] + df['nota_datos']) / 2
    df['conflicto_identidad'] = df['documento'].notna() & df['documento'].duplicated(keep=False)
    df['prioridad_revision'] = np.select([
        df['conflicto_identidad'],
        df['ciudad_pendiente_revision'],
        ~completas,
        (df['asistencia'] < 80) | (df['promedio_dos_notas'] < 3.5),
    ], ['Identidad contradictoria', 'Ciudad sin equivalencia', 'Datos incompletos', 'Revisión académica didáctica'], default='Sin alerta')
    assert len(df) == len(original)
    assert df.loc[~df['notas_completas'], 'promedio_dos_notas'].isna().all()
    antes = original.loc[(original['programa'].astype('string').str.strip().str.casefold()=='adso') & (pd.to_numeric(original['asistencia'],errors='coerce')<80),'documento'].tolist()
    despues = df.loc[(df['programa'].astype('string').str.strip().str.casefold()=='adso') & (df['asistencia']<80),'documento'].tolist()
    assert antes == despues
    assert hashlib.sha256(fuente.read_bytes()).hexdigest() == huella
    df.to_csv(destino/'semana5_reto_autonomo.csv', index=False, encoding='utf-8-sig')
    pd.DataFrame([{'indicador':'Completitud notas y asistencia','numerador':int(completas.sum()),'denominador':len(df),'porcentaje':round(completas.mean()*100,2)}]).to_csv(destino/'semana5_reto_indicador.csv',index=False,encoding='utf-8-sig')
    reglas = [
        ('R01','ciudad','ciudad_normalizada','strip + casefold + map','Desconocidos quedan sin mapear'),
        ('R02','ciudad_normalizada','ciudad_pendiente_revision','marcar valores sin equivalencia','No se infiere una ciudad'),
        ('R03','notas y asistencia','completas','tres valores presentes','No imputar nulos'),
        ('R04','dos notas','promedio_dos_notas','media aritmética solo con ambas','Nulos producen NaN'),
        ('R05','identidad, ciudad, completitud, asistencia y notas','prioridad_revision','np.select en orden','Primera regla verdadera gana'),
    ]
    pd.DataFrame(reglas,columns=['regla','origen','destino','criterio','limitacion']).to_csv(destino/'semana5_reto_bitacora.csv',index=False,encoding='utf-8-sig')
    comprobacion=pd.read_csv(destino/'semana5_reto_autonomo.csv',encoding='utf-8-sig')
    assert len(comprobacion)==len(df)
    print(f'Reto S5 OK: {len(df)} filas, completitud {int(completas.sum())}/{len(df)}; SHA256 fuente {huella}')
    return df

if __name__ == '__main__': ejecutar()
