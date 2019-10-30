import mysql.connector
import os, time
from mysql.connector import Error
from datetime import date

class accesSql:

    host = ''
    user = ''
    __passwd = ''
    db = ''

    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.__passwd = passwd
        self.db = db

    def cleanTerminal():
        time.sleep(5)
        os.system ("clear")
    
    
    def insertUsers(self, email, name, password):
        try:
            connection = mysql.connector.connect(host = self.host, user = self.user, passwd = self.__passwd, db = self.db)
            mySql_insert_query = """INSERT INTO users VALUES("{}", "{}","{}");""".format(email, name, password)
            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_query)
            connection.commit()
            print("Inserted data")
            cursor.close()

        except mysql.connector.Error as error:
            print("error, data no inserted")
            print(error)

        finally:
            if(connection.is_connected()):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()
                

    def insertAC(self, id, temp, status):
            try:
                connection = mysql.connector.connect(host = self.host, user = self.user, passwd = self.__passwd, db = self.db)
                mySql_insert_query = """INSERT INTO ac VALUES("{}", "{}","{}");""".format(id, temp, status)
                cursor = connection.cursor()
                result = cursor.execute(mySql_insert_query)
                connection.commit()
                print("Inserted data")
                cursor.close()

            except mysql.connector.Error as error:
                print("error, data no inserted")
                print(error)

            finally:
                if(connection.is_connected()):
                    connection.close()
                    print("close connection")
                    accesSql.cleanTerminal()


    def insertRegForHour(self, id_ac, status, motion):
        try:

            connection = mysql.connector.connect(host = self.host, user = self.user, passwd = self.__passwd, db = self.db)
            mySql_insert_query = """INSERT INTO regforhour VALUES("{}", {},"{}", "{}");""".format(id_ac, "null", status, motion)
            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_query)
            connection.commit()
            print("Inserted data")
            cursor.close()

        except mysql.connector.Error as error:
            print("error, data no inserted")
            print(error)

        finally:
            if(connection.is_connected()):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()  

    def insertRegForDay(self, date, prom, time_on):
        try:

            connection = mysql.connector.connect(host = self.host, user = self.user, passwd = self.__passwd, db = self.db)
            mySql_insert_query = """INSERT INTO regforday VALUES("{}", "{}", "{}");""".format(date, prom, time_on)
            cursor = connection.cursor()
            result = cursor.execute(mySql_insert_query)
            connection.commit()
            print("Inserted data")
            cursor.close()

        except mysql.connector.Error as error:
            print("error, data no inserted")
            print(error)

        finally:
            if(connection.is_connected()):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()               
                
    def select(self, nameTable):
       # """"Puede hacer un select general a todas las tablas""""
        try:
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.__passwd, db=self.db)
            sql_query = "SELECT * FROM {};".format(nameTable)
            cursor = connection.cursor()
            cursor.execute(sql_query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print("Error reading data from table")
        finally:
            if(connection.is_connected):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()
    
    def deleteRegforHour(self, date):
        try:
            connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.__passwd, db=self.db)
            cursor = connection.cursor()
            sql_query = "DELETE FROM regforhour WHERE SUBSTRING(date, 1, 10) = '{}';".format(date)
            cursor.execute(sql_query)
            connection.commit()

            sql_query = "SELECT * FROM regforhour;"
            cursor.execute(sql_query)
            data = cursor.fetchall()
            
            if(len(data) == 0):
                print("Deleted succesefully...")

        except mysql.connector.Error as error:
            print("Failed to delete data : {}".format(error))
        finally:
            if(connection.is_connected):
                connection.close()
                print("close connection")
                accesSql.cleanTerminal()
