# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext
import wx.grid

###########################################################################
## Class ScGuiMainFrame
###########################################################################

class ScGuiMainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1248,884 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook5 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Texto para cifrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer11.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.txtPlainTextCi = wx.richtext.RichTextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.txtPlainTextCi.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer11.Add( self.txtPlainTextCi, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"KEY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer9.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.txtKeyCi = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.txtKeyCi.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer9.Add( self.txtKeyCi, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.btnEncodeCi = wx.Button( self.m_panel1, wx.ID_ANY, u"Cifrar", wx.DefaultPosition, wx.Size( 350,200 ), wx.BORDER_NONE )
		self.btnEncodeCi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.btnEncodeCi.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer9.Add( self.btnEncodeCi, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer8.Add( bSizer9, 1, wx.ALIGN_BOTTOM, 5 )

		bSizer111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText21 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Texto cifrado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer111.Add( self.m_staticText21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.txtCipherTextCi = wx.richtext.RichTextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.txtCipherTextCi.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer111.Add( self.txtCipherTextCi, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( bSizer111, 1, wx.EXPAND, 5 )


		bSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer4 )
		self.m_panel1.Layout()
		bSizer4.Fit( self.m_panel1 )
		self.m_notebook5.AddPage( self.m_panel1, u"Cifrar", False )
		self.m_panel11 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		bSizer81 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer112 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Texto para decifrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer112.Add( self.m_staticText22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.txtCipherTextDe = wx.richtext.RichTextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.txtCipherTextDe.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer112.Add( self.txtCipherTextDe, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer81.Add( bSizer112, 1, wx.EXPAND, 5 )

		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"KEY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer91.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.txtKeyDe = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.txtKeyDe.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer91.Add( self.txtKeyDe, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.btnDecodeDe = wx.Button( self.m_panel11, wx.ID_ANY, u"Decifrar", wx.DefaultPosition, wx.Size( 350,200 ), wx.BORDER_NONE )
		self.btnDecodeDe.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.btnDecodeDe.SetBackgroundColour( wx.Colour( 130, 255, 170 ) )

		bSizer91.Add( self.btnDecodeDe, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer81.Add( bSizer91, 1, wx.ALIGN_BOTTOM, 5 )

		bSizer1111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText211 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Texto decifrado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		bSizer1111.Add( self.m_staticText211, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.txtDecipherTextDe = wx.richtext.RichTextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_NONE )
		self.txtDecipherTextDe.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1111.Add( self.txtDecipherTextDe, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer81.Add( bSizer1111, 1, wx.EXPAND, 5 )


		bSizer41.Add( bSizer81, 1, wx.EXPAND, 5 )


		self.m_panel11.SetSizer( bSizer41 )
		self.m_panel11.Layout()
		bSizer41.Fit( self.m_panel11 )
		self.m_notebook5.AddPage( self.m_panel11, u"Decifrar", False )
		self.m_panel111 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.txtCipherTextBr1 = wx.richtext.RichTextCtrl( self.m_panel111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,90 ), 0|wx.BORDER_NONE )
		self.txtCipherTextBr1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer22.Add( self.txtCipherTextBr1, 1, wx.EXPAND |wx.ALL, 5 )

		self.btnFreq = wx.Button( self.m_panel111, wx.ID_ANY, u"Frequências", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.btnFreq, 0, wx.ALL, 5 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.gridFrequences = wx.grid.Grid( self.m_panel111, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), 0 )

		# Grid
		self.gridFrequences.CreateGrid( 2, 21 )
		self.gridFrequences.EnableEditing( False )
		self.gridFrequences.EnableGridLines( True )
		self.gridFrequences.EnableDragGridSize( False )
		self.gridFrequences.SetMargins( 0, 0 )

		# Columns
		self.gridFrequences.SetColSize( 0, 100 )
		self.gridFrequences.SetColSize( 1, 100 )
		self.gridFrequences.SetColSize( 2, 12 )
		self.gridFrequences.EnableDragColMove( False )
		self.gridFrequences.EnableDragColSize( False )
		self.gridFrequences.SetColLabelSize( 30 )
		self.gridFrequences.SetColLabelValue( 0, u"Sequencia" )
		self.gridFrequences.SetColLabelValue( 1, u"Espaçamento" )
		self.gridFrequences.SetColLabelValue( 2, u"2" )
		self.gridFrequences.SetColLabelValue( 3, u"3" )
		self.gridFrequences.SetColLabelValue( 4, u"4" )
		self.gridFrequences.SetColLabelValue( 5, u"5" )
		self.gridFrequences.SetColLabelValue( 6, u"6" )
		self.gridFrequences.SetColLabelValue( 7, u"7" )
		self.gridFrequences.SetColLabelValue( 8, u"8" )
		self.gridFrequences.SetColLabelValue( 9, u"9" )
		self.gridFrequences.SetColLabelValue( 10, u"10" )
		self.gridFrequences.SetColLabelValue( 11, u"11" )
		self.gridFrequences.SetColLabelValue( 12, u"12" )
		self.gridFrequences.SetColLabelValue( 13, u"13" )
		self.gridFrequences.SetColLabelValue( 14, u"14" )
		self.gridFrequences.SetColLabelValue( 15, u"15" )
		self.gridFrequences.SetColLabelValue( 16, u"16" )
		self.gridFrequences.SetColLabelValue( 17, u"17" )
		self.gridFrequences.SetColLabelValue( 18, u"18" )
		self.gridFrequences.SetColLabelValue( 19, u"19" )
		self.gridFrequences.SetColLabelValue( 20, u"20" )
		self.gridFrequences.SetColLabelValue( 21, u"12" )
		self.gridFrequences.SetColLabelValue( 22, wx.EmptyString )
		self.gridFrequences.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridFrequences.AutoSizeRows()
		self.gridFrequences.EnableDragRowSize( False )
		self.gridFrequences.SetRowLabelSize( 0 )
		self.gridFrequences.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridFrequences.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer13.Add( self.gridFrequences, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( bSizer13, 1, wx.EXPAND, 5 )

		self.txtMostFreq = wx.richtext.RichTextCtrl( self.m_panel111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,100 ), 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.txtMostFreq.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer22.Add( self.txtMostFreq, 1, wx.ALL, 5 )

		bSizer84 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnGuess = wx.Button( self.m_panel111, wx.ID_ANY, u"Adivinhe", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer84.Add( self.btnGuess, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel111, wx.ID_ANY, u"KEY:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer84.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.txtGuessedKey = wx.TextCtrl( self.m_panel111, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer84.Add( self.txtGuessedKey, 0, wx.ALL, 5 )


		bSizer22.Add( bSizer84, 1, wx.EXPAND, 5 )


		self.m_panel111.SetSizer( bSizer22 )
		self.m_panel111.Layout()
		bSizer22.Fit( self.m_panel111 )
		self.m_notebook5.AddPage( self.m_panel111, u"Quebrar", True )

		bSizer1.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnEncodeCi.Bind( wx.EVT_BUTTON, self.cipher )
		self.btnDecodeDe.Bind( wx.EVT_BUTTON, self.decipher )
		self.btnFreq.Bind( wx.EVT_BUTTON, self.generateKeySize )
		self.btnGuess.Bind( wx.EVT_BUTTON, self.guessKey )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cipher( self, event ):
		event.Skip()

	def decipher( self, event ):
		event.Skip()

	def generateKeySize( self, event ):
		event.Skip()

	def guessKey( self, event ):
		event.Skip()


###########################################################################
## Class diagGuess
###########################################################################

class diagGuess ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 712,634 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Escolha o tamanho da KEY:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer16.Add( self.m_staticText7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn2diag = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn2diag, 0, wx.ALL, 7 )

		self.btn3diag = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn3diag, 0, wx.ALL, 7 )

		self.btn4diag = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn4diag, 0, wx.ALL, 7 )

		self.btn5diag = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn5diag, 0, wx.ALL, 7 )

		self.btn6diag = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn6diag, 0, wx.ALL, 7 )

		self.btn7diag = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn7diag, 0, wx.ALL, 7 )

		self.btn8diag = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn8diag, 0, wx.ALL, 7 )

		self.btn9diag = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn9diag, 0, wx.ALL, 7 )

		self.btn10diag = wx.Button( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn10diag, 0, wx.ALL, 7 )

		self.btn11diag = wx.Button( self, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn11diag, 0, wx.ALL, 7 )

		self.btn12diag = wx.Button( self, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn12diag, 0, wx.ALL, 7 )

		self.btn13diag = wx.Button( self, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn13diag, 0, wx.ALL, 7 )

		self.btn14diag = wx.Button( self, wx.ID_ANY, u"14", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn14diag, 0, wx.ALL, 7 )

		self.btn15diag = wx.Button( self, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn15diag, 0, wx.ALL, 7 )

		self.btn16diag = wx.Button( self, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn16diag, 0, wx.ALL, 7 )

		self.btn17diag = wx.Button( self, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn17diag, 0, wx.ALL, 7 )

		self.btn18diag = wx.Button( self, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn18diag, 0, wx.ALL, 7 )

		self.btn19diag = wx.Button( self, wx.ID_ANY, u"19", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn19diag, 0, wx.ALL, 7 )

		self.btn20diag = wx.Button( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer15.Add( self.btn20diag, 0, wx.ALL, 7 )


		bSizer29.Add( bSizer15, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.SHAPED, 5 )


		bSizer18.Add( bSizer29, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.SHAPED, 5 )

		bSizer151 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey1 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.radCharKey1, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22.Add( self.txtCharKey1, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22, 1, 0, 5 )

		bSizer221 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey2 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.radCharKey2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer221.Add( self.radCharKey2, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer221.Add( self.txtCharKey2, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer221, 1, wx.EXPAND, 5 )

		bSizer222 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey3 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer222.Add( self.radCharKey3, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer222.Add( self.txtCharKey3, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer222, 1, wx.EXPAND, 5 )

		bSizer2221 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey4 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2221.Add( self.radCharKey4, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer2221.Add( self.txtCharKey4, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer2221, 1, wx.EXPAND, 5 )

		bSizer2222 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey5 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2222.Add( self.radCharKey5, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer2222.Add( self.txtCharKey5, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer2222, 1, wx.EXPAND, 5 )

		bSizer2223 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey6 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2223.Add( self.radCharKey6, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer2223.Add( self.txtCharKey6, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer2223, 1, wx.EXPAND, 5 )

		bSizer2224 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey7 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2224.Add( self.radCharKey7, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer2224.Add( self.txtCharKey7, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer2224, 1, wx.EXPAND, 5 )

		bSizer2225 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey8 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2225.Add( self.radCharKey8, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer2225.Add( self.txtCharKey8, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer2225, 1, wx.EXPAND, 5 )

		bSizer2226 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey9 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2226.Add( self.radCharKey9, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer2226.Add( self.txtCharKey9, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer2226, 1, wx.EXPAND, 5 )

		bSizer2227 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey10 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2227.Add( self.radCharKey10, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer2227.Add( self.txtCharKey10, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer2227, 1, wx.EXPAND, 5 )

		bSizer22272 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey11 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22272.Add( self.radCharKey11, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22272.Add( self.txtCharKey11, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22272, 1, wx.EXPAND, 5 )

		bSizer22273 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey12 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22273.Add( self.radCharKey12, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22273.Add( self.txtCharKey12, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22273, 1, wx.EXPAND, 5 )

		bSizer22274 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey13 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22274.Add( self.radCharKey13, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22274.Add( self.txtCharKey13, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22274, 1, wx.EXPAND, 5 )

		bSizer22275 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey14 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22275.Add( self.radCharKey14, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22275.Add( self.txtCharKey14, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22275, 1, wx.EXPAND, 5 )

		bSizer22276 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey15 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22276.Add( self.radCharKey15, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22276.Add( self.txtCharKey15, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22276, 1, wx.EXPAND, 5 )

		bSizer22277 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey16 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22277.Add( self.radCharKey16, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22277.Add( self.txtCharKey16, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22277, 1, wx.EXPAND, 5 )

		bSizer22278 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey17 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22278.Add( self.radCharKey17, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22278.Add( self.txtCharKey17, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22278, 1, wx.EXPAND, 5 )

		bSizer22271 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey18 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22271.Add( self.radCharKey18, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22271.Add( self.txtCharKey18, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22271, 1, wx.EXPAND, 5 )

		bSizer22279 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey19 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22279.Add( self.radCharKey19, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer22279.Add( self.txtCharKey19, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer22279, 1, wx.EXPAND, 5 )

		bSizer222791 = wx.BoxSizer( wx.VERTICAL )

		self.radCharKey20 = wx.RadioButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer222791.Add( self.radCharKey20, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.txtCharKey20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer222791.Add( self.txtCharKey20, 0, wx.ALIGN_CENTER|wx.ALL, 2 )


		bSizer26.Add( bSizer222791, 1, wx.EXPAND, 5 )


		bSizer151.Add( bSizer26, 1, wx.SHAPED, 5 )


		bSizer18.Add( bSizer151, 1, wx.ALIGN_CENTER, 5 )


		bSizer16.Add( bSizer18, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer83 = wx.BoxSizer( wx.VERTICAL )

		self.btnPlot = wx.Button( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer83.Add( self.btnPlot, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.SHAPED, 5 )

		self.btnShiftPlot = wx.Button( self, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer83.Add( self.btnShiftPlot, 0, wx.ALL, 5 )

		self.btnSet = wx.Button( self, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer83.Add( self.btnSet, 0, wx.ALL, 5 )


		bSizer16.Add( bSizer83, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer14.Add( bSizer16, 1, wx.EXPAND|wx.SHAPED, 5 )

		self.btnOkDiag = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.btnOkDiag, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn2diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn3diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn4diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn5diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn6diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn7diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn8diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn9diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn10diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn11diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn12diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn13diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn14diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn15diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn16diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn17diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn18diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn19diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.btn20diag.Bind( wx.EVT_BUTTON, self.selectKeySize )
		self.radCharKey1.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey2.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey3.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey4.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey5.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey6.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey7.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey8.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey9.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey10.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey11.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey12.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey13.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey14.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey15.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey16.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey17.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey18.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey19.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.radCharKey20.Bind( wx.EVT_RADIOBUTTON, self.selectKeyIndex )
		self.btnPlot.Bind( wx.EVT_BUTTON, self.plotFreq )
		self.btnShiftPlot.Bind( wx.EVT_BUTTON, self.shiftPlot )
		self.btnSet.Bind( wx.EVT_BUTTON, self.setCharKey )
		self.btnOkDiag.Bind( wx.EVT_BUTTON, self.getGuessedKey )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def selectKeySize( self, event ):
		event.Skip()



















	def selectKeyIndex( self, event ):
		event.Skip()




















	def plotFreq( self, event ):
		event.Skip()

	def shiftPlot( self, event ):
		event.Skip()

	def setCharKey( self, event ):
		event.Skip()

	def getGuessedKey( self, event ):
		event.Skip()


