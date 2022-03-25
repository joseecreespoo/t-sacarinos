from numpy import insert
import pymysql
import sys
import Functions as f
class connectionbd : 
        try:
            #database connection
            #Conectamos la base de datos a mi servidor local xamp
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="sacarinosDB")
            cursor = connection.cursor()
            # queries for inserting values
        except pymysql.Error as e:
                print("No se puede conectar a la base de datos")
                sys.exit(1)
        print("Conexión correcta con la base de datos")
        cursor = connection.cursor()
        arrayConLasCositasXD = f.FuncionesParaElTrabajito.gettingCSV()
        #Sacamos el id de Coche        
        idCoche = arrayConLasCositasXD['_id']
        tipoVehiculo = arrayConLasCositasXD['TIPO DE VEHÍCULO']
        cantidad = arrayConLasCositasXD['CANTIDAD']  
        
        
        def insertCsvToTheDatabse(cursor,idCoche,tipoVehiculo,cantidad) : 
            # queries for inserting values
            try :
                insert1 = "INSERT INTO sacarinosDB.españa (idCoche,tipoVehiculo,cantidad) VALUES ({idCoche},{tipoVehiculo},{cantidad})"
                #executing the quires
                cursor.execute(insert1)
                cursor.commit()
            except pymysql.Error as e : 
                sys.exit(1)
                print("ERROR")
                #commiting the connection then closing it.
                cursor.commit()
                cursor.close()
        insertCsvToTheDatabse(cursor,idCoche,tipoVehiculo,cantidad)
        
            
