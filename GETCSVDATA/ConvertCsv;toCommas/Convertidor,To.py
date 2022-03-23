import csv
#METODO DE LECTURA DEL ARCHIVO CACA.CSV BUSCAMOS CON EL DELIMITER LOS ;
reader = csv.reader(open("caca.csv", "rU"), delimiter=';')
#METODO DE ESCRITURA DEL ARCHIVO nuevo csv 
writer = csv.writer(open("csvLimpio.csv", 'w'), delimiter=',')
#Y sustituimos los ; por el delimitador  ,
writer.writerows(reader)

print("Delimiter successfully changed")