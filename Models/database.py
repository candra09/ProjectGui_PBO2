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
            self.con = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "posts")
            if self.con.is_connected():
                cursor = self.con.cursor()
                cursor.execute(query,value)
                self.con.commit()
                print("...")
                print("\nData Berhasil ditambahkan")
        except Error as e:
            print(e)
            print("Data gagal ditambahkan")

    def executeSelect(self,query,Val=False):
        try:
            self.con = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "posts")
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
            self.con = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "posts")
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
    

class Person(DBConnect):
    def setMahaSiswa(self,nama,nim,alamat):
        # self.query = 'INSERT INTO posts (nama,nim,alamat) VALUES(%s,%s,%s)'
        # value = (nama,nim,alamat)
        # self.executeInsert(self.query,value)
        self.query = 'INSERT INTO posts (nama,nim,alamat) VALUES(%s,%s,%s)'
        value = (nama,nim,alamat)
        # self.query = self.query % (nama,nim,alamatt)
        self.executeInsert(self.query,value)

    def getAllMahaSiswa(self):
        # self.query = 'SELECT * FROM post ORDER BY nama ASC'
        # result=self.executeSelect(self.query,True)
        # return result
        connection = DBConnect()
        query = 'SELECT * FROM posts '
        result=connection.executeSelect(query)
        #print(result)
        print("Nama \t NIM \t  Alamat ")
        for row in result:
            print(row[0], "\t\t",row[1], "\t\t",row[2])

    def getMahaSiswa(self):
        # nama=str(input('nama : '))
        # self.query = 'SELECT * from post WHERE nama = {}'.format(nama)
        # result = self.executeSelectOne(self.query)
        # return result
        connection = DBConnect()
        # noIdk=int(input('No Induk : '))
        query = 'SELECT * FROM post WHERE nama = {}'.format(nama)
        result = connection.executeSelectOne(query)
        #print(result)
        print(' Nama : {} \n NIM : {} \n Alamat : {}'.format(result[0],result[1],result[2]))

    

mhs = Person()
mhs.getAllMahaSiswa()
# if __name__ == "__main__":
#   while(True):
#     show_menu()

# if __name__ == '__main__':
# 	mhs = Person()
# 	daftarMhs = mhs.getAllMahasiswa()
# 	baris = 1
# 	for mhs_row in daftarMhs:
# 		print(baris,'. ', mhs_row)
# 		baris += 1