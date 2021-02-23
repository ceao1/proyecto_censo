import pandas as pd 
import numpy as np
import psycopg2
import json
import geopandas as gpd
import folium
from folium import plugins
from folium.plugins import HeatMap
import matplotlib.pyplot as plt
import seaborn as sns


from functions import Utilidades
from functions import Mapa


if __name__ == '__main__':

  utils = Utilidades()

  #conexion = utils.conectar_db()
  #data = utils.cargar_datos_db(conexion)

  data=utils.cargar_csv()

  datos_mapas = utils.cargar_mapa()

  datos_mapas = utils.depurar_columnas(gpd_mapa=datos_mapas)

  final = utils.unir_dataframes(df_izquierda=data, indice_izquierda='codigo_manzana', df_derecha=datos_mapas[['MANZ_CCNCT','geometry']], indice_derecha='MANZ_CCNCT')

 
  for feature in final.columns[1:-2]:
    print(feature)
    mapa = Mapa(location=[4.05, -73.627321], zoom_start=7)
    mapa.agregar_capa(nombre_capa=feature, gpd_mapa=datos_mapas, df_datos=final, columnas_datos=['MANZ_CCNCT',feature], nombre_leyenda=feature)  
    folium.LayerControl().add_to(mapa)
    nombre_mapa = './mapas_finales/mapa_' + feature + '.html'
    mapa.save(nombre_mapa)
 
  correlacion = final.iloc[:,1:-2].corr()
  cmap = sns.diverging_palette(230, 20, as_cmap=True)
  figura = sns.heatmap(correlacion, cmap=cmap, vmax=1, annot=True,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
  figura.figure.savefig('./imagenes/correlation.png')