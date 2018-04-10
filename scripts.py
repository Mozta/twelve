import petl as etl
import psycopg2

connection = psycopg2.connect('dbname=twelveBD user=postgres password=admin')

table = etl.fromdb(connection, 'SELECT * FROM personas')
table1 = [['idPersona','nombre','sexo','edad'],[1,'Rafael Perez Aguirre','m',24]]
table2 = [['idPersona','nombre','sexo','edad'],[2,'Eduardo Cantoran Flores','m',25]]
table3 = [['idPersona','nombre','sexo','edad'],[3,'Adriana Lopez Montiel','m',30]]

table1 = [['idEmpresa','nombre','sucursal','direccion'],['IDIT',1,'Blvrd del Niño Poblano 2901, Reserva Territorial Atlixcáyotl, Centro Comercial Puebla, 72810 San Andrés Cholula, Pue.']]

table1 = [['nombre','nofichas','secuencia','tiempo'],['fácil',30,1,45]]
table1 = [['nombre','nofichas','secuencia','tiempo'],['intermedio',35,1,40]]
table1 = [['nombre','nofichas','secuencia','tiempo'],['Dificil',45,1,40]]
table1 = [['nombre','nofichas','secuencia','tiempo'],['Veterano',50,1,45]]
table1 = [['nombre','nofichas','secuencia','tiempo'],['Dios',55,1,40]]

etl.todb(table1, connection, 'personas')
etl.appenddb(table1, connection, 'personas')
