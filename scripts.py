import petl as etl
import psycopg2

connection = psycopg2.connect('dbname=twelveBD user=postgres password=admin')

table = etl.fromdb(connection, 'SELECT * FROM personas')
table1 = [['idPersona','nombre','sexo','edad'],[1,'Rafael Perez Aguirre','m',24]]
table2 = [['idPersona','nombre','sexo','edad'],[2,'Eduardo Cantoran Flores','m',25]]
table3 = [['idPersona','nombre','sexo','edad'],[3,'Adriana Lopez Montiel','m',30]]

etl.todb(table1, connection, 'personas')
etl.appenddb(table1, connection, 'personas')
