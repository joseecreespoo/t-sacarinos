import pandas as pd
import pymysql
import Functions as f
class FuncionesParaElTrabajito :
    def insertCsvToTheDatabse(connection,idCoche,tipoVehiculo,cantidad) : 
        # queries for inserting values
        try :
            print(idCoche)
            print(tipoVehiculo)
            print(cantidad)
            insert1 = ("INSERT INTO sacarinosDB.espana (id,tipoVehiculo,cantidad) VALUES ('%s','%s','%s')" % (idCoche,tipoVehiculo,cantidad))
            #executing the quires
            curr = connection.cursor()
            curr.execute(insert1)
            connection.commit()

        except pymysql.Error as e : 
            print("ERROR AL INSERTAR")
            #commiting the connection then closing it.
            connection.commit()
        print("Introduccion correcta con la base de datos")  
    #Funcion para coger los datos del csv que devuelve el objeto df "Es el array  bidimensional del csv "
    def  gettingCSV():
        #Leemos el csv para utilizar la librería pandas que lo convierte en tabla
        df = pd.read_csv("../t-sacarinos/Python/vehiculos-2021.csv")
        ##Devolvemos el array bidimensional
        return df
    def  extractDataFromArrayList(cursor,arrayconlasCosas) :
       tuples = [tuple(x) for x in arrayconlasCosas.values]
       for each in tuples:
            f.FuncionesParaElTrabajito.insertCsvToTheDatabse(cursor,each[0],str(each[1]),each[2])
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
        