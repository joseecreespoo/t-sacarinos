
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
print(conexion1)  