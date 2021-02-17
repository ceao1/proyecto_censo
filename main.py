import pandas as pd
import geopandas as gpd


from functions import Utilidades


def main():

    utils = Utilidades()

    #conexion = utils.conectar_db()
    #data = utils.cargar_datos_db(conexion)
    
    data=utils.cargar_csv()

    datos_mapas = gpd.read_file('./mapas/manzana/MGN_URB_MANZANA.shp')
    datos_mapas = datos_mapas[datos_mapas['DPTO_CCDGO'] == '50'][['DPTO_CCDGO','MPIO_CCDGO','MANZ_CCNCT','geometry']]
    
    
    print(data.head())
    print(datos_mapas.head())

    final = data.merge(datos_mapas[['MANZ_CCNCT','geometry']], how='left', left_on='codigo_manzana', right_on='MANZ_CCNCT')
    print(final.head())
    print(final.info())


if __name__ == '__main__':
  main()