# TP2: Algoritmos geneticos
## Introduccion
 Este proyecto es una implementacion de algoritmos geneticos para resolver un problema de minimizacion de una funcion de la cual solo se tienen ciertos valores de prueba.
 Se encuentran implementados los siguientes algoritmos:
 
#### Algoritmos de cruza
    - Cruza simple
    - Cruza multiple
    - Cruza uniforme

#### Algoritmos de seleccion
    - Seleccion elite
    - Seleccion de ruleta
    - Seleccion rank
    - Seleccion competitiva (Tournament)
    - Seleccion de Boltzmann
    - Seleccion truncada


## Instalacion y ejecucion

Para el desarrollo del programa se utilizo la version 3.7 de Python

Las dependencias de los ejecutables se encuentran en el archivo requirements.txt para instalarlos, ejecutar

```shell
pip install -r requirements.txt
```
*Puede que en versiones de python3 sea necesario usar pip3*

Una vez instalada las dependecias, se encuentra un ejecutable ***main.py*** para correr el programa, el cual recibe como parametro un archivo de configuracion.
La forma de correrlo es la siguiente:

```shell
PYTHONPATH=`pwd`/.. python3 main.py <config.json>
```

*La definicion de la variable de entorno PYTHONPATH para la ejecucion es necesaria para que se resuelvan apropiadamente los modulos locales. Para una shell no bash como en windows, la variable de entorno se debe settear apropiadamente*



## Archivo de configuracion
El archivo de configuracion a pasar es un json, en el proyecto
se incluye un archivo de configuracion **config.json** a modo de ejemplo con la siguiente forma:

``` json
{   
    "gen_size": 100,
    "max_generations": 500,
    "crossing_fun": "double_cross",
    "selection_fun": "roulette_selection",
    "mutation_prob": 0.1,
    "mutation_std": 1,
}
```

A continuacion se detallan las propiedades a pasar y sus valores posibles:


| Propiedad    | Obligatoria?                       | Valores posibles                                                                                                              |
|--------------|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
 | gen_size    | Si                                 | x / x pertenece a Naturales                                                                                                   |
 | max_generations| Si                                 | x / x pertenece a Naturales                                                                                                   | 
 | Crossing_fun | Si                                 | simple_cross o double_cross o rand_cross                                                                                      | 
| selection_fun| Si                                 | elite_selection o roulette_selection o boltzmann_selection o truncated_selection o rank_selection o tournament_selection      | 
 | mutation_prob | Si                                 | x/ x pertenece al interavalo (0,1)| 
 | mutation_std | Si                                 | x/x pertence a Reales > 0 |
 | K | Solo si se usa truncated_selection | x/ x pertenece a Naturales y x < gen_size|
| threshold| Solo si se usa tournament_selection | x / x pertenece al intervalo [0.5,1]|       
| initial_temp | Solo si se usa boltmann_selection  | x/ x pertenece a Reales > 0|
| decrease_factor | Solo si se usa boltzmann_selection | x/ x pertenece a Reales > 0|
|change_factor| Solo si se usa boltzmann_selection |  x/ x pertenece a Reales > 0|

