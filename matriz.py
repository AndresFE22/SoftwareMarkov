from flask import Flask, render_template, request 
import numpy as np
import pandas as pd


# Carga la matriz de transición desde el archivo Excel
matriz_transicion = pd.read_excel('MATRIZL.xlsx', index_col=0)


print(matriz_transicion.iloc[:3, :3])



@app.route('/obtener_valor', methods=['POST'])
def obtener_valor():
    estado_origen = request.form['estado_origen']
    estado_destino = request.form['estado_destino']

    # Obtiene el valor correspondiente de la matriz de transición
    valor = matriz_transicion.loc[estado_origen, estado_destino]

    print(valor)  # imprime el valor en la consola

    return str(valor)



