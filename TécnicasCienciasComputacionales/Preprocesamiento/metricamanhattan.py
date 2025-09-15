import csv
import math as m
from idlelib.iomenu import encoding

from ipywidgets import jslink

from Preprocesamiento.ejemplomain import encabezado

matriz= []


with open('','r',encoding="utf-8") as csvfile:
 reader= csv.reader(csvfile)
 encabezado= next(reader)


for row in matriz:
