import pandas as pd
import pymysql
class FuncionesParaElTrabajito :
    #Funcion para coger los datos del csv que devuelve el objeto df "Es el array  bidimensional del csv "
    def  gettingCSV():
        #Leemos el csv para utilizar la librería pandas que lo convierte en tabla
        df = pd.read_csv("../t-sacarinos/Python/vehiculos-2021.csv")
        ##Devolvemos el array bidimensional
        return df
    def  extractDataFromArrayList(dato) :
        for fila in dato :
            print(fila)
        return fila
 
       
            
    def insertCsvToTheDatabse(cursor,idCoche,tipoVehiculo,cantidad) : 
        # queries for inserting values
        try :
            insert1 = f"INSERT INTO sacarinosDB.espana (idCoche,tipoVehiculo,cantidad) VALUES ({idCoche},{tipoVehiculo},{cantidad})"
            #executing the quires
            cursor.execute(insert1)
            cursor.commit()
            cursor.close()
        except pymysql.Error as e : 
            print("ERROR AL INSERTAR")
            #commiting the connection then closing it.
            cursor.commit()
            cursor.close()
        print("Introduccion correcta con la base de datos")  
    def searchingINTOTHEDATABASE(cursor) :
        try :
            select1 = f"SELECT * FROM sacarinosDB.españa"
            #executing the quires
            cursor.execute(select1)
            rows = cursor.fetchall()
            for row in rows:
                print(row)   
            cursor.commit()
        except pymysql.Error as e : 
            print("ERROR AL BUSCAR")
            #commiting the connection then closing it.
            cursor.commit()
        print("Busqueda correcta con la base de datos")
        