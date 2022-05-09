# TP2: Perceptron simple y multicapa
## Introduccion
En este proyecto se implementa el perceptron simple, 
tanto como una red multicapa completa. Se facilitan funciones de activacion escalon, lineal y no lineales.


## Instalacion y ejecucion

Para el desarrollo del programa se utilizo la version 3.7 de Python

Las dependencias de los ejecutables se encuentran en el archivo requirements.txt para instalarlos, ejecutar

```shell
pip install -r requirements.txt
```
*Puede que en versiones de python3 sea necesario usar pip3*

Una vez instalada las dependecias, se encuentran, dentro de runnables,
ejecutab les ***ex{NUM}.py*** (con NUM el indice del ejercicio) 
que permite correr el programa representativo para cada ejercicio. Estos reciben
como parametro un archivo de configuracion.

La forma de correrlo es la siguiente:

```shell
PYTHONPATH=`pwd`/.. python3 ex{NUM}.py <config.json>
```

*La definicion de la variable de entorno PYTHONPATH para la ejecucion es necesaria para que se resuelvan apropiadamente los modulos locales. Para una shell no bash como en windows, la variable de entorno se debe settear apropiadamente*



## Archivo de configuracion
El archivo de configuracion a pasar es un json, en el proyecto
se incluye un archivo de configuracion **config.json** a modo de ejemplo con la siguiente forma:

``` json
{   
  "activation_function": "linear_activation",
  "learning_rate": 0.01,
  "batch_size": 1000
}
```

A continuacion se detallan las propiedades a pasar y sus valores posibles:


| Propiedad    | Obligatoria?                       | Valores posibles                                                                                                              |
|--------------|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
 | activation_function    | Si                                 | step_activation - linear_activation - sigmoid_classic_activation - sigmoid_tanh_activation                                                                                                   |
 | learning_rate| Si                                 | x / x pertenece a reales positivos                                                                                                   | 
 | batch_size | Si                                 | x / x perteneciente a los naturales                                                                                      | 

