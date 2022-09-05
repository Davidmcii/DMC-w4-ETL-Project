# DMC-w4-ETL-Project

## OBJETIVO: 

CREAR UNA BASE DE DATOS COMO BASE PARA PREDECIR LA POTENCIA GENERADA POR LAS ENERGÍAS RENOVABLES EN EL MERCADO ESPAÑOL DEPENDIENDO DE LA PREDICCIÓN METEOROLÓGICA Y ANALIZANDO EL COMPORTAMIENTO DE LOS HISTÓRICOS METEOROLÓGICOS

Se ha “escrapeado” información de la distribución de las plantas fotovoltaicas de España (15,4MW Vs los 16,8MW instalados)

Se ha “escrapeado” información de las plantas eólicas en España (27,5MW vs los 29,5MW instalados)

Se han descargado de la API de AEMET todas las estaciones meteorológicas e históricos desde 2010 -2022

## ORGANIZACIÓN DE LA DOCUMENTACIÓN

2-Code

    1-w4_main- Código para conseguir la distribución de las plantas FV y su potencia

    2-w4_mainEolico(lento): Código para descargar la info de todos los PPEE de Europa. Se descargó por la lentitud de la web al cargar cada página (Requería abrir aprox 25000 registros)

    2-w4_mainEolico: Código para conseguir la distribución de los PPEE y potencia

    3- 3-w4_main_API_EAMET: Código para recopilar los históricos de datos meteorológicos
