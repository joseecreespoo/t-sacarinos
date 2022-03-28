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
        
        s=""  
        t=0
        for fila1 in dato:
            print (fila1)
            if (isinstance(fila1, str)):
                print("CADENA",type(fila1))
                s+= " ' "+ fila1 + "'" + ","
                dato = s
            else:
                print("INT",type(fila1))
                t+= "'"+ fila1 + "'" + ","
                dato = t
        print (dato)  
        return dato
       
            
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
        