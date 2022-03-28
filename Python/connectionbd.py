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
            ##ESTO SE HACE SOLO 1 VEZ QUE ES PARA METER EL CSV EN LA TABLA ESPAÑA
            #Obtenemos un arraybidimnesional de las cosas del csv
            ##arrayConLasCositasXD = f.FuncionesParaElTrabajito.gettingCSV()
            ##f.FuncionesParaElTrabajito.extractDataFromArrayList(connection,arrayConLasCositasXD)
            menu_options = {
                1:"WATCH ALL THE DATA FROM THE TABLE SPAIN" ,
                2:"WATCH ALL THE DATA FROM THE TABLE  VEHICLES",
                3:"INTRODUCE DATA TO VEHICLES",
                4: "WIPE OUT DATA FROM VEHICLES WHERE ID",
                5: "SEARCH DATA FROM VEHICLES WHERE ENROLLMENT(ID OF THE CAR)",
                6: "EXIT",
            }
            f.FuncionesParaElTrabajito.menu(connection,menu_options)

 
        except pymysql.Error as e:
               print("No se puede conectar a la base de datos")
        print("Se conectó")
        

        

       
           
      
       

            
