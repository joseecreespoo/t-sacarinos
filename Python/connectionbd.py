from numpy import insert
import pymysql
import sys
import Functions as f
class connectionbd : 
        #Obtenemos un arraybidimnesional de las cosas del csv
        arrayConLasCositasXD = f.FuncionesParaElTrabajito.gettingCSV()
        #Sacamos el id de Coche y los demas atributos a utilizar sin limpiar ya que obtenemos un dato DATAFRAME
        idCocheNoClean = arrayConLasCositasXD['_id'].to_list()
        tipoVehiculoNoClean = arrayConLasCositasXD['TIPO DE VEHÍCULO'].to_list()
        cantidadNoClean = arrayConLasCositasXD['CANTIDAD'].to_list()
        try:
            #database connection
            #Conectamos la base de datos a mi servidor local xamp
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="sacarinosDB")
            cursor = connection.cursor()
            try:
                #LIMPIAMOS LOS DATOS
                idCoche = f.FuncionesParaElTrabajito.extractDataFromArrayList(idCocheNoClean)
                print ("----------")
                tipoVehiculo =  f.FuncionesParaElTrabajito.extractDataFromArrayList(tipoVehiculoNoClean)
                print ("----------")
                cantidad =  f.FuncionesParaElTrabajito.extractDataFromArrayList(cantidadNoClean)
                print ("----------")
                f.FuncionesParaElTrabajito.insertCsvToTheDatabse(cursor,idCoche,tipoVehiculo,cantidad)
            except pymysql.Error as e:
                    print("Ninguna de las dos") 
            
        except pymysql.Error as e:
                print("No se puede conectar a la base de datos")
        print("Conexión correcta con la base de datos")
        

        

       
           
      
       

            
