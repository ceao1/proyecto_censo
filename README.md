# Proyecto de exploracion Censo Colombia 2018

## Resumen
Este proyecto busca servir de práctica usando los datos del censo nacional de Colombia de 2018, por manejo de volumen de datos solo se trabaja con datos del Departamento del meta.
Como antesala a este proyecto se descargaron los datos proporcionados por el DANE y se les dio tratamiento para alojarlos en una base de datos PostgreSql.
El objetivo inicial es poder generar un análisis descriptivo de algunas variables demográficas, permitiendo visualizarlas por medio de mapas.

## Fuentes de datos

Como se menciona anteriormente, la fuentes de datos son los resultados del Censo nacional de Colombia realizado en el año 2018 por el DANE, alojados en este [enlace](https://www.dane.gov.co/index.php/estadisticas-por-tema/demografia-y-poblacion/censo-nacional-de-poblacion-y-vivenda-2018).
Estos datos fueron descargos como csv y cargados posteriormente en una base de datos PostgreSql alojada en una instancia RDS de Amazon Web Services. Desde allí se generaron 
algunas vistas que permitían hacer la agregación de las variables analizadas. a nivel de código de manzana.

### Aclaraciones

Como este es un proyecto para desarrollar y aplicar diferentes conocimientos, se hospedó la base de datos en la instancia RDS ya mencionada. A pesar de esto, al estar haciendo uso
de la capa gratuita de AWS, descargué una copia en formato CSV con el resultado final de la vista agregada.

## Resultados

Como resultados finales, se crearon diferentes mapas en formato html que permiten ver los resultados a nivel de manzana (en este caso para las ciudades del departamento del Meta).
Estos mapas son bastante pesados por lo que tambien subo algunas imagenes de como se ven estos resultados.






