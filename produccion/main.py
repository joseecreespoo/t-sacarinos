from fastapi import FastAPI
from functions import *
import pymysql

#############
##CONEXION BD
#############

try:
    #database connection
    #Conectamos la base de datos a mi servidor local
    connection = pymysql.connect(host="localhost", user="josecrespo", passwd="josecrespo", database="sacarinosDB")
    cursor = connection.cursor()

    print("Se ha conectado correctamente a la base de datos")
    
except pymysql.Error as e:
    
    print("No se puede conectar a la base de datos, error: ",e)
    




#creamos la api
app = FastAPI()


#implementamos el metodo get para obtener la información a traves de una peticion get
#nos devuelve toda la informacion de la tabla de clasificaciones

@app.get("/obtenerTiposVehiculos")

def obtenerTipos():
    return searhTypes(connection)

#implementamos el metodo get para obtener la información a traves de una peticion get
#nos devuelve toda la informacion sin filtrar

@app.get("/obtenerInformacion")

def obtenerTodaInformacion():
    return searchCarIDS(connection)


#implementamos el metodo get para obtener la información a traves de una peticion get
#nos devuelve toda la informacion filtrada

@app.get("/obtenerInformacion/{matricula}")

def obtenerInformacionPorMatricula(matricula):

    return searchingMatricula(connection,matricula)


#implementamos el metodo post para pasar la información
#nos añade la informacion requerida a la base de datos


@app.post("/añadirInformacion/{marca}-{modelo}-{matricula}-{tipoVehiculo}")

def añadirInformacionVehiculos(marca,modelo,matricula,tipoVehiculo):
    
    return insertVehicle(connection,marca,modelo,matricula,tipoVehiculo)
    

#implementamos el metodo post para eliminar el vehiculo
#nos elimina el vehiculo que tiene la matricula pasada por parametro


@app.post("/eliminarVehiculo/{matricula}")

def eliminarVehiculo(matricula):
    
    return deleteVehicle(connection,matricula)



#implementamos el metodo post para modificar el vehiculo
#nos modifica todos los parametros de un vehiculo con matricula pasada por parametro


@app.post("/modificarVehiculo/{idVehiculo}/{marcaNueva}-{modeloNuevo}-{matriculaNueva}-{tipoVehiculoNuevo}")

def modificarVehiculo(id,marcaNueva,modeloNuevo,matriculaNueva,tipoVehiculoNuevo):
    
    return modifyVehicle(connection,id,marcaNueva,modeloNuevo,matriculaNueva,tipoVehiculoNuevo)
    
