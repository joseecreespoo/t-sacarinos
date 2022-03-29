import pandas as pd
import pymysql
import Functions as f
class FuncionesParaElTrabajito : 
 
    ##################################
    # OBTENER, LIMPIAR E INSERTAR DATOS DEL CSV EN LA BASE DE DATOS
    ##################################    
        
        
    #Funcion para coger los datos del csv que devuelve el objeto df
    def  gettingCSV():
        #Leemos el csv para utilizar la librería pandas que lo convierte en tabla
        df = pd.read_csv("../t-sacarinos/Python/vehiculos-2021.csv")
        ##Devolvemos el array bidimensional
        return df
    
    

    
    #Limpiar los datos de la lista y sacamos esos datos en tuplas
    def  extractDataFromArrayList(cursor,arrayconlasCosas) :
       tuples = [tuple(x) for x in arrayconlasCosas.values]
       for each in tuples:
            f.FuncionesParaElTrabajito.insertCsvToTheDatabse(cursor,each[0],str(each[1]),each[2])
            
            
    #FUNCION QUE INSERTA EL CSV EN LA DATABASE
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
        
        
        
    ################################################################################################
    
    
    
    ##################################
    # FUNCIONES PARA INSERTAR, CONSULTAR .... 
    ##################################  
    
    
    #DEVUELVE TODOS LOS IDS QUE HAY EN LA TABLA
    def searchCarIDS (connection):
        try :
            select1 = "SELECT  matricula FROM sacarinosDB.vehiculos"
            #executing the quires
            curr = connection.cursor()
            curr.execute(select1)
            rows = curr.fetchall()
            for row in rows:
                print(row)   
            connection.commit()
        except pymysql.Error as e : 
            print("ERROR AL BUSCAR")
            #commiting the connection then closing it.
            connection.commit()
        print("Busqueda correcta con la base de datos") 
        
        
        
        
    #MUESTRA ID Y TIPO DE VEHICULO DENTRO DE LA TABLA ESPAÑA
    def searchtipoVehiculo(connection) :
        try :
            select1 = "SELECT id,tipoVehiculo FROM sacarinosDB.espana"
            #executing the quires
            curr = connection.cursor()
            curr.execute(select1)
            rows = curr.fetchall()
            for row in rows:
                print(row)   
            connection.commit()
        except pymysql.Error as e : 
            print("ERROR AL BUSCAR")
            #commiting the connection then closing it.
            connection.commit()
        print("Busqueda correcta con la base de datos")
    
    
    # INSERTAR VEHICULOS EN BASE DE DATOS
    
    def insertVehiclesToTheDatabse(connection,marca,modelo,matricula,tipoVehiculo) : 
        # queries for inserting values
        try :
            print(marca)
            print(modelo)
            print(matricula)
            print(tipoVehiculo)
            
            insert1 = ("INSERT INTO sacarinosDB.vehiculos(marca,modelo,matricula,tipoVehiculo)  VALUES ('%s','%s','%s','%s')" % (marca,modelo,matricula,tipoVehiculo))
            #executing the quires
            curr = connection.cursor()
            curr.execute(insert1)
            connection.commit()
        except pymysql.Error as e : 
            print(e)
            print("ERROR AL INSERTAR")
            #commiting the connection then closing it.
            connection.commit()
        print("Introduccion correcta con la base de datos")  
    
          
          
          
          
    #ELIMINA MATRICULA PASADA POR PARAMETRO:
    def deleteDataWhereIDinVehiculos(connection,matricula):
        try :    
            sql = f"DELETE FROM sacarinosDB.vehiculos WHERE matricula = ' {matricula} ' "
            curr = connection.cursor()
            curr.execute(sql)
            connection.commit()
        except pymysql.Error as e : 
            print(e)
        print("BORRADO correcto con la base de datos")
            
        
        
        
        
    #CONSULTA DE LA TABLA ESPAÑA : 
    def searchingINTOTHEDATABASESPAIN(connection) :
        try :
            select1 = "SELECT * FROM sacarinosDB.espana"
            #executing the quires
            curr = connection.cursor()
            curr.execute(select1)
            rows = curr.fetchall()
            for row in rows:
                print(row)   
            connection.commit()
        except pymysql.Error as e : 
            print("ERROR AL BUSCAR")
            #commiting the connection then closing it.
            connection.commit()
        print("Busqueda correcta con la base de datos")
        
        
        
        
     #CONSULTA DE LA TABLA VEHICULOS : 
    def searchingIDINTOTHEDATABASESPAIN(connection,idVehiculo) :
        try :
            select1 = "SELECT * FROM sacarinosDB.vehiculos where (matricula) = ('%s')" % (idVehiculo)
            #executing the quires
            curr = connection.cursor()
            curr.execute(select1)
            rows = curr.fetchall()
            for row in rows:
                print(row)   
            connection.commit()
        except pymysql.Error as e : 
            print("ERROR AL BUSCAR")
            #commiting the connection then closing it.
            connection.commit()
        print("Busqueda correcta con la base de datos")
        
        
        
 
        
        
    #MUESTRA TODOS LOS VEHICULOS EN LA TABLA VEHICULOS
 
    def searchingINTOTHEDATABASEVEHICLES(connection) :
        try :
            select1 = "SELECT * FROM sacarinosDB.vehiculos"
            #executing the quires
            curr = connection.cursor()
            curr.execute(select1)
            rows = curr.fetchall()
            for row in rows:
                print(row)   
            connection.commit()
        except pymysql.Error as e : 
            print("ERROR AL BUSCAR")
            #commiting the connection then closing it.
            connection.commit()
        print("Busqueda correcta con la base de datos")
        
          

    
    
    ###########################
    # MENU
    ###########################
    
    
    
    def menu(connection,menu_options):
      while(True):
        print("Welcome to T-SACARINOS CONSULTING")
        for key in menu_options.keys():
            print (key, '--', menu_options[key] )
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            f.FuncionesParaElTrabajito.searchingINTOTHEDATABASESPAIN(connection)
        elif option == 2:
            f.FuncionesParaElTrabajito.searchingINTOTHEDATABASEVEHICLES(connection)
        elif option == 3:
            marca = input("GIVE ME THE CAR BRAND: ")
            modelo = input("GIVE ME THE CAR MODEL: ")
            matricula = input("GIVE ME THE ENROLLMENT(INTRODUCE THE ID): ")
            print("----------------------------------------------")
            FuncionesParaElTrabajito.searchtipoVehiculo(connection)
            print("----------------------------------------------")
            tipoVehiculo = input("INTRODUCE THE TYPE OF CAR : ")    
            f.FuncionesParaElTrabajito.insertVehiclesToTheDatabse(connection,marca,modelo,matricula,tipoVehiculo)
        elif option == 4:
            FuncionesParaElTrabajito.searchCarIDS(connection)
            matricula = input("GIVE ME THE CAR ID: ")
            FuncionesParaElTrabajito.deleteDataWhereIDinVehiculos(connection,matricula)
        elif option == 5:
            matricula = input("GIVE ME THE CAR ID: ")
            FuncionesParaElTrabajito.searchingIDINTOTHEDATABASESPAIN(connection,matricula)
        elif option == 6:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 9.')
    
      



#################################COMPROBAR#######################################################        
    def searchingTypesOfVehicles(connection,tipodeVehiculo) :
        try :
            select1 = "SELECT * FROM sacarinosDB.espana,sacarinosDB.vehiculos where tipoVehiculo = ('%s') " % (tipodeVehiculo)
            #executing the quires
            curr = connection.cursor()
            curr.execute(select1)
            rows = curr.fetchall()
            for row in rows:
                print(row)   
            connection.commit()
        except pymysql.Error as e : 
            print("ERROR AL BUSCAR")
            #commiting the connection then closing it.
            connection.commit()
        print("Busqueda correcta con la base de datos") 
###############################################################################################    