import pandas as pd
 #Leemos el csv para utilizar la librería pandas que lo convierte en tabla
df = pd.read_csv("vehiculos-2021.csv")
#iMPRIMIMOS LA TABLAS
print(df)
#Sacamos cada dato de la tabla y lo metemos en las diferentes variables
id= df["_id"]
tipoVehiculo= df["TIPO DE VEHÍCULO"]
cantidad = df["CANTIDAD"]







