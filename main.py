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

# obtener tickers repetidos
cant = vertical_concat.groupby(['Ticker'])['Ticker'].count().to_frame()
cant24 = cant[cant['Ticker'] == 25] #tickers repetidos 25 veces

#pesos del mes 1
pesos1 = df[['Ticker','Peso (%)']]
pesos1 = pesos1.loc[pesos1['Ticker'].isin((cant24.index))].set_index('Ticker')
pesos1["Peso (%)"] = df["Peso (%)"] / 100
pesos1["Ticker"] = [pesos1["Ticker"].replace(".", "-").replace("*", "") + ".MX" for i in list(pesos1["Ticker"])


def passive(naftrac_date = 20210129, capital = 1000000, comission = 0.00125):
    
    df, naftrac_date = data.file_reading(naftrac_date = naftrac_date)
    df = data.data_wrangling(df)
    fig1, fig2 = visualizations.pie_chart(df)
    

    df["Ticker"] = [stock.replace(".", "-").replace("*", "") + ".MX" for stock in list(df["Ticker"])]
    
    df_passive, fig3, df_metrics = functions.passive_investment_strategy(df, naftrac_date, capital, comission, 
                                                         "Passive Investment Strategy: NAFTRAC")    
    
    return df_passive, df_metrics, fig1, fig2, fig3
