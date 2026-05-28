import pandas as pd 

#importando csv
df=pd.read_csv("cumulative.csv")

print("OKEY! archivo descargado correctamente")



print(df.head())

filas,columnas = df.shape
print(f"el dataframe tiene {filas} filas y {columnas} columnas")

total_kepid = df["kepid"].count()
print(f"cantidad de filas en el kepid: {total_kepid}")

print("............analisis avanzado de datos..........")

filtro_avanzado = df["koi_pdisposition"].str.startswith('CANDI', na=False)
df_filtrado = df[filtro_avanzado]

total_registros = df_filtrado["koi_pdisposition"].count()
#print(f"cantidad de veces que aparece 'CANDI': {total_registros}")

suma_dinero = df_filtrado["dec"].sum()
#print(f"valor total de CANDI {suma_dinero:.2f}")

print(".......reporte automatico......")
print(f"valor total de CANDI {suma_dinero:.2f}")

if default_limite_alto:=(suma_dinero > 500):
    print("alerta: el volumen de candi es cirtico y de alta prioridad")
    print("requiere revision inmediata")

elif suma_dinero > 200:
    print("AVISO: VOLUMEN DE MERCADO MODERADO/ALTO")
    print("monitorear comportamiento proximo trimestre")

else:
    print("estado:volumen de mercado bajo dentro del parametro")
    print("no se requiere accion adicional")