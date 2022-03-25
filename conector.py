from re import L
import sys 
import MySQLdb
class connection:
    
    try:
        conn = MySQLdb.connect("locahost","root","","sacarinosDB")

    except MySQLdb.Error as e:
        print("No se puede conectar a la base de datos")
        sys.exit(1)
    print("Conexión correcta con la base de datos")
    
    cursor = conn.cursor()

    
    
#crear registros 

def insertData(idCoche,marca,modelo,matricula,tipoVehiculo):
    
    sql = f"INSERT INTO sacarinosDB.vehiculos (idcoches,marca,modelo,matricula,tipoVehiculo) VALUES ({idCoche},{marca},{modelo},{matricula},{tipoVehiculo})"
    
    connection.cursor.execute(sql)
    
    data = connection.cursor.fetchall()
    
    connection.cursor.close()
    connection.conn.close()
    
    return data
    
    
    #return print("La inserción se ha ejecutado con éxito")

#editar registros

def updateData(idCoche,marca,modelo,matricula,tipoVehiculo):
    
    
    
    sql = f"UPDATE sacarinosDB.vehiculos SET marca={marca},modelo={modelo},matricula={matricula},tipoVehiculo={tipoVehiculo} WHERE idcoches={idCoche}"


#eliminar registros

def deleteData(idCoche):
    
    sql = f"DELETE FROM sacarinosDB.vehiculos WHERE idcoches={idCoche}"

#buscar registros

def searchData(matricula):
    
    sql = f"SELECT * FROM sacrinosDB.vehiculos WHERE {matricula}"






