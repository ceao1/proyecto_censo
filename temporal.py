from functions import Utilidades
import pandas as pd

utils= Utilidades()

conexion = utils.conectar_db()

datos=utils.cargar_datos_db(conexion)

datos.to_csv('datos.csv',index=False)

