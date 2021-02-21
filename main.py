import pandas as pd 
import numpy as np
import psycopg2
import json
import geopandas as gpd
import folium
import streamlit as st

from streamlit_folium import folium_static
from folium import plugins
from folium.plugins import HeatMap


from functions import Utilidades
from functions import Mapa

@st.cache(suppress_st_warning=True)
def cargue():

    utils = Utilidades()

    #conexion = utils.conectar_db()
    #data = utils.cargar_datos_db(conexion)
    
    data=utils.cargar_csv()

    datos_mapas = utils.cargar_mapa()
    datos_mapas = utils.depurar_columnas(gpd_mapa=datos_mapas)

    final = utils.unir_dataframes(df_izquierda=data, indice_izquierda='codigo_manzana', df_derecha=datos_mapas[['MANZ_CCNCT','geometry']], indice_derecha='MANZ_CCNCT')
    
    return datos_mapas, final

@st.cache(suppress_st_warning=True)
def dibujar_mapa():
  mapa = Mapa(location=[4.05, -73.627321], zoom_start=7)
  mapa.agregar_capa(nombre_capa='Estrato', gpd_mapa=datos_mapas, df_datos=final, columnas_datos=['MANZ_CCNCT','estrato'], nombre_leyenda='Estrato')  
  folium.LayerControl().add_to(mapa)
  return mapa


if __name__ == '__main__':
  datos_mapas, final = cargue()
  
  st.title('Prueba de streamlit')
  
  menu = ["Opcion1","Opcion2","Opcion3"]
  
  choice = st.sidebar.selectbox('Menu',menu)
  
  if choice == "Opcion1":
    st.subheader('Opcion1')
  else:
    pass
  
