import sqlite3
import psycopg


class DBConexLite3:
    
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def execute_query(self, query, params=()):
        self.cursor.execute(query,params)
        self.conn.commit()
    
    def fetch_data(self,query,params=()):
        self.cursor.execute(query, params)   
       
        return self.cursor.fetchall()
    

    def close_connection(self):
        self.conn.close()

class DBConexPostgreSQL:
    def __init__(self):
        self.conn = psycopg.connect(f"host=localhost port=5432 dbname=  user=postgres password= ")
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=()):
        self.cursor.execute(query,params)
        self.conn.commit()
    
    def fetch_data(self,query,params=()):
        self.cursor.execute(query, params)   
       
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

class DBFactory:

    @staticmethod
    def create_db(db_type,db_name):
        if db_type == "SQLITE3":
            return DBConexLite3(db_name)
        elif db_type == "POSTGRESQL":
            return DBConexPostgreSQL()
        else:
            raise ValueError("Tipo de base de datos no permitida")