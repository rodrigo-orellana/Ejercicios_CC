## Arquitecturas software para la nube  
**Ejercicio 1.** Buscar una aplicación de ejemplo, preferiblemente propia, y deducir qué patrón es el que usa. ¿Qué habría que hacer para evolucionar a un patrón tipo microservicios?  
*Entre los proyectos que he implementado, podría citar del año 2016 lideré el upgrade del sistema financiero [Oracle EBS](https://www.oracle.com/es/applications/ebusiness/) para una empresa de telecomunicaciones más importanes de latinoamerica. Esta tenía una [arquitectura orientada a servicios](https://es.wikipedia.org/wiki/Arquitectura_orientada_a_servicios). Para evolucionar la aplicación a un patrón de tipo microservicios, se tendría que identificar las principales entidades para luego separarlas en servicios independientes que se comuniquen a travez de alguna interfaz (cómo API REST) y luego desplegarlas en la nube  

**Ejercicio 2.** En la aplicación que se ha usado como ejemplo en el ejercicio anterior, ¿podría usar diferentes lenguajes? ¿Qué almacenes de datos serían los más convenientes?  
El estar en una arquitectura de microservicios permitiria que cada microservicio poseea un lenguaje diferente, ya que la comunicación sería a traves de la exposición de una interfaz web. Esto permite crear nucleos de equipos de desarrollo en donde cada uno desarrolle en el lenguaje de programación que prefieran o el más adecuado al ambito de la entidad.  
Cada microservicio podría contar con un motor de base de datos distinto, en algunos casos puede utilizar noSQL (mongoDB) y en otras las propias del producto (Oracle), esta última debido a que estaba disponible por la compra del producto y cuenta con un soporte de alto estandar.