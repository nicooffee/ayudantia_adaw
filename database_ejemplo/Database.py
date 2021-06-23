import psycopg2
import DatabaseData as dbdata

class PSConnection:
    def __init__(self):
        self.connection = self.__create_conn()
        self.cursor = self.connection.cursor()

    def query(self,query,params):
        try:
            res = self.cursor.execute(query,params)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error al ejecutar la query: ", error)
            self.connection = self.__create_conn()
            self.cursor = self.connection.cursor()
            res = self.cursor.execute(query,params)
            self.connection.commit()

    def fetch(self,query,params):
        try:
            res = self.cursor.execute(query,params)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error al ejecutar la query: ", error)
            self.connection = self.__create_conn()
            self.cursor = self.connection.cursor()
            res = self.cursor.execute(query,params)
            self.connection.commit()
        finally:
            return self.cursor.fetchone()

    def fetch_all(self,query,params):
        try:
            res = self.cursor.execute(query,params)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error al ejecutar la query: ", error)
            self.connection = self.__create_conn()
            self.cursor = self.connection.cursor()
            res = self.cursor.execute(query,params)
            self.connection.commit()
        finally:
            return self.cursor.fetchall()

    def __create_conn(self):
        return psycopg2.connect(
            user=dbdata.user,
            password=dbdata.db_model_pswd,
            host=dbdata.host,
            port=dbdata.port,
            database=dbdata.db_model_name,
            application_name='Demo'
        )
    
    def __del__(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()
