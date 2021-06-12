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


class User():

    def __init__(self):
        self.username= str(input("Enter Username:"))        
        self.password = getpass.getpass("Enter your password:")

    
    def account(self):
        connection = DBConnect()
        # return username, password
        query = 'SELECT * FROM account where username= %s and pwd = %s'
        value = (self.username,self.password)
        result=connection.executelogin(query,value)
        return result

class Siswa(DBConnect):
    def setSiswa(self,noIdk,nama,jk,kelas,alamat):
        self.query = 'INSERT INTO siswa (NoInduk,NamaLengkap,Jk,Kelas,alamat) VALUES(%s,%s,%s,%s,%s)'
        value = (noIdk,nama,jk,kelas,alamat)
        self.executeInsert(self.query,value)

    def getAllSiswa(self):
        self.query = 'SELECT * FROM siswa ORDER BY NoInduk ASC'
        result=self.executeSelect(self.query,True)
        return result

    def getSiswa(self):
        noIdk=int(input('No Induk : '))
        self.query = 'SELECT p.NoInduk, p.NamaLengkap, p.Jk, p.Kelas, p.alamat, dp.NilaiTugas, dp.NilaiUTS, dp.NilaiUAS, dp.NilaiAkhir, dp.Mutu, dp.status FROM siswa p JOIN detailnilai dp ON p.NoInduk=dp.NoInduk WHERE p.NoInduk = {}'.format(noIdk)
        result = self.executeSelectOne(self.query)
        return result

    def getDetailSiswa(self):
        self.query = 'SELECT p.NoInduk, p.NamaLengkap, p.Jk, p.Kelas, p.Alamat, dp.NilaiTugas, dp.NilaiUTS, dp.NilaiUAS, dp.NilaiAkhir, dp.Mutu, dp.status FROM siswa p JOIN detailnilai dp ON p.NoInduk=dp.NoInduk ORDER BY p.NamaLengkap ASC'
        result=self.executeSelect(self.query,Val=True)
        return result

    def getInfoJumlah(self):
        # self.query = "with sws AS(\
        #                 select  '(' || p.NoInduk ||': '|| count(p.NoInduk) || ')' as jumlah\
        #                 from siswa p \
        #                 group by p.NoInduk\
        #             )\
        #             select group_concat( p.jumlah, ', ') as info\
        #             from sws p;"
        self.query = 'select count(NoInduk) as jumlah from siswa'
        print('self.query : ', self.query )
        result=self.executeSelect(self.query,Val=True)
        # print('Jumlah Data')
        for i in result:
            print('Jumlah Data Siwa : ', i[0])

    def hapusSiswa(self,dlt):
        self.query = 'DELETE FROM  siswa WHERE NoInduk= {} '.format(dlt)
        self.executeDelete(self.query)

class DetailSiswa(Siswa):
     na = 0
     indeks = ""
     info = ""

     def __init__(self,noIdk,tugas,uts,uas):
         self.noIdk = noIdk
         self.tugas = tugas 
         self.uts = uts 
         self.uas = uas

     def hitung(self):
        
        self.na =  (0.15 * self.uas) + (0.35 * self.uts) +  (0.50 * self.uas)

        if self.na >= 80:
            self.indeks = 'A'
            self.info = 'Naik Kelas'
        elif self.na >= 70:
            self.indeks = 'B'
            self.info = 'Naik Kelas'
        elif self.na >= 55:
            self.indeks = 'C'
            self.info = 'Naik Kelas'
        elif self.na >= 40:
            self.indeks = 'D'
            self.info = 'Tidak Naik Kelas'
        else:
            self.indeks = 'E'
            self.info = 'Tidak Naik Kelas'

     def tampilkanNilai(self):
        print("\nNilai Akhir  = %0.2f" % self.na)
        print("Mutu = %s" % self.indeks)
        print("Status = %s" % self.info)

     def setNilaiSiswa(self):
        self.query = 'INSERT INTO detailnilai (NoInduk,NilaiTugas,NilaiUTS,NilaiUAS,NilaiAkhir,Mutu,Status) VALUES(%s,%s,%s,%s,%s,%s,%s)' 
        value = (self.noIdk,self.tugas,self.uts,self.uas,self.na,self.indeks,self.info)
        self.executeInsert(self.query,value)

     def UpdateNilaiSiswa(self):
        self.query = '''UPDATE detailnilai SET NilaiTugas = %s, NilaiUTS = %s, NilaiUAS = %s, NilaiAkhir = %s, Mutu = %s, Status = %s WHERE NoInduk = %s '''
        value = (self.tugas,self.uts,self.uas,self.na,self.indeks,self.info,self.noIdk)
        self.executeInsert(self.query,value)


if __name__ == '__main__':
    sws = Siswa()
    daftarSws = sws.getAllSiswa()
    baris = 1
    for sws_row in daftarSws:
        print(baris,'. ', sws_row)
        baris += 1


# class View():
#     sws = Siswa()

