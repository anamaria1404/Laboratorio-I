# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 08:17:04 2023

@author: HP
"""

import functions as fn
from data import df

#iloc[fila,columna] (texto)
#loc[fila,coliumna] (número > posición)
df.loc[:,'mean_1'] = fn.remove_mean(df.iloc[:,0])
df.loc[:,'add_value'] = fn.add_number(df.iloc[:,0], 3)

