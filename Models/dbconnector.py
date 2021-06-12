import mysql.connector
from mysql.connector import Error
import os
import getpass

host = "localhost",
user = "root",
password = "",

class DBConnect:
    def executeInsert(self,query,value):
        try:
            self.con = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "PilotDB")
            if self.con.is_connected():
                cursor = self.con.cursor()
                cursor.execute(query,value)
                self.con.commit()
                print("...")
                print("\nData Berhasil ditambahkan")
        except Error as e:
            print(e)
            print("Data gagal ditambahkan")

    def executeDelete(self,query):
        try:
            self.con = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "PilotDB")
            if self.con.is_connected():
                cursor = self.con.cursor()
                cursor.execute(query)
                self.con.commit()
                print("\nData telah dihapus")
        except Error as e:
            print(e)
            print("Data gagal dihapus")

    def executeSelect(self,query,Val=False):
        try:
            self.con = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "PilotDB")
            if self.con.is_connected():
                cursor = self.con.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                self.con.commit()
                print("...")
                #return record
                if Val:
                    return record

        except Error as e:
            print(e)
            print("Data gagal ditampilkan")

    def executeSelectOne(self,query):
        try:
            self.con = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "PilotDB")
            if self.con.is_connected():
                cursor = self.con.cursor()
                cursor.execute(query)
                record = cursor.fetchone()
                self.con.commit()
                print("...")
                return record
        except Error as e:
            print(e)
            print("Data gagal ditampilkan")
    
    
    def executelogin(self,query,value):
        try:
            self.con = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "PilotDB")
            if self.con.is_connected():
                cursor = self.con.cursor()
                cursor.execute(query,value)
                record = cursor.fetchall()
                # self.con.commit()
                print("...")
                return record
                # if Val:
                #     return record

        except Error as e:
            print(e)
            print("Data gagal ditampilkan")