pip install streamlit
#streamlit hello
import pandas as pd
import yfinance as yf

# para para descargar los datos y limpiarlos
def obtener_precios_activos(symbol, start_date, end_date):
    df = yf.download(symbol, start=start_date, end=end_date)
    df = df[['Adj Close']].dropna()
    return df

# inputs
symbol = input("Ingrese el símbolo del activo: ")
start_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
end_date = input("Ingrese la fecha de fin (YYYY-MM-DD): ")

# Obtener los precios y limpiar la base de datos
precios = obtener_precios_activos(symbol, start_date, end_date)

# Mostrar los primeros 5 y los últimos 5 datos
primeros_5 = precios.head(5)
ultimos_5 = precios.tail(5)

# Mostrar los resultados
st.write("\nPrimeros 5 datos:")
st.write(primeros_5)

st.write("\nÚltimos 5 datos:")
st.write(ultimos_5)
