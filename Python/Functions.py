import pandas as pd
import pymysql
import Functions as f
class FuncionesParaElTrabajito :
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
    #Borrado donde el id es : 
    def deleteDataWhereIDinVehiculos(connection,idCoche):    
        sql = "DELETE FROM sacarinosDB.vehiculos WHERE('%s')" % (idCoche)
        curr = connection.cursor()
        curr.execute(sql)
    #CONSULTA DE LA TABLA ESPAÑA : 
    def searchingINTOTHEDATABASE(connection) :
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
    
    def menu():
        print("Welcome to T-SACARINOS CONSULTING")
        menu_options = {
            1:"WATCH ALL THE DATA FROM THE TABLE SPAIN" ,
            2:"WATCH ALL THE DATA FROM THE TABLE  VEHICLES",
            3:"INTRODUCE DATA TO SPAIN",
            4:"INTRODUCE DATA TO VEHICLES",
            5:"WIPE OUT DATA FROM SPAIN WHERE ID",
            6: "WIPE OUT DATA FROM VEHICLES WHERE ID",
            7: "SEARCH DATA FROM VEHICLES WHERE ENROLLMENT(ID OF THE CAR)",
            8: "SEARCH DATA FROM SPAIN WHERE ENROLLMENT(ID OF THE CAR)"
        }
        def print_menu():
            for key in menu_options.keys():
                print (key, '--', menu_options[key] )
        if __name__=='__main__':
            while(True):
                print_menu()
                option = ''
                try:
                    option = int(input('Enter your choice: '))
                except:
                    print('Wrong input. Please enter a number ...')
                #Check what choice was entered and act accordingly
                if option == 1:
                    
                elif option == 2:
                    option2()
                elif option == 3:
                    option3()
                elif option == 4:
                    print('Thanks message before exiting')
                    exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 4.')
    
        choises={
           
        }
        for i in choises.keys(): # Loop to print all Choises and key of choise ! 
            print(f"{i} - {choises[i]}")
        arg=int(input("Pleasse Chose : "))
        R=choises.get(arg,-1)
        while R==-1:
            print("\n Wrong Choise ! Try again ....\n")
            menu()
        else:
            print(f"You Chosed {R}")
            if R==1:
                login()
            if R==2:
                register()   