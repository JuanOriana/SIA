# Ejercicio Obligatorio 1

## Introduccion
En el presente trabajo se busca ver la eficiencia de distintos metodos de optimizacion no lineal

## Instalacion y ejecucion

Para el desarrollo del programa se utilizo la version 3.9 de Python

Las dependencias de los ejecutables se encuentran en el archivo requirements.txt
para instalarlos, ejecutar
```shell
pip install -r requirements.txt
```
*Puede que en versiones de python3 sea necesario usar pip3*

Una vez instaladas las dependencias, hay dos ejecutables para correr el programa:

Un conjugate (que usa scikit para calcular matematicamente el gradiente descendiente y los gradientes conjugados). Este se ejecuta asi:

```shell
PYTHONPATH=`pwd`/.. python3 conjugate.py <method=CG|L-BFGS-B>
```
Un main (que usa keras para construir una red neuronal con 3 inputs y una capa hidden de 2 nodos, con metodos de optimacion gradiente descendiente y adam).
Este se ejecuta asi:

```shell
PYTHONPATH=`pwd`/.. python3 main.py <method> <generation_max>
```
*La definicion de la variable de entorno PYTHONPATH para la ejecucion es necesaria
para que se resuelvan apropiadamente los modulos locales. Para una shell no bash como en windows, la variable de entorno se debe settear apropiadamente*
