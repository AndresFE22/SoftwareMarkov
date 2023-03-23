from flask import Flask, render_template, request
import numpy as np
import random as rm
import pandas as pd 
from sklearn.model_selection import train_test_split  
from sklearn.utils import check_array
from sklearn.ensemble  import RandomForestClassifier 
from sklearn.neural_network import MLPClassifier
import openpyxl
from et_xmlfile import xmlfile


#import matplotlib 
#import matplotlib.pyplot as plt 
#import seaborn as sns 
#df = pd.read_excel('MATRIZ.xlsx')

dataset = pd.read_csv('datasetPrediccionprueba.csv', delimiter= ";") 
app = Flask(__name__)

# Carga la matriz de transición desde el archivo Excel
matriz_transicion = pd.read_excel('MatrizLista.xlsx', index_col=0)

@app.route('/')
def index():
    return render_template('indexinter.html')
    

@app.route('/showpagetraining')
def showpagetraining():
  

#imprimir primeras 5 lineas del dataset 
  print(dataset.head()) 

#Preparar datos para entrenar 
  #Dividir atributos y etiquetas

  X = dataset.iloc[:, 0:18].values
  y = dataset.iloc[:, -1].values

#dividir los datos en etapas de entrenamiento y prueba
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#return render_template('training.html')

@app.route('/showpageprediction')
def showpageprediction():





#Preparar datos para entrenar 
#Dividir atributos y etiqueta

  return render_template('formprediction.html', variable= "alto")
  


