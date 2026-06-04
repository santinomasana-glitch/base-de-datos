import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

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

#-------------------------------------------
#GRAFICO 1: grafico de barras  (con seaborn)
#-------------------------------------------

print("\n generando grafico de barras")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(9,5))

sns.barplot(
    data=df,
    x="kepid",
    y="koi_pdisposition",
    estimator=sum,
    errorbar=None,
    palette="viridis"
)

plt.title(
    "distribucion economica de tecnologia avanzada",fontsize=11
)
plt.xlabel("tipo de kepid", fontsize=11)
plt.ylabel("total:(CANDI)", fontsize=11)

plt.tight_layout()
#plt.xticks(rotation=40, fontsize=6) 
#sirve para rotar las letras
plt.savefig("grafico_barras.png", dpi=300)
plt.close()
print("grafico de barras guardado exitosamente")

#--------------------------------------------
#grafico de torta
#--------------------------------------------
print("\n generando grafico de torta")
datos_torta=(
     df.groupby ("koi_pdisposition")["kepid"]
    .sum()
    .nlargest(5)
)
plt.figure(figsize=(7,7))
plt.pie(
   datos_torta.values,
   labels=datos_torta.index,
   autopct="%1.1f%%",
   colors=sns.color_palette("Set2")[0:5],
   startangle=140,
   wedgeprops={'edgecolor':'white','linewidth':2},
)
plt.title(
    "distribucion interna: tecnologia avanzada",fontsize=11
)
plt.tight_layout()
plt.savefig("grafico_torta.png", dpi=300)
print("grafico de torta guardado exitosamente")
