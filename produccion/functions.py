import json
import pymysql
from simplejson import JSONEncoder

            ##ESTO SE HACE SOLO 1 VEZ QUE ES PARA METER EL CSV EN LA TABLA ESPAÑA
            #Obtenemos un arraybidimnesional de las cosas del csv
            ##arrayConLasCositasXD = f.FuncionesParaElTrabajito.gettingCSV()
            ##f.FuncionesParaElTrabajito.extractDataFromArrayList(connection,arrayConLasCositasXD)  
   


    
##################################
# FUNCIONES PARA INSERTAR, CONSULTAR .... 
##################################  




def searhTypes (connection):
    try :
        #preparamos la query y la ejecutamos
        
        select1 = "SELECT * FROM sacarinosDB.tiposVehiculos"
        curr = connection.cursor()
        curr.execute(select1)
        rows = curr.fetchall()
        
        #creamos una lista en la que guardaremos los coches obtenidos de la query
        listaTipos = []
        
        #añadimos todos los resultados con estructura json
        for row in rows:
            x = '{"id":',row[0],',"tipoVehiculo":',row[1],'}'
            listaTipos.append(x)
        connection.commit()
        
        #devolvemos el array de json
        print(json.dumps(listaTipos))

        return(json.dumps(listaTipos))
        
    #en caso de que haya error lo mostramos
    
    except pymysql.Error as e : 
        
        connection.commit()
        return("Error al buscar, error: ",e)


#DEVUELVE todo lo QUE HAY EN LA TABLA

def searchCarIDS (connection):
    try :
        
        #preparamos la query y la ejecutamos
        
        select1 = "SELECT * FROM `vehiculos`"
        curr = connection.cursor()
        curr.execute(select1)
        rows = curr.fetchall()
        
        #creamos una lista en la que guardaremos los coches obtenidos de la query
        listaCoches = []
        
        #añadimos todos los resultados con estructura json
        for row in rows:
            x = '{"id":',row[0],',"marca":',row[1],',"modelo":',row[2],',"matricula":',row[3],',"tipoCoche":',row[4],'}'
            listaCoches.append(x)
        connection.commit()
        
        #devolvemos el array de json
        print(json.dumps(listaCoches))

        return(json.dumps(listaCoches))
        
    #en caso de que haya error lo mostramos
    
    except pymysql.Error as e : 
        
        connection.commit()
        return("Error al buscar, error: ",e)
        
    



        
 #CONSULTA DE LA TABLA VEHICULOS PASANDO MATRICULA POR PARAMETRO : 
def searchingMatricula(connection,matricula) :
    try :
        #preparamos la query y la ejecutamos
        select1 = f"SELECT * FROM sacarinosDB.vehiculos WHERE matricula = ('{matricula}')"
        curr = connection.cursor()
        curr.execute(select1)  
        rows = curr.fetchall()
        
        
        #añadimos todos los resultados con estructura json
        for row in rows:
            
            x = '{"id":',row[0],',"marca":',row[1],',"modelo":',row[2],',"matricula":',row[3],',"tipoCoche":',row[4],'}'
            return(json.dumps(x)) 
         
        connection.commit()
        
    #en caso de que haya error lo mostramos
    
    except pymysql.Error as e : 
        
        connection.commit()
        return(print("Error al buscar o la matricula no se encuentra. Error: ",e))

        

# INSERTAR VEHICULOS EN BASE DE DATOS

def insertVehicle(connection,marca,modelo,matricula,tipoVehiculo) : 
    try :
        #preparamos la query y la ejecutamos
        insert1 = f"INSERT INTO sacarinosDB.vehiculos(marca,modelo,matricula,tipoVehiculo)  VALUES ('{marca}','{modelo}','{matricula}','{tipoVehiculo}')"
        curr = connection.cursor()
        curr.execute(insert1)
        connection.commit()
        
        #devolvemos que se haya insertado correctamente
        
        return(print("Datos insertados correctamente"))
    
    
    #en caso de que haya error lo mostramos    
        
    except pymysql.Error as e : 
        
        connection.commit()
        return(print("Error al insertar. Error: ",e))


#ELIMINA MATRICULA PASADA POR PARAMETRO:


def deleteVehicle(connection,matricula): 
       
    try:
        #preparamos la query y la ejecutamos
        
        delete1 = f"DELETE FROM sacarinosDB.vehiculos WHERE matricula = '{matricula}'"
        curr = connection.cursor()
        curr.execute(delete1)
        connection.commit()
        
        #devolvemos que se han eliminado correctamente
        
        return(print("Datos eliminados correctamente"))
        
    #en caso de que haya error lo mostramos
    except pymysql.Error as e :
        
        connection.commit()
        return(print("Error al eliminar. Error: ",e))
    
      
      
#MODIFICA VEHICULO POR ID:

def modifyVehicle(connection,id,marcaNueva,modeloNuevo,matriculaNueva,tipoVehiculoNuevo): 
       
    try:
        #preparamos la query y la ejecutamos
        update1 = f"UPDATE sacarinosDB.vehiculos SET marca = '{marcaNueva}', modelo = '{modeloNuevo}', matricula = '{matriculaNueva}', tipoVehiculo = '{tipoVehiculoNuevo}' WHERE idcoches = {id}"
        curr = connection.cursor()
        curr.execute(update1)
        connection.commit()
        
        #devolvemos que se han eliminado correctamente
        
        return(print("Datos modificados correctamente"))
        
    #en caso de que haya error lo mostramos
    except pymysql.Error as e :
        
        connection.commit()
        return(print("Error al modificar. Error: ",e))