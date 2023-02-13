# -*- coding: utf-8 -*-


"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Laboratorio 1: Inversión de Capital                                                        -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: anamaria1404 y Galileatr                                                                    -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/anamaria1404/Laboratorio-I                                           -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import data
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
pd.set_option('display.float_format', lambda x: '%.4f' % x)


# obtener tickers repetidos
cant = vertical_concat.groupby(['Ticker'])['Ticker'].count().to_frame()
cant24 = cant[cant['Ticker'] == 25] #tickers repetidos 25 veces

#pesos del mes 1
pesos1 = df[['Ticker','Peso (%)']]

pesos1["Peso (%)"] = pesos1["Peso (%)"] / 100

pesos1 = pesos1.drop(37) #eliminar última fila vacía


#pesos del mes 1
pesos1.Ticker = pesos1.Ticker.apply(replace_text, args=('*',''))
pesos1.Ticker = pesos1.Ticker.apply(replace_text, args=(".", "-"))
pesos1.Ticker = pesos1.Ticker + '.MX'
pesos1.set_index("Ticker", inplace = True)
pesos1=pesos1.T
pesos1.drop(['MXN.MX','GENTERA.MX','IENOVA.MX','LABB.MX','NMKA.MX','SITESB-1.MX'],axis=1, inplace=True) #eliminar MXN y no repetidas


#tickers limpieza 
t = pd.DataFrame(cant24.index)
t.Ticker = t.Ticker.apply(replace_text, args=('*',''))
t.Ticker = t.Ticker.apply(replace_text, args=(".", "-"))
t.Ticker = t.Ticker + '.MX'
t=t.drop(23,axis=0) #Eliminamos MXN

# Importar datos
names = t.Ticker.values.tolist()
start = '2021-01-31'
end = '2023-01-25'

# Obtener precios mensuales
closes = get_adj_closes(tickers=names, start_date=start, end_date=end)

tabla, df_pasiva = pasiva(pesos1,closes,1000000,0.00125)