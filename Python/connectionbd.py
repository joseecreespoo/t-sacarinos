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
            #Obtenemos un arraybidimnesional de las cosas del csv
            arrayConLasCositasXD = f.FuncionesParaElTrabajito.gettingCSV()
            f.FuncionesParaElTrabajito.extractDataFromArrayList(connection,arrayConLasCositasXD)
        except pymysql.Error as e:
               print("No se puede conectar a la base de datos")
        

        

       
           
      
       

            
