import pandas as pd
import yfinance as yf
import streamlit as st

# para para descargar los datos y limpiarlos
def obtener_precios_activos(symbol, start_date, end_date):
    df = yf.download(symbol, start=start_date, end=end_date)
    df = df[['Adj Close']].dropna()
    return df

# inputs
symbol = st.text_input("Ingrese el símbolo del activo: ")
start_date = st.text_input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
end_date = st.text_input("Ingrese la fecha de fin (YYYY-MM-DD): ")

if st.button("Buscar"):
    #df = yf.download(symbol, start=start_date, end=end_date)
    #precios = df[['Adj Close']].dropna()
    precios = yf.Ticker(symbol).history(start=start_date, end=end_date)

    # - accurate time-series count:
    #precios = ticker.history(start=start_date, end=end_date)

    st.write(precios)
    
    #Mostrar los primeros 5 y los últimos 5 datos
    primeros_5 = precios.head(5)
    ultimos_5 = precios.tail(5)
    
    # Mostrar los resultados
    st.write("\nPrimeros 5 datos:")
    st.write(primeros_5)

    st.write("\nÚltimos 5 datos:")
    st.write(ultimos_5)

    def encontrar_mejor_momento(precios):
    max_rendimiento = 0
    dia_compra = None
    dia_venta = None
    precio_compra = 0
    precio_venta = 0
    
    for i in range(len(precios)):
        for j in range(i + 1, len(precios)):
            rendimiento = (precios.iloc[j]['Adj Close'] - precios.iloc[i]['Adj Close']) / precios.iloc[i]['Adj Close']
            
            if rendimiento > max_rendimiento:
                max_rendimiento = rendimiento
                dia_compra = precios.index[i]
                dia_venta = precios.index[j]
                precio_compra = precios.iloc[i]['Adj Close']
                precio_venta = precios.iloc[j]['Adj Close']
    
    return dia_compra, dia_venta, precio_compra, precio_venta, max_rendimiento

# Obtener los precios y limpiar la base de datos
precios = obtener_precios_activos(symbol, start_date, end_date)

# Encontrar el mejor momento para comprar y vender
dia_compra, dia_venta, precio_compra, precio_venta, rendimiento = encontrar_mejor_momento(precios)

# Mostrar los resultados
if dia_compra is None or dia_venta is None:
    print("No se pudo generar rendimiento positivo en el período especificado.")
else:
    st.write("Día de Compra:", dia_compra)
    st.write("Día de Venta:", dia_venta)
    st.write("Precio de Compra:", precio_compra)
    st.write("Precio de Venta:", precio_venta)
    st.write("Rendimiento (%):", rendimiento * 100)
    st.write("Rendimiento ($):", (precio_venta - precio_compra) * 100, "comprando 100 acciones.")
