"""Procesamiento reproducible de datos académicos ficticios (sin conexión a MongoDB)."""
from pathlib import Path
import pandas as pd
import numpy as np

def procesar(archivo, salida):
    archivo, salida = Path(archivo), Path(salida)
    salida.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(archivo, encoding="utf-8-sig")
    origen = df.copy(deep=True)
    for col in ("nota_python", "nota_datos", "asistencia"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["conflicto_identidad"] = df["documento"].notna() & df["documento"].duplicated(keep=False)
    df["numero_notas"] = df[["nota_python", "nota_datos"]].notna().sum(axis=1)
    df["promedio_dos_notas"] = (df["nota_python"] + df["nota_datos"]) / 2
    df["completo_para_revision"] = df[["nota_python", "nota_datos", "asistencia"]].notna().all(axis=1)
    df["programa_normalizado"] = df["programa"].astype("string").str.strip().str.casefold().replace({"adso":"ADSO", "ciencia datos python":"Ciencia de datos con Python", "ciencia de datos con python":"Ciencia de datos con Python"})
    df["codigo_programa"] = df["programa_normalizado"].map({"ADSO":"ADS", "Ciencia de datos con Python":"CDP"})
    df["estado_revision"] = np.select([df["conflicto_identidad"], df["documento"].isna(), ~df["completo_para_revision"], df["asistencia"].lt(80) | df["promedio_dos_notas"].lt(3.5)], ["Revisar identidad", "Revisar documento", "Datos incompletos", "Revisión sugerida"], default="Sin alerta didáctica")
    assert len(df) == len(origen)
    assert df.loc[df["numero_notas"].lt(2), "promedio_dos_notas"].isna().all()
    assert int(df["conflicto_identidad"].sum()) == int(origen["documento"].duplicated(keep=False).sum())
    indicadores = pd.DataFrame([
        {"indicador":"Completitud de notas y asistencia", "numerador":int(df["completo_para_revision"].sum()), "denominador":len(df)},
        {"indicador":"Registros con identidad en conflicto", "numerador":int(df["conflicto_identidad"].sum()), "denominador":len(df)},
    ])
    indicadores["porcentaje"] = (100*indicadores["numerador"]/indicadores["denominador"]).round(2)
    df.to_csv(salida/"semana5_integrado_transformado.csv", index=False, encoding="utf-8-sig")
    indicadores.to_csv(salida/"semana5_integrado_indicadores.csv", index=False, encoding="utf-8-sig")
    return df, indicadores

if __name__ == "__main__":
    raiz=Path(__file__).resolve().parents[1]
    datos,indicadores=procesar(raiz/"data"/"processed"/"seguimiento_academico_semana3_preparado.csv",raiz/"outputs")
    print(f"Registros procesados: {len(datos)}")
    print(indicadores.to_string(index=False))
