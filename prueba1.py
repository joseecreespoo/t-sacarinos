import sys
import MySQLdb


try:
    conn = MySQLdb.connect("192.168.1.186","root","tsystems","sacarinosDB")

except MySQLdb.Error as e:
    print("No se puede conectar a la base de datos")
    print(e)
    sys.exit(1)
print("Conexión correcta con la base de datos")


sql="select * from sacarinosDB.vehiculos"
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

try:
    
   cursor.execute(sql)
   registro = cursor.fetchone()
   
   while registro:
       
      print(registro["matricula"],registro["idcoches"])
      registro = cursor.fetchone()
      
except:
   print("Error en la consulta")
conn.close()

