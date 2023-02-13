#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Laboratorio 1: Inversión de Capital                                                        -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: anamaria1404 y Galileatr                                                                    -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/anamaria1404/Laboratorio-I                                           -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
fig = make_subplots(specs = [[{"secondary_y" : False}]])
fig.add_trace(go.Scatter(x = df_pasiva.index, y = df_pasiva["Rend_Acum"], name = "Capital"), secondary_y = False,)
fig.update_layout(title = "Desempeño Estrategia Inversión", xaxis_title = "Fecha", yaxis_title = "MXN")
