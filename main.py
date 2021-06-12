import wx
import guiProject_S4
from Models import database1

class pnlDashboard(guiProject_S4.panelDashboard):
    def __init__(self,parent):
        guiProject_S4.panelDashboard.__init__(self,parent) #construktor Superclass nya
        self.dataSiswa()
        self.dataNilai()

    def dataSiswa(self):
        s_cols = self.tabelSiswa.GetNumberCols()
        s_rows = self.tabelSiswa.GetNumberRows()
        if s_cols > 0:
            self.tabelSiswa.DeleteCols(0, s_cols, True)
        if s_rows > 0:
            self.tabelSiswa.DeleteRows(0, s_rows, True)

        #Nama Kolom
        colNames = ['No Induk','Nama lengkap','Jenis Kelamin','Kelas','Alamat']
        self.tabelSiswa.AppendCols(len(colNames))
        self.sws = database1.Siswa()
        daftarSws = self.sws.getAllSiswa()
        baris = 0
        self.listData = []
        for col in range(len(colNames)):
            self.tabelSiswa.SetColLabelValue(col, colNames[col])
        for sws_row in daftarSws:
            self.tabelSiswa.AppendRows(1)
            print(baris,'.',sws_row)
            noIdk,nama,jk,kelas,alamat = sws_row
            self.tabelSiswa.SetCellValue(baris,0, str(noIdk))
            self.tabelSiswa.SetCellValue(baris,1, nama)
            self.tabelSiswa.SetCellValue(baris,2, jk)
            self.tabelSiswa.SetCellValue(baris,3, kelas)
            self.tabelSiswa.SetCellValue(baris,4, alamat)
            self.tabelSiswa.SetCellAlignment( wx.ALIGN_CENTRE,baris,0,0 )
            self.listData.append(noIdk)
            baris += 1

    def insert(self):
        self.noIdk = self.inputNoIdk1.GetValue()
        self.tugas = int(float(self.inputTugas1.GetValue()))
        self.uts = int(float(self.inputUTS1.GetValue()))
        self.uas = int(float(self.inputUAS1.GetValue())) 
        
    def btnTambahSwsOnButtonClick( self, event ):
        if self.inputNoIdk.GetValue() == '' or self.inputNama.GetValue() == '' or self.inputJk.GetValue() == '' or self.inputKelas.GetValue() == '' or self.inputAlamat.GetValue() == '':
          wx.MessageBox('Data harus diisi','Terjadi Kesalahan')
          print('Data harus diisi')
          return False  

        noIdk = self.inputNoIdk.GetValue()
        nama = self.inputNama.GetValue()
        jk = self.inputJk.GetValue()
        kelas = self.inputKelas.GetValue()
        alamat = self.inputAlamat.GetValue()

        self.sws = database1.Siswa()
        self.sws.setSiswa(noIdk,nama,jk,kelas,alamat)

        wx.MessageBox('Data berhasil ditambahkan','informasi', wx.OK | wx.ICON_INFORMATION)
        self.dataSiswa()

    def btnTambahNilai1OnButtonClick( self, event ):
        if self.inputNoIdk1.GetValue() == '' or self.inputTugas1.GetValue() == '' or self.inputUTS1.GetValue() == '' or self.inputUAS1.GetValue() == '':
            wx.MessageBox('Data harus diisi','Terjadi Kesalahan')
            print('Data harus diisi')
            return False

        self.noIdk = self.inputNoIdk1.GetValue()
        self.tugas = int(float(self.inputTugas1.GetValue()))
        self.uts = int(float(self.inputUTS1.GetValue()))
        self.uas = int(float(self.inputUAS1.GetValue()))

        self.detail = database1.DetailSiswa(self.noIdk,self.tugas,self.uts,self.uas)
        self.detail.hitung()
        self.detail.tampilkanNilai()
        self.detail.setNilaiSiswa()
        self.dataNilai()

        wx.MessageBox('Data berhasil ditambahkan','informasi', wx.OK | wx.ICON_INFORMATION)

    def btnEditNilaiOnButtonClick( self, event ):
        if self.inputNoIdk2.GetValue() == '' or self.inputTugas2.GetValue() == '' or self.inputUTS2.GetValue() == '' or self.inputUAS2.GetValue() == '':
          wx.MessageBox('Data harus diisi','Terjadi Kesalahan')
          print('Data harus diisi')
          return False

        self.noIdk = self.inputNoIdk2.GetValue()
        self.tugas = int(float(self.inputTugas2.GetValue()))
        self.uts = int(float(self.inputUTS2.GetValue()))
        self.uas = int(float(self.inputUAS2.GetValue()))

        self.detail = database1.DetailSiswa(self.noIdk,self.tugas,self.uts,self.uas)
        self.detail.hitung()
        self.detail.tampilkanNilai()
        self.detail.UpdateNilaiSiswa()
        self.dataNilai()

        wx.MessageBox('Data berhasil diubah','informasi', wx.OK | wx.ICON_INFORMATION)

    def dataNilai(self):
        s_cols = self.cobaSetNilai.GetNumberCols()
        s_rows = self.cobaSetNilai.GetNumberRows()
        if s_cols > 0:
            self.cobaSetNilai.DeleteCols(0, s_cols, True)
        if s_rows > 0:
            self.cobaSetNilai.DeleteRows(0, s_rows, True)

        #Nama Kolom
        colNames = ['No Induk','Nama lengkap','Jenis Kelamin','Kelas','Alamat','NilaiTugas','NilaiUTS','NilaiUAS','NilaiAkhir','Mutu','Status']
        self.cobaSetNilai.AppendCols(len(colNames))
        self.sws = database1.Siswa()
        daftarSws = self.sws.getDetailSiswa()
        baris = 0
        self.listData = []
        for col in range(len(colNames)):
            self.cobaSetNilai.SetColLabelValue(col, colNames[col])
        for sws_row in daftarSws:
            self.cobaSetNilai.AppendRows(1)
            print(baris,'.',sws_row)                
            noIdk,nama,jk,kelas,alamat,tugas,uts,uas,na,indeks,info = sws_row
            self.cobaSetNilai.SetCellValue(baris,0, str(noIdk))
            self.cobaSetNilai.SetCellValue(baris,1, nama)
            self.cobaSetNilai.SetCellValue(baris,2, jk)
            self.cobaSetNilai.SetCellValue(baris,3, kelas)                
            self.cobaSetNilai.SetCellValue(baris,4, alamat)
            self.cobaSetNilai.SetCellValue(baris,5, str(tugas))
            self.cobaSetNilai.SetCellValue(baris,6, str(uts))
            self.cobaSetNilai.SetCellValue(baris,7, str(uas))
            self.cobaSetNilai.SetCellValue(baris,8, str(na))
            self.cobaSetNilai.SetCellValue(baris,9, str(indeks))
            self.cobaSetNilai.SetCellValue(baris,10, str(info))
            self.cobaSetNilai.SetCellAlignment( wx.ALIGN_CENTRE,baris,0,0 )
            self.listData.append(noIdk)                
            baris += 1 

    def btnDetailDataSwsOnButtonClick( self, event ):
        self.panelDashboard.lihat.Show()

    def btnHapusOnButtonClick( self, event ):
        dlt = self.inputNoIdkHapus.GetValue()
        dlg = wx.MessageDialog(self,'Hapus data', 'Informasi', style=wx.YES_NO )
        retval = dlg.ShowModal()
        if retval == wx.ID_YES:
            print('hapus')
            self.sws.hapusSiswa(dlt)
            self.dataSiswa()
            self.dataNilai()
        else:
            print('NO di pilih')
        
    def cari(self,noIdk):
        self.sws = database1.Siswa()
        result = self.sws.getSiswa(noIdk)
        if result == []:
            wx.MessageBox('Data tidak ditemukan','Terjadi Kesalahan',wx.OK | wx.ICON_ERROR) 
            print('Data tidak ditemukan')
        else:
            data = ('\n No.Induk : {} \n Nama Lengkap : {} \n Jenis Kelamin : {} \n kelas : {} \n Alamat : {} \n Nilai Tugas : {} \n Nilai UTS : {} \n Nilai UAS : {} \n Rata-Rata Nilai: {} \n Mutu : {} \n Status : {}'.format(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10]))
            data1 =str(data)

            wx.MessageBox(data1,'Informasi',wx.OK | wx.ICON_ASTERISK)

        print(data1) 
        print("searching berhasil")

    def btnCariOnButtonClick( self, event ):
        noIdkCari = self.inputCari.GetValue()
        self.cari(noIdkCari)
        
