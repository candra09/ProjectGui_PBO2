# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class panelDashboard
###########################################################################

class panelDashboard ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 616,805 ), style = wx.TAB_TRAVERSAL )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.Dashboard = wx.StaticText( self, wx.ID_ANY, u"Dashboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Dashboard.Wrap( -1 )
		self.Dashboard.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer13.Add( self.Dashboard, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Dash = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Dash.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer341 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText611 = wx.StaticText( self.Dash, wx.ID_ANY, u"Rekap Nilai Kelas", wx.DefaultPosition, wx.Size( 200,25 ), wx.ALIGN_CENTRE )
		self.m_staticText611.Wrap( -1 )
		self.m_staticText611.SetFont( wx.Font( 14, 74, 90, 90, False, "Geometr212 BkCn BT" ) )
		self.m_staticText611.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText611.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_staticText611.SetMaxSize( wx.Size( 500,100 ) )
		
		bSizer341.Add( self.m_staticText611, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP|wx.ALL|wx.SHAPED, 5 )
		
		self.m_staticText592 = wx.StaticText( self.Dash, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText592.Wrap( -1 )
		self.m_staticText592.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer341.Add( self.m_staticText592, 0, wx.ALL, 5 )
		
		self.m_splitter2 = wx.SplitterWindow( self.Dash, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		
		self.m_panel151 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel151.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2211 = wx.StaticText( self.m_panel151, wx.ID_ANY, u"Tambah Data Siswa :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2211.Wrap( -1 )
		bSizer18.Add( self.m_staticText2211, 0, wx.ALL, 5 )
		
		fgSizer201 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer201.SetFlexibleDirection( wx.BOTH )
		fgSizer201.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText581 = wx.StaticText( self.m_panel151, wx.ID_ANY, u"No Induk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText581.Wrap( -1 )
		fgSizer201.Add( self.m_staticText581, 0, wx.ALL, 5 )
		
		self.inputNoIdk = wx.TextCtrl( self.m_panel151, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputNoIdk.SetMaxSize( wx.Size( 500,-1 ) )
		
		fgSizer201.Add( self.inputNoIdk, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText591 = wx.StaticText( self.m_panel151, wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText591.Wrap( -1 )
		fgSizer201.Add( self.m_staticText591, 0, wx.ALL, 5 )
		
		self.inputNama = wx.TextCtrl( self.m_panel151, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer201.Add( self.inputNama, 0, wx.ALL, 5 )
		
		self.m_staticText631 = wx.StaticText( self.m_panel151, wx.ID_ANY, u"Jenis Kelamin (P/L)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText631.Wrap( -1 )
		fgSizer201.Add( self.m_staticText631, 0, wx.ALL, 5 )
		
		self.inputJk = wx.TextCtrl( self.m_panel151, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer201.Add( self.inputJk, 0, wx.ALL, 5 )
		
		self.m_staticText671 = wx.StaticText( self.m_panel151, wx.ID_ANY, u"Kelas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText671.Wrap( -1 )
		fgSizer201.Add( self.m_staticText671, 0, wx.ALL, 5 )
		
		self.inputKelas = wx.TextCtrl( self.m_panel151, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer201.Add( self.inputKelas, 0, wx.ALL, 5 )
		
		self.m_staticText641 = wx.StaticText( self.m_panel151, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText641.Wrap( -1 )
		fgSizer201.Add( self.m_staticText641, 0, wx.ALL, 5 )
		
		self.inputAlamat = wx.TextCtrl( self.m_panel151, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer201.Add( self.inputAlamat, 0, wx.ALL, 5 )
		
		self.btnTambahSws = wx.Button( self.m_panel151, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer201.Add( self.btnTambahSws, 0, wx.ALL, 5 )
		
		
		bSizer18.Add( fgSizer201, 1, wx.EXPAND, 5 )
		
		
		self.m_panel151.SetSizer( bSizer18 )
		self.m_panel151.Layout()
		bSizer18.Fit( self.m_panel151 )
		self.m_panel161 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel161.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_panel161.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText54 = wx.StaticText( self.m_panel161, wx.ID_ANY, u"Tambah Data Nilai :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		bSizer20.Add( self.m_staticText54, 0, wx.ALL, 5 )
		
		fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.NoInduk = wx.StaticText( self.m_panel161, wx.ID_ANY, u"No Induk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NoInduk.Wrap( -1 )
		fgSizer12.Add( self.NoInduk, 0, wx.ALL, 5 )
		
		self.inputNoIdk1 = wx.TextCtrl( self.m_panel161, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.inputNoIdk1, 0, wx.ALL, 5 )
		
		self.NilaiTugas = wx.StaticText( self.m_panel161, wx.ID_ANY, u"Nilai Tugas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NilaiTugas.Wrap( -1 )
		fgSizer12.Add( self.NilaiTugas, 0, wx.ALL, 5 )
		
		self.inputTugas1 = wx.TextCtrl( self.m_panel161, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.inputTugas1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.NilaiUTS = wx.StaticText( self.m_panel161, wx.ID_ANY, u"Nilai UTS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NilaiUTS.Wrap( -1 )
		fgSizer12.Add( self.NilaiUTS, 0, wx.ALL, 5 )
		
		self.inputUTS1 = wx.TextCtrl( self.m_panel161, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.inputUTS1, 0, wx.ALL, 5 )
		
		self.NilaiUAS = wx.StaticText( self.m_panel161, wx.ID_ANY, u"Nilai UAS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NilaiUAS.Wrap( -1 )
		fgSizer12.Add( self.NilaiUAS, 0, wx.ALL, 5 )
		
		self.inputUAS1 = wx.TextCtrl( self.m_panel161, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.inputUAS1, 0, wx.ALL, 5 )
		
		self.m_staticText60 = wx.StaticText( self.m_panel161, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		self.m_staticText60.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		fgSizer12.Add( self.m_staticText60, 0, wx.ALL, 5 )
		
		self.m_staticText612 = wx.StaticText( self.m_panel161, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText612.Wrap( -1 )
		self.m_staticText612.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		fgSizer12.Add( self.m_staticText612, 0, wx.ALL, 5 )
		
		self.btnTambahNilai1 = wx.Button( self.m_panel161, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer12.Add( self.btnTambahNilai1, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( fgSizer12, 1, wx.EXPAND, 5 )
		
		
		self.m_panel161.SetSizer( bSizer20 )
		self.m_panel161.Layout()
		bSizer20.Fit( self.m_panel161 )
		self.m_splitter2.SplitVertically( self.m_panel151, self.m_panel161, 0 )
		bSizer341.Add( self.m_splitter2, 1, wx.EXPAND, 5 )
		
		
		self.Dash.SetSizer( bSizer341 )
		self.Dash.Layout()
		bSizer341.Fit( self.Dash )
		self.m_notebook2.AddPage( self.Dash, u"Dashboard", False )
		self.Lihat = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer16.SetMinSize( wx.Size( -1,0 ) ) 
		self.m_staticText37 = wx.StaticText( self.Lihat, wx.ID_ANY, u"Detail Data Siswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		self.m_staticText37.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer16.Add( self.m_staticText37, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.cobaSetNilai = wx.grid.Grid( self.Lihat, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.cobaSetNilai.CreateGrid( 5, 1 )
		self.cobaSetNilai.EnableEditing( True )
		self.cobaSetNilai.EnableGridLines( True )
		self.cobaSetNilai.EnableDragGridSize( False )
		self.cobaSetNilai.SetMargins( 0, 0 )
		
		# Columns
		self.cobaSetNilai.SetColSize( 0, 200 )
		self.cobaSetNilai.EnableDragColMove( False )
		self.cobaSetNilai.EnableDragColSize( True )
		self.cobaSetNilai.SetColLabelSize( 30 )
		self.cobaSetNilai.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.cobaSetNilai.EnableDragRowSize( True )
		self.cobaSetNilai.SetRowLabelSize( 1 )
		self.cobaSetNilai.SetRowLabelValue( 0, wx.EmptyString )
		self.cobaSetNilai.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.cobaSetNilai.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer16.Add( self.cobaSetNilai, 0, wx.ALL, 5 )
		
		self.m_button11 = wx.Button( self.Lihat, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button11, 0, wx.ALL, 5 )
		
		
		self.Lihat.SetSizer( bSizer16 )
		self.Lihat.Layout()
		bSizer16.Fit( self.Lihat )
		self.m_notebook2.AddPage( self.Lihat, u"Detail Data Siswa", False )
		self.Edit = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Edit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6113 = wx.StaticText( self.Edit, wx.ID_ANY, u"Rekap Nilai Kelas", wx.DefaultPosition, wx.Size( 200,25 ), wx.ALIGN_CENTRE )
		self.m_staticText6113.Wrap( -1 )
		self.m_staticText6113.SetFont( wx.Font( 14, 74, 90, 90, False, "Geometr212 BkCn BT" ) )
		self.m_staticText6113.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText6113.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_staticText6113.SetMaxSize( wx.Size( 500,100 ) )
		
		bSizer33.Add( self.m_staticText6113, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText86 = wx.StaticText( self.Edit, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		self.m_staticText86.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer33.Add( self.m_staticText86, 0, wx.ALL, 5 )
		
		self.m_panel1611 = wx.Panel( self.Edit, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1611.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_panel1611.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer201 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText541 = wx.StaticText( self.m_panel1611, wx.ID_ANY, u"Edit Data Nilai :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText541.Wrap( -1 )
		bSizer201.Add( self.m_staticText541, 0, wx.ALL, 5 )
		
		fgSizer121 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer121.SetFlexibleDirection( wx.BOTH )
		fgSizer121.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.NoInduk1 = wx.StaticText( self.m_panel1611, wx.ID_ANY, u"No Induk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NoInduk1.Wrap( -1 )
		fgSizer121.Add( self.NoInduk1, 0, wx.ALL, 5 )
		
		self.inputNoIdk2 = wx.TextCtrl( self.m_panel1611, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer121.Add( self.inputNoIdk2, 0, wx.ALL, 5 )
		
		self.NilaiTugas1 = wx.StaticText( self.m_panel1611, wx.ID_ANY, u"Nilai Tugas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NilaiTugas1.Wrap( -1 )
		fgSizer121.Add( self.NilaiTugas1, 0, wx.ALL, 5 )
		
		self.inputTugas2 = wx.TextCtrl( self.m_panel1611, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer121.Add( self.inputTugas2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.NilaiUTS1 = wx.StaticText( self.m_panel1611, wx.ID_ANY, u"Nilai UTS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NilaiUTS1.Wrap( -1 )
		fgSizer121.Add( self.NilaiUTS1, 0, wx.ALL, 5 )
		
		self.inputUTS2 = wx.TextCtrl( self.m_panel1611, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer121.Add( self.inputUTS2, 0, wx.ALL, 5 )
		
		self.NilaiUAS1 = wx.StaticText( self.m_panel1611, wx.ID_ANY, u"Nilai UAS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NilaiUAS1.Wrap( -1 )
		fgSizer121.Add( self.NilaiUAS1, 0, wx.ALL, 5 )
		
		self.inputUAS2 = wx.TextCtrl( self.m_panel1611, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer121.Add( self.inputUAS2, 0, wx.ALL, 5 )
		
		self.m_staticText601 = wx.StaticText( self.m_panel1611, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText601.Wrap( -1 )
		self.m_staticText601.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		fgSizer121.Add( self.m_staticText601, 0, wx.ALL, 5 )
		
		self.m_staticText6121 = wx.StaticText( self.m_panel1611, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6121.Wrap( -1 )
		self.m_staticText6121.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		fgSizer121.Add( self.m_staticText6121, 0, wx.ALL, 5 )
		
		self.btnEditNilai = wx.Button( self.m_panel1611, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer121.Add( self.btnEditNilai, 0, wx.ALL, 5 )
		
		
		bSizer201.Add( fgSizer121, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1611.SetSizer( bSizer201 )
		self.m_panel1611.Layout()
		bSizer201.Fit( self.m_panel1611 )
		bSizer33.Add( self.m_panel1611, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.Edit.SetSizer( bSizer33 )
		self.Edit.Layout()
		bSizer33.Fit( self.Edit )
		self.m_notebook2.AddPage( self.Edit, u"Edit Data Nilai", True )
		self.Hapus = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-500 ), wx.TAB_TRAVERSAL )
		self.Hapus.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.Hapus.SetMaxSize( wx.Size( -1,-500 ) )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6112 = wx.StaticText( self.Hapus, wx.ID_ANY, u"Rekap Nilai Kelas", wx.DefaultPosition, wx.Size( 200,25 ), wx.ALIGN_CENTRE )
		self.m_staticText6112.Wrap( -1 )
		self.m_staticText6112.SetFont( wx.Font( 14, 74, 90, 90, False, "Geometr212 BkCn BT" ) )
		self.m_staticText6112.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText6112.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_staticText6112.SetMaxSize( wx.Size( 500,100 ) )
		
		bSizer21.Add( self.m_staticText6112, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText531 = wx.StaticText( self.Hapus, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText531.Wrap( -1 )
		self.m_staticText531.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer21.Add( self.m_staticText531, 0, wx.ALL, 5 )
		
		self.m_panel19 = wx.Panel( self.Hapus, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText55 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"Masukan No Induk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )
		self.m_staticText55.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer22.Add( self.m_staticText55, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText551 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"Masukan No Induk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText551.Wrap( -1 )
		bSizer22.Add( self.m_staticText551, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.inputNoIdkHapus = wx.TextCtrl( self.m_panel19, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.inputNoIdkHapus, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnHapus = wx.Button( self.m_panel19, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.btnHapus, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText76 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"*Data yang sudah terhapus tidak dapat kembali lagi,sekian.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )
		self.m_staticText76.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		
		bSizer22.Add( self.m_staticText76, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText77 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"``", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )
		self.m_staticText77.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer22.Add( self.m_staticText77, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText771 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"``", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText771.Wrap( -1 )
		self.m_staticText771.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer22.Add( self.m_staticText771, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText772 = wx.StaticText( self.m_panel19, wx.ID_ANY, u"``", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText772.Wrap( -1 )
		self.m_staticText772.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer22.Add( self.m_staticText772, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel19.SetSizer( bSizer22 )
		self.m_panel19.Layout()
		bSizer22.Fit( self.m_panel19 )
		bSizer21.Add( self.m_panel19, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.Hapus.SetSizer( bSizer21 )
		self.Hapus.Layout()
		self.m_notebook2.AddPage( self.Hapus, u"Hapus Data", False )
		
		bSizer13.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelDataSiswa = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText231 = wx.StaticText( self.m_panelDataSiswa, wx.ID_ANY, u"Data Siswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )
		bSizer141.Add( self.m_staticText231, 0, wx.ALL, 5 )
		
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText48 = wx.StaticText( self.m_panelDataSiswa, wx.ID_ANY, u"No Induk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		bSizer211.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.inputCari = wx.TextCtrl( self.m_panelDataSiswa, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.inputCari.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.inputCari.SetMaxSize( wx.Size( 500,-1 ) )
		
		bSizer211.Add( self.inputCari, 0, wx.ALL, 5 )
		
		self.btnCari = wx.Button( self.m_panelDataSiswa, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.btnCari, 0, wx.ALL, 5 )
		
		
		bSizer141.Add( bSizer211, 0, wx.SHAPED|wx.TOP, 0 )
		
		self.btnDetailDataSws = wx.Button( self.m_panelDataSiswa, wx.ID_ANY, u"Detail Data Siswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.btnDetailDataSws, 0, wx.ALL, 5 )
		
		self.tabelSiswa = wx.grid.Grid( self.m_panelDataSiswa, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 500,-1 ), wx.SUNKEN_BORDER )
		
		# Grid
		self.tabelSiswa.CreateGrid( 5, 5 )
		self.tabelSiswa.EnableEditing( True )
		self.tabelSiswa.EnableGridLines( True )
		self.tabelSiswa.EnableDragGridSize( False )
		self.tabelSiswa.SetMargins( 0, 0 )
		
		# Columns
		self.tabelSiswa.SetColSize( 0, 80 )
		self.tabelSiswa.SetColSize( 1, 230 )
		self.tabelSiswa.SetColSize( 2, 81 )
		self.tabelSiswa.SetColSize( 3, 65 )
		self.tabelSiswa.SetColSize( 4, 90 )
		self.tabelSiswa.EnableDragColMove( False )
		self.tabelSiswa.EnableDragColSize( True )
		self.tabelSiswa.SetColLabelSize( 30 )
		self.tabelSiswa.SetColLabelValue( 0, u"No Induk" )
		self.tabelSiswa.SetColLabelValue( 1, u"Nama Lengkap" )
		self.tabelSiswa.SetColLabelValue( 2, u"Jenis Kelamin" )
		self.tabelSiswa.SetColLabelValue( 3, u"Kelas" )
		self.tabelSiswa.SetColLabelValue( 4, u"Alamat" )
		self.tabelSiswa.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.tabelSiswa.SetRowSize( 0, 80 )
		self.tabelSiswa.SetRowSize( 1, 200 )
		self.tabelSiswa.SetRowSize( 2, 81 )
		self.tabelSiswa.SetRowSize( 3, 65 )
		self.tabelSiswa.SetRowSize( 4, 85 )
		self.tabelSiswa.AutoSizeRows()
		self.tabelSiswa.EnableDragRowSize( True )
		self.tabelSiswa.SetRowLabelSize( 80 )
		self.tabelSiswa.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.tabelSiswa.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		# Cell Defaults
		self.tabelSiswa.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		self.tabelSiswa.SetMaxSize( wx.Size( 1000,-1 ) )
		
		bSizer141.Add( self.tabelSiswa, 0, wx.ALL, 5 )
		
		
		self.m_panelDataSiswa.SetSizer( bSizer141 )
		self.m_panelDataSiswa.Layout()
		bSizer141.Fit( self.m_panelDataSiswa )
		bSizer131.Add( self.m_panelDataSiswa, 1, wx.ALIGN_TOP|wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer131, 10, 0, 5 )
		
		
		self.SetSizer( bSizer13 )
		self.Layout()
		
		# Connect Events
		self.inputNoIdk.Bind( wx.EVT_ERASE_BACKGROUND, self.inputNoIdkOnEraseBackground )
		self.btnTambahSws.Bind( wx.EVT_BUTTON, self.btnTambahSwsOnButtonClick )
		self.btnTambahNilai1.Bind( wx.EVT_BUTTON, self.btnTambahNilai1OnButtonClick )
		self.btnEditNilai.Bind( wx.EVT_BUTTON, self.btnEditNilaiOnButtonClick )
		self.btnHapus.Bind( wx.EVT_BUTTON, self.btnHapusOnButtonClick )
		self.btnCari.Bind( wx.EVT_BUTTON, self.btnCariOnButtonClick )
		self.btnDetailDataSws.Bind( wx.EVT_BUTTON, self.btnDetailDataSwsOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def inputNoIdkOnEraseBackground( self, event ):
		event.Skip()
	
	def btnTambahSwsOnButtonClick( self, event ):
		event.Skip()
	
	def btnTambahNilai1OnButtonClick( self, event ):
		event.Skip()
	
	def btnEditNilaiOnButtonClick( self, event ):
		event.Skip()
	
	def btnHapusOnButtonClick( self, event ):
		event.Skip()
	
	def btnCariOnButtonClick( self, event ):
		event.Skip()
	
	def btnDetailDataSwsOnButtonClick( self, event ):
		event.Skip()
	
	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 0 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 823,645 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		layoutLogin = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelLogin = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelLogin.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText65 = wx.StaticText( self.m_panelLogin, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )
		self.m_staticText65.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer12.Add( self.m_staticText65, 0, wx.ALL, 5 )
		
		self.m_staticText63 = wx.StaticText( self.m_panelLogin, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		self.m_staticText63.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer12.Add( self.m_staticText63, 0, wx.ALL, 5 )
		
		self.m_staticText62 = wx.StaticText( self.m_panelLogin, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		self.m_staticText62.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer12.Add( self.m_staticText62, 0, wx.ALL, 5 )
		
		self.m_staticText60 = wx.StaticText( self.m_panelLogin, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		self.m_staticText60.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer12.Add( self.m_staticText60, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self.m_panelLogin, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		self.m_staticText61.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer12.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.LOGIN = wx.StaticText( self.m_panelLogin, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LOGIN.Wrap( -1 )
		self.LOGIN.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 73, 90, 91, False, "Bahnschrift SemiLight" ) )
		
		bSizer12.Add( self.LOGIN, 0, wx.ALL, 5 )
		
		self.m_panel7 = wx.Panel( self.m_panelLogin, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.Username = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Username.Wrap( -1 )
		fgSizer7.Add( self.Username, 0, wx.ALL, 5 )
		
		self.inputUsername = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.inputUsername, 0, wx.ALL, 5 )
		
		self.Password = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Password.Wrap( -1 )
		fgSizer7.Add( self.Password, 0, wx.ALL, 5 )
		
		self.inputPassword = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer7.Add( self.inputPassword, 0, wx.ALL, 5 )
		
		self.m_buttonLogin = wx.Button( self.m_panel7, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_buttonLogin, 0, wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( fgSizer7 )
		self.m_panel7.Layout()
		fgSizer7.Fit( self.m_panel7 )
		bSizer12.Add( self.m_panel7, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panelLogin.SetSizer( bSizer12 )
		self.m_panelLogin.Layout()
		bSizer12.Fit( self.m_panelLogin )
		layoutLogin.Add( self.m_panelLogin, 0, wx.ALIGN_CENTER, 5 )
		
		
		self.SetSizer( layoutLogin )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MyFrame2OnClose )
		self.Bind( wx.EVT_SIZE, self.MyFrame2OnSize )
		self.m_buttonLogin.Bind( wx.EVT_BUTTON, self.m_buttonLoginOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def MyFrame2OnClose( self, event ):
		event.Skip()
	
	def MyFrame2OnSize( self, event ):
		event.Skip()
	
	def m_buttonLoginOnButtonClick( self, event ):
		event.Skip()
	

