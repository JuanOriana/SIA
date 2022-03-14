# TP1: Metodos de busqueda
## Introduccion
En el presente trabajo se busca mostrar diversas formas de
resolver el rompecabezas de ocho numeros (variacion de https://es.wikipedia.org/wiki/Juego_del_15)
mediante el uso de diversos metodos de busqueda, no informados e informados.
Se implementaron tres estrategias de busqueda no informadas: BPA, BPP y BPPV;
tres estrategias de busqueda informadas: Heuristica Local,
Heuristica Global y A*; y ademas se desarrollaron tres heuristicas: dos admisibles y una no admisible.

## Instalacion y ejecucion

Para el desarrollo del programa se utilizo la version 3.7 de Python

Las dependencias de los ejecutables se encuentran en el archivo requirements.txt
para instalarlos, ejecutar
```shell
pip install -r requirements.txt
```
*Puede que en versiones de python3 sea necesario usar pip3*

Una vez instaladas las dependencias, hay dos ejecutables para correr el programa,
ambos acompañados de un archivo de configuracion (ver más adelante): Una opcion
de display en terminal, para testeos más rapidos y especificos, y una opcion interactiva con GUI usando pygame.
La forma de correr cada uno, respectivamente, es:
```shell
PYTHONPATH=`pwd`/.. python3 console.py <config.json>
```
```shell
PYTHONPATH=`pwd`/.. python3 game.py <config.json>
```
La definicion de la variable de entorno PYTHONPATH para la ejecucion es necesaria
para que se resuelvan apropiadamente los modulos locales

La primera hace una resolucion **one shot**, donde corre el algoritmo
con los parametros especificados y luego muestra los resultados.
La segunda permite interactuar con el tablero, modificar su posicion, cambiar los algoritmos en tiempo real
y guardar estados anteriores.

## Archivo de configuracion
El archivo de configuracion a pasar es un json, en el proyecto
se incluye un archivo de configuracion a modo de ejemplo con la siguiente forma:
```json
{
  "start_state": {
    "0": [8, 7, 6],
    "1": [1, 4, 3],
    "2": [5, 2, 0]
  },
  "algorithm": "a_star",
  "heuristic": "deep"
}
```

Ademas del ejemplo **config.json** hay un archivo **hard_config.json** con un
problema que se resuelve en 30 pasos y un **easy_config.json** que tiene un problema
mas sencillo que se resuelve en 12 pasos.

A continuacion se detallan las propiedades a pasar y sus valores posibles:

| Propiedad   | Obligatoria?             | Valores posibles                                                                                                                                                    |
|-------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| start_state | Si                       | Incluye tres arreglos (0 al 2) con 3 elementos cada uno.  Debe representar matricialmente un estado del juego valido  (https://mathworld.wolfram.com/15Puzzle.html) |
| algorithm   | Si                       | bpa / bpp / bppv / a_star / local_heuristic / global_heuristic                                                                                                 |
| heuristic   | Si lo requiere el algoritmo | basic (admisible) / deep (admisible) / fat (no admisible) 
