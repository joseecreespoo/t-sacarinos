import pandas as pd

class FuncionesParaElTrabajito :
    #Funcion para coger los datos del csv que devuelve el objeto df "Es el array  bidimensional del csv "
    def  gettingCSV():
        #Leemos el csv para utilizar la librería pandas que lo convierte en tabla
        df = pd.read_csv("../t-sacarinos/Python/vehiculos-2021.csv")
        ##Devolvemos el array bidimensional
        return df
    print (gettingCSV())
    lista= gettingCSV
    