@app.route('/doprediction', methods=['POST'])
def doprediction():

  print (request)
  #Codigo Matriz
  print(matriz_transicion.iloc[:3, :3])

  estado_origen = request.form['init']
  estado_destino = request.form['target']

    # Obtiene el valor correspondiente de la matriz de transición
  valor = matriz_transicion.loc[estado_origen, estado_destino]
  
  print(valor)  # imprime el valor en la consola

  porcentaje = valor * 100

  str.format("{:.2f}%".format(porcentaje))

  resultado = str.format("{:.2f}%".format(porcentaje))

  matriz_transicion.fillna(0, inplace=True)

  select_options = {
    #CORTE 1
    "Start": "Inicio",
    "EATa1c1": "entregar a tiempo la actividad 1 del corte 1",
    "EATa2c1": "entregar a tiempo la actividad 2 del corte 1",
    "EATa3c1": "entregar a tiempo la actividad 3 del corte 1",
    "EATa4c1": "entregar a tiempo la actividad 4 del corte 1",
    "EATpc1": "entregar a tiempo el parcial del corte 1",
    "EEXa1c1": "entregar extemporaneamente la actividad 1 del corte 1",
    "EEXa2c1": "entregar extemporaneamente la actividad 2 del corte 1",
    "EEXa3c1": "entregar extemporaneamente la actividad 3 del corte 1",
    "EEXa4c1": "entregar extemporaneamente la actividad 4 del corte 1",
    "EEXpc1": "entregar extemporaneamente el parcial del corte 1",
    "NoEa1c1": "no entregar la actividad 1 del corte 1",
    "NoEa2c1": "no entregar la actividad 2 del corte 1",
    "NoEa3c1": "no entregar la actividad 3 del corte 1",
    "NoEa4c1": "no entregar la actividad 4 del corte 1",
    "NoEpc1": "no entregar el parcial del corte 1",
    "Rcorte1": "retirarse en el corte 1",
    "RaM4,5c1": "tener un rendimiento alto mayor a 4,5 en el corte 1",
    "Rm3,5_4,4c1": "tener un rendimiento medio entre 3,5 y 4,4 en el corte 1",
    "Rb3,0_3,4c1": "tener un rendimiento entre bajo 3,0 y 3,4 en el corte 1",
    "Rp0_2,99c1": "estar reprobado entre 0 y 2,99 en el corte 1",

    #CORTE2
    "EATa1c2": "entregar a tiempo la actividad 1 del corte 2",
    "EATa2c2": "entregar a tiempo la actividad 2 del corte 2",
    "EATa3c2": "entregar a tiempo la actividad 3 del corte 2",
    "EATa4c2": "entregar a tiempo la actividad 4 del corte 2",
    "EATpc2":  "entregar a tiempo el parcial del corte 2",
    "EEXa1c2": "entregar extemporaneamente la actividad 1 del corte 2",
    "EEXa2c2": "entregar extemporaneamente la actividad 2 del corte 2",
    "EEXa3c2": "entregar extemporaneamente la actividad 3 del corte 2",
    "EEXa4c2": "entregar extemporaneamente la actividad 4 del corte 2",
    "EEXpc2": "entregar extemporaneamente el parcial del corte 2",
    "NoEa1c2": "no entregar la actividad 1 del corte 2",
    "NoEa2c2": "no entregar la actividad 2 del corte 2",
    "NoEa3c2": "no entregar la actividad 3 del corte 2",
    "NoEa4c2": "no entregar la actividad 4 del corte 2",
    "NoEpc2": "no entregar el parcial del corte 2",
    "Rcorte2": "retirarse en el corte 2",
    "RaM4,5c2": "tener un rendimiento alto mayor a 4,5 en el corte 2",
    "Rm3,5_4,4c2": "tener un rendimiento medio entre 3,5 y 4,4 en el corte 2",
    "Rb3,0_3,4c2": "tener un rendimiento bajo entre 3,0 y 3,4 en el corte 2",
    "Rp0_2,99c2": "estar reprobado entre 0 y 2,99 en el corte 2",

    #CORTE3
    "EATa1c3": "entregar a tiempo la actividad 1 del corte 3",
    "EATa2c3": "entregar a tiempo la actividad 2 del corte 3",
    "EATa3c3": "entregar a tiempo la actividad 3 del corte 3",
    "EATa4c3": "entregar a tiempo la actividad 4 del corte 3",
    "EATpc3":  "entregar a tiempo el parcial del corte 3",
    "EEXa1c3": "entregar extemporaneamente la actividad 1 del corte 3",
    "EEXa2c3": "entregar extemporaneamente la actividad 2 del corte 3",
    "EEXa3c3": "entregar extemporaneamente la actividad 3 del corte 3",
    "EEXa4c3": "entregar extemporaneamente la actividad 4 del corte 3",
    "EEXpc3": "entregar extemporaneamente el parcial del corte 3",
    "NoEa1c3": "no entregar la actividad 1 del corte 3",
    "NoEa2c3": "no entregar la actividad 2 del corte 3",
    "NoEa3c3": "no entregar la actividad 3 del corte 3",
    "NoEa4c3": "no entregar la actividad 4 del corte 3",
    "NoEpc3": "no entregar el parcial del corte 3",
    "Rcorte3": "retirarse en el corte 3",
    "Rpcorte3": "Reprobado del parcial del corte 3",
    "RaM4,5c3": "tener un rendimiento alto mayor a 4,5 en el corte 3",
    "Rm3,5_4,4c3": "tener un rendimiento medio entre 3,5 y 4,4 en el corte 3",
    "Rb3,0_3,4c3": "tener un rendimiento bajo entre 3,0 y 3,4 en el corte 3",
    "Rp0_2,99c3": "estar retirado entre 0 y 2,99 en el corte 3",
  }

  selected_value = request.form.get('init')
  display_text = select_options.get(selected_value, selected_value)

  select_options2 = {
  
    #CORTE 1
    "Start": "Inicio",
    "EATa1c1": "entregar a tiempo la actividad 1 del corte 1",
    "EATa2c1": "entregar a tiempo la actividad 2 del corte 1",
    "EATa3c1": "entregar a tiempo la actividad 3 del corte 1",
    "EATa4c1": "entregar a tiempo la actividad 4 del corte 1",
    "EATpc1": "entregar a tiempo el parcial del corte 1",
    "EEXa1c1": "entregar extemporaneamente la actividad 1 del corte 1",
    "EEXa2c1": "entregar extemporaneamente la actividad 2 del corte 1",
    "EEXa3c1": "entregar extemporaneamente la actividad 3 del corte 1",
    "EEXa4c1": "entregar extemporaneamente la actividad 4 del corte 1",
    "EEXpc1": "entregar extemporaneamente el parcial del corte 1",
    "NoEa1c1": "no entregar la actividad 1 del corte 1",
    "NoEa2c1": "no entregar la actividad 2 del corte 1",
    "NoEa3c1": "no entregar la actividad 3 del corte 1",
    "NoEa4c1": "no entregar la actividad 4 del corte 1",
    "NoEpc1": "no entregar el parcial del corte 1",
    "Rcorte1": "retirarse en el corte 1",
    "RaM4,5c1": "tener un rendimiento alto mayor a 4,5 en el corte 1",
    "Rm3,5_4,4c1": "tener un rendimiento medio entre 3,5 y 4,4 en el corte 1",
    "Rb3,0_3,4c1": "tener un rendimiento entre bajo 3,0 y 3,4 en el corte 1",
    "Rp0_2,99c1": "estar reprobado entre 0 y 2,99 en el corte 1",

    #CORTE2
    "EATa1c2": "entregar a tiempo la actividad 1 del corte 2",
    "EATa2c2": "entregar a tiempo la actividad 2 del corte 2",
    "EATa3c2": "entregar a tiempo la actividad 3 del corte 2",
    "EATa4c2": "entregar a tiempo la actividad 4 del corte 2",
    "EATpc2":  "entregar a tiempo el parcial del corte 2",
    "EEXa1c2": "entregar extemporaneamente la actividad 1 del corte 2",
    "EEXa2c2": "entregar extemporaneamente la actividad 2 del corte 2",
    "EEXa3c2": "entregar extemporaneamente la actividad 3 del corte 2",
    "EEXa4c2": "entregar extemporaneamente la actividad 4 del corte 2",
    "EEXpc2": "entregar extemporaneamente el parcial del corte 2",
    "NoEa1c2": "no entregar la actividad 1 del corte 2",
    "NoEa2c2": "no entregar la actividad 2 del corte 2",
    "NoEa3c2": "no entregar la actividad 3 del corte 2",
    "NoEa4c2": "no entregar la actividad 4 del corte 2",
    "NoEpc2": "no entregar el parcial del corte 2",
    "Rcorte2": "retirarse en el corte 2",
    "RaM4,5c2": "tener un rendimiento alto mayor a 4,5 en el corte 2",
    "Rm3,5_4,4c2": "tener un rendimiento medio entre 3,5 y 4,4 en el corte 2",
    "Rb3,0_3,4c2": "tener un rendimiento bajo entre 3,0 y 3,4 en el corte 2",
    "Rp0_2,99c2": "estar reprobado entre 0 y 2,99 en el corte 2",

    #CORTE3
    "EATa1c3": "entregar a tiempo la actividad 1 del corte 3",
    "EATa2c3": "entregar a tiempo la actividad 2 del corte 3",
    "EATa3c3": "entregar a tiempo la actividad 3 del corte 3",
    "EATa4c3": "entregar a tiempo la actividad 4 del corte 3",
    "EATpc3":  "entregar a tiempo el parcial del corte 3",
    "EEXa1c3": "entregar extemporaneamente la actividad 1 del corte 3",
    "EEXa2c3": "entregar extemporaneamente la actividad 2 del corte 3",
    "EEXa3c3": "entregar extemporaneamente la actividad 3 del corte 3",
    "EEXa4c3": "entregar extemporaneamente la actividad 4 del corte 3",
    "EEXpc3": "entregar extemporaneamente el parcial del corte 3",
    "NoEa1c3": "no entregar la actividad 1 del corte 3",
    "NoEa2c3": "no entregar la actividad 2 del corte 3",
    "NoEa3c3": "no entregar la actividad 3 del corte 3",
    "NoEa4c3": "no entregar la actividad 4 del corte 3",
    "NoEpc3": "no entregar el parcial del corte 3",
    "Rcorte3": "retirarse en el corte 3",
    "Rpcorte3": "Reprobado del parcial del corte 3",
    "RaM4,5c3": "tener un rendimiento alto mayor a 4,5 en el corte 3",
    "Rm3,5_4,4c3": "tener un rendimiento medio entre 3,5 y 4,4 en el corte 3",
    "Rb3,0_3,4c3": "tener un rendimiento bajo entre 3,0 y 3,4 en el corte 3",
    "Rp0_2,99c3": "estar retirado entre 0 y 2,99 en el corte 3",
    }

  selected_value2 = request.form.get('target')
  displaytext = select_options2.get(selected_value2, selected_value2)

  
  return render_template('showprediction.html', variable = resultado, init = display_text, target = displaytext)  


  



