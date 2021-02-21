import pandas as pd 
import numpy as np
import psycopg2
import json
import geopandas as gpd
import folium
import streamlit as st

from folium import plugins
from folium.plugins import HeatMap


class Utilidades:
  
  def conectar_db(self):
    '''
        Hace la conexión a la base de datos postgres donde se encuentra la información descargado del censo nacional de colombia 2018 alojada en AWS,
        toma las credenciales de un archivo json 

        :returns:

        conn : object
            Es el objeto con el que se conecta a la base de datos
    '''

    f=open('./credenciales/credenciales.json')
    credenciales=json.load(f)
    conn= psycopg2.connect(dbname=credenciales['DB_NAME'],user=credenciales['db_user'],password=credenciales['db_pass'], host= credenciales['host_aws'])
    return conn

  
  def cargar_datos_db(self,conexion, query='''SELECT * FROM resumen_features_manzanas'''):
    '''
        Hace una consulta a una base de datos y regresa un pd.DataFrame con la informacion

        :params:

        conexion : object
            Es el objeto de conexion a la base de datos
        
        query : str
            Es el string con la consulta que se desea hacer a la base de datos

        :returns:

        datos : pd.DataFrame
            Es un DataFrame con el resultado de la consulta
    '''
    datos = pd.read_sql(query, con=conexion)
    return datos

  
  def cargar_csv(self, ruta_csv='datos.csv'):
    '''
        Carga datos de un archivo csv

        :params:

        ruta_csv : str
              Es el path del archivo CSV
        
        :returns:

        pd.DataFrame
    '''
    return pd.read_csv(ruta_csv)

  
  def cargar_mapa(self, ruta='./mapas/manzana/MGN_URB_MANZANA.shp'):
    '''
        Carga mapa usando geopandas

        :params:

        ruta : str
            Es el path del mapa

        :returns:

        gpd.DataFrame
    '''

    return gpd.read_file(ruta)

  
  def depurar_columnas(self, gpd_mapa, codigo_dpto='50', columnas_a_dejar=['DPTO_CCDGO','MPIO_CCDGO','MANZ_CCNCT','geometry']):
    '''
        Filtra un archivo de mapa por su departamento y deja las columnas deseadas

        :params:
        
        gpd_mapa : gpd.DataFrame
            Es un objeto cargado con geopandas que se quiere depurar
        
        columnas_a_dejar : list
            Es el listado de columnas que se quieren dejar en el dataframe
        
        :returns:

        gpd.DataFrame

    '''
    return gpd_mapa[gpd_mapa['DPTO_CCDGO'] == codigo_dpto][columnas_a_dejar]

  
  def unir_dataframes(self, df_izquierda, indice_izquierda, df_derecha, indice_derecha, tipo_union='left'):
    '''
        Une dos dataframes

        :params:

        tipo_union : str
            Es el tipo de union que se realiza, por default toma left

        df_izquierda : pd.DataFrame
            Es el dataframe al cual se le hara un merge
        
        indice_izquierda : str
            Feature(s) o columna(s) por la cual se hara la union en la izquierda

        df_derecha : pd.DataFrame
            Es el dataframe que se unira
        
        indice_derecha : str
            Feature(s) o columna(s) por la cual se hara la union en la derecha

        :returns:

        final : pd.DataFrame
            Dataframe con los datos de la union 
    '''
    df_unido = df_izquierda.merge(df_derecha, how=tipo_union, left_on=indice_izquierda, right_on=indice_derecha)
    return df_unido


class Mapa(folium.Map):

  
  def __init_(self, *args, **kwargs):
    folium.Map.__init__(*args, **kwargs)
  
  
  def agregar_capa(self, nombre_capa, gpd_mapa, df_datos, columnas_datos, nombre_leyenda, llave_mapa='feature.properties.MANZ_CCNCT'):
    capa=folium.Choropleth(
      geo_data=gpd_mapa,
      name=nombre_capa,
      data=df_datos,
      columns=columnas_datos,
      key_on=llave_mapa,
      fill_color="YlOrRd",
      fill_opacity=0.7,
      line_opacity=0.9,
      legend_name=nombre_leyenda
  ).add_to(self)
    