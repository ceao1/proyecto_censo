import pandas as pd 
import numpy as np
import psycopg2
import json
import geopandas as gpd


class Utilidades:
  

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








