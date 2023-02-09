# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 08:17:04 2023

@author: HP
"""

"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Laboratorio 1: Inversión de Capital                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: anamaria1404 y Galileatr                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/anamaria1404/Laboratorio-I                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

def passive(naftrac_date = 20210129, capital = 1000000, comission = 0.00125):
    
    df, naftrac_date = data.file_reading(naftrac_date = naftrac_date)
    df = data.data_wrangling(df)
    fig1, fig2 = visualizations.pie_chart(df)
    
    df["Peso (%)"] = df["Peso (%)"] / 100
    [df.drop(labels = i, axis = 0, inplace = True) for i in range(len(df)) if df["Ticker"][i] in ["KOFL", "KOFUBL", "MXN", "BSMXB", "NMKA"]];
    df.reset_index(drop = True, inplace = True)
    df["Ticker"] = [stock.replace(".", "-").replace("*", "") + ".MX" for stock in list(df["Ticker"])]
    
    df_passive, fig3, df_metrics = functions.passive_investment_strategy(df, naftrac_date, capital, comission, 
                                                         "Passive Investment Strategy: NAFTRAC")    
    
    return df_passive, df_metrics, fig1, fig2, fig3
