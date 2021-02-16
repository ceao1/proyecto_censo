import pandas as pd 
import numpy as np
import psycopg2
import json



class Utilidades:
  

  def cargar_csv(self):
    return pd.read_csv('datos.csv')


  def conectar_db(self):
    f=open('./credenciales/credenciales.json')
    credenciales=json.load(f)
    conn= psycopg2.connect(dbname=credenciales['DB_NAME'],user=credenciales['db_user'],password=credenciales['db_pass'], host= credenciales['host_aws'])
    return conn


  def cargar_datos_db(self,conn):
    datos = pd.read_sql('''SELECT *
                        FROM resumen_features_manzanas'''
                        ,con=conn)
    return datos


  def alistar_datos(self, dataset, drop_cols):
    df_final = dataset.drop(drop_cols, axis=1)
    return df_final






