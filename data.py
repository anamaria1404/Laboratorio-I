# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 08:01:52 2023

@author: HP
"""

from sklearn.datasets import load_iris
import pandas as pd

df = pd.DataFrame(load_iris().data)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
print(df)

