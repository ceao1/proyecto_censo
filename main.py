import pandas as pd

from sklearn.cluster import KMeans
from functions import Utilidades


def main():

    utils = Utilidades()

    #conexion = utils.conectar_db()
    #data = utils.cargar_datos_db(conexion)
    
    data=utils.cargar_csv()

    data_final = utils.alistar_datos(data,['codigo_manzana'])
    
    kmeans = KMeans().fit(data_final)
    data['cluster'] = kmeans.predict(data_final)
    
    print(data.columns)
    print(kmeans.cluster_centers_)

    #data.to_csv('datos_cluster.csv',index=False)


if __name__ == '__main__':
  main()








if __name__ == '__main__':

  main()