#     def menu1(self):
#         loop = self.sws.getAllSiswa()
#         print('\n    Daftar Siswa')
#         print("-"*80)
#         print("No Induk \t Nama Lengkap \t Jenis Kelamin \t Kelas \t\t Alamat ")
#         print("-"*80)
#         for row in loop:
#             print(row[0], "\t\t",row[1], "\t\t",row[2], "\t",row[3], "\t",row[4])
#         print("-"*80)

#     def menu2(self):
#         loop = self.sws.getDetailSiswa()
#         print('\n   Detail Daftar Siswa')
#         print("-"*165)
#         print("No Induk \t Nama Lengkap \t Jenis Kelamin \t Kelas \t\t Alamat \t Nilai Tugas \t Nilai UTS \t Nilai UAS \t Nilai Akhir \t Mutu \t Status ")
#         print("-"*165)
#         for row in loop:
#              print(row[0], "\t\t",row[1], "\t\t",row[2], "\t",row[3], "\t",row[4], "\t",row[5], "\t\t",row[6], "\t\t",row[7], "\t\t",row[8], "\t\t",row[9], "\t",row[10])
#         print("-"*165)
#         print("\n--> Data berhasil ditampilkan")

#     def menu3(self):
#         noIdk = int(input("No Induk : "))
#         nama = str(input("Nama Lengkap : "))
#         jk = str(input("Jenis Kelamin [P/L] : "))
#         kelas = str(input("Kelas : "))
#         alamat = str(input("Alamat : "))

#         tambah = Siswa()
#         tambah.setSiswa(noIdk,nama,jk,kelas,alamat)
    
#     def inpdata(self):
#         self.noIdk=int(input("No Induk: "))
#         self.tugas=int(input("Nilai Tugas: "))
#         self.uts=int(input("Nilai UTS: "))
#         self.uas=int(input("Nilai UAS: "))

#     def menu4(self):
#         Detail = DetailSiswa(self.noIdk,self.tugas,self.uts,self.uas) 
#         Detail.hitung()
#         Detail.tampilkanNilai()  
#         Detail.setNilaiSiswa()
    
#     def menu5(self):
#         result = self.sws.getSiswa()
#         print('\n No.Induk : {} \n Nama Lengkap : {} \n Jenis Kelamin : {} \n kelas : {} \n Alamat : {} \n Nilai Tugas : {} \n Nilai UTS : {} \n Nilai UAS : {} \n Rata-Rata Nilai: {} \n Mutu : {} \n Status : {}'.format(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10]))
#         print("\nData berhasil ditampilkan")

#     def menu6(self):
#         Detail = DetailSiswa(self.noIdk,self.tugas,self.uts,self.uas) 
#         Detail.hitung()
#         Detail.tampilkanNilai()  
#         Detail.UpdateNilaiSiswa()

#     def menu7(self):
#         dlt = int(input("No Induk : "))
#         pilih = str(input("Apakah anda yakin ingin menghapus data tersebut? [No/Yes] : "))
#         if (pilih == 'No'):
#             print("Data batal di hapus")
#         elif (pilih == 'Yes'):
#             self.sws.hapusSiswa(dlt)
#         else:
#             print("Pilihan tidak ada!")
    
#     def acc(self):
#         Dee = View() 
#         zaza = User()
#         bisa = zaza.account()   
#         if bisa  == []:
#             print("Maaf akun anda tidak terdaftar!")
#             Dee.acc()
#         else:
#             print("Selamat Datang!")

       
# def show_menu():
#     print('\n')
#     print('===============================================')
#     print('            APLIKASI REKAP NILAI KELAS         ')
#     print('===============================================')
#     print("1. Tampilkan Data Siswa")
#     print("2. Tampikan Detail Data Siswa")
#     print("3. Tambah Data Siswa")
#     print("4. Tambah Data Nilai")
#     print("5. Cari Data Siswa")
#     print("6. Update Data Nilai")
#     print("7. Hapus Data Siswa")
#     print("8. Kembali Ke Halaman Utama")
#     print("9. Jumlah")
#     print("0. Keluar")
#     menu = input("Pilih menu> ")

#     D = View()
#     if menu == "1":
#         D.menu1()
#         print("\n--> Data berhasil ditampilkan")
#     elif menu == "2":
#         # D.menu1()
#         D.menu2()
#     elif menu == "3":
#         D.menu1()
#         D.menu3()
#     elif menu == "4":
#         D.menu1()
#         D.inpdata()
#         D.menu4()
#     elif menu == "5":
#         D.menu1()
#         D.menu5()
#     elif menu == "6":
#         D.menu1()
#         D.inpdata()
#         D.menu6()
#     elif menu =="7":
#         D.menu1()
#         D.menu7()
#     elif menu == "8":
#         D.acc() 
#     elif menu == "9":
#         sis = Siswa()
#         sis.getInfoJumlah()
#     elif menu == "0":
#         exit()
#     else:
#         print("Menu salah!")

# # De = View()
# # De.acc() 

# if __name__ == "__main__":
#   while(True):
#     show_menu()