class Frame (guiProject_S4.MyFrame2): 
    def __init__ (self,parent):
        guiProject_S4.MyFrame2.__init__(self,parent)
        # di construktor buat panelDashboard biat def nya dikenali
        self.panelDashboard = pnlDashboard(parent=self) 
        self.panelDashboard.Hide()

    def MyFrame2OnSize( self, event ):
        self.panelDashboard.SetSize(self.GetSize())
        self.m_panelLogin.SetSize(self.GetSize())

    def m_buttonLoginOnButtonClick( self, event ):
        username = self.inputUsername.GetValue()
        password = self.inputPassword.GetValue()

        print('Username',username)
        print('Password',password)

        self.acc = database1.User()
        bisa = self.acc.account(username,password)
        if bisa  == []:
            wx.MessageBox('Login Gagal','Terjadi Kesalahan',wx.OK | wx.ICON_ERROR) 
            print("Login Gagal")
        else:
            wx.MessageBox('Login Berhasil','informasi',wx.OK | wx.ICON_INFORMATION)
            print("Login Berhasi")
            self.m_panelLogin.Hide()
            self.panelDashboard.Show()

    def MyFrame2OnClose( self, event ):
        self.Destroy()


app = wx.App()
frame = Frame(parent=None)
frame.Show()
app.MainLoop()