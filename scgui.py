# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class ScGuiMainFrame
###########################################################################

class ScGuiMainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1248,753 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
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
		
		self.txtPlainTextCi = wx.richtext.RichTextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.txtPlainTextCi.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer11.Add( self.txtPlainTextCi, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"KEY:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer9.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.txtKeyCi = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.txtKeyCi.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer9.Add( self.txtKeyCi, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btnEncodeCi = wx.Button( self.m_panel1, wx.ID_ANY, u"Cifrar", wx.DefaultPosition, wx.Size( 350,200 ), wx.NO_BORDER )
		self.btnEncodeCi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.btnEncodeCi.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer9.Add( self.btnEncodeCi, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.ALIGN_BOTTOM, 5 )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText21 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Texto cifrado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer111.Add( self.m_staticText21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.txtCipherTextCi = wx.richtext.RichTextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.txtCipherTextCi.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
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
		
		self.txtCipherTextDe = wx.richtext.RichTextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.txtCipherTextDe.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer112.Add( self.txtCipherTextDe, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer81.Add( bSizer112, 1, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText11 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"KEY:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer91.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.txtKeyDe = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.txtKeyDe.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer91.Add( self.txtKeyDe, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btnDecodeDe = wx.Button( self.m_panel11, wx.ID_ANY, u"Decifrar", wx.DefaultPosition, wx.Size( 350,200 ), wx.NO_BORDER )
		self.btnDecodeDe.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.btnDecodeDe.SetBackgroundColour( wx.Colour( 130, 255, 170 ) )
		
		bSizer91.Add( self.btnDecodeDe, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer81.Add( bSizer91, 1, wx.ALIGN_BOTTOM, 5 )
		
		bSizer1111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText211 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Texto decifrado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		bSizer1111.Add( self.m_staticText211, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.txtDecipherTextDe = wx.richtext.RichTextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.txtDecipherTextDe.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1111.Add( self.txtDecipherTextDe, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer81.Add( bSizer1111, 1, wx.EXPAND, 5 )
		
		
		bSizer41.Add( bSizer81, 1, wx.EXPAND, 5 )
		
		
		self.m_panel11.SetSizer( bSizer41 )
		self.m_panel11.Layout()
		bSizer41.Fit( self.m_panel11 )
		self.m_notebook5.AddPage( self.m_panel11, u"Decifrar", True )
		self.m_panel3 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.m_panel3, u"a page", False )
		
		bSizer1.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnEncodeCi.Bind( wx.EVT_BUTTON, self.cipher )
		self.btnDecodeDe.Bind( wx.EVT_BUTTON, self.decipher )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def cipher( self, event ):
		event.Skip()
	
	def decipher( self, event ):
		event.Skip()
	

