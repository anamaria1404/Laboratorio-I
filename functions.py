#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Laboratorio 1: Inversión de Capital                                                        -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: anamaria1404 y Galileatr                                                                    -- #
# -- license:                                                                                            -- #
# -- repository: https://github.com/anamaria1404/Laboratorio-I                                           -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
#Función para limpiar tickets
def replace_text(x, to_replace, replacement):
        try:
            x=x.replace(to_replace, replacement)
        except:
            pass
        return x
    

# Función para descargar precios de cierre ajustados:
def get_adj_closes(tickers, start_date, end_date):
    # Descargamos DataFrame con todos los datos
    closes = yf.download(tickers = tickers,start=start_date,end=end_date)['Adj Close']
    closes.reset_index(inplace = True)
    closes = closes.groupby([closes["Date"].dt.year, closes["Date"].dt.month], as_index=False).last()
    # Se ordenan los índices de manera ascendente
    closes.sort_index(inplace=True)
    closes.set_index("Date", inplace = True)
    return closes

# Función para obtener rendimientos en inv pasiva
def pasiva( tickers,precios,capital, comision):
    
    tabla = pd.DataFrame(index = precios.columns, columns = ["Títulos", "Comisión","Costo Total","Ponderación"]) 
    
    for ticker in precios.columns:
        tabla.at[ticker, "Títulos"] = np.floor((capital*tickers[ticker].values[0])/(precios[ticker][0]*(1 + comision)))
        tabla.at[ticker, "Comisión"] = tabla.loc[ticker, "Títulos"]*precios[ticker][0]*comision
        tabla.at[ticker, "Costo Total"] = tabla.loc[ticker, "Títulos"]*precios[ticker][0]*(1 + comision)
        tabla.at[ticker, "Ponderación"] = (tabla.loc[ticker, "Títulos"]*precios[ticker][0])/capital
     
    df_pasiva = pd.DataFrame(index = precios.index, columns = ["Capital", "Rend","Rend_Acum"])
    
    df_pasiva["Capital"] = np.dot(precios * (1 - comision), tabla["Títulos"])
    df_pasiva["Rend"] = df_pasiva["Capital"].pct_change().dropna()
    df_pasiva["Rend_Acum"] = (df_pasiva["Rend"] + 1).cumprod() - 1 
    
    return tabla, df_pasiva

# Función para obtener metricas
def metricas(df_pasiva, rf):
    
    df_medidas = pd.DataFrame(index = ["rend_m", "rend_c", "sharpe"], columns = ["descripcion", "inv_pasiva"])
    df_medidas.loc["rend_m", "descripcion"] = "Rendimiento Promedio Mensual"
    df_medidas.loc["rend_c", "descripcion"] = "Rendimiento mensual acumulado"
    df_medidas.loc["sharpe", "descripcion"] = "Sharpe Ratio"
    
    df_medidas.loc["rend_m","inv_pasiva"] = df_pasiva["Rend"].dropna().mean()
    df_medidas.loc["rend_c","inv_pasiva"] = df_pasiva["Rend_Acum"][-1]
    df_medidas.loc["sharpe","inv_pasiva"] = (df_pasiva["Rend"].dropna().mean()-rf)/df_pasiva["Rend"].dropna().std() 

    return df_medidas 