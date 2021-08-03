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
		
		self.m_richText1 = wx.richtext.RichTextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer11.Add( self.m_richText1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"KEY:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer9.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		bSizer9.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btnEncode = wx.Button( self.m_panel1, wx.ID_ANY, u"Cifrar", wx.DefaultPosition, wx.Size( 350,200 ), wx.NO_BORDER )
		self.btnEncode.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
		self.btnEncode.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer9.Add( self.btnEncode, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.ALIGN_BOTTOM, 5 )
		
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText21 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Texto cifrado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer111.Add( self.m_staticText21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_richText12 = wx.richtext.RichTextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		bSizer111.Add( self.m_richText12, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer111, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer4 )
		self.m_panel1.Layout()
		bSizer4.Fit( self.m_panel1 )
		self.m_notebook5.AddPage( self.m_panel1, u"a page", True )
		self.m_panel2 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.m_panel2, u"a page", False )
		self.m_panel3 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.m_panel3, u"a page", False )
		
		bSizer1.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnEncode.Bind( wx.EVT_BUTTON, self.teste )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def teste( self, event ):
		event.Skip()
	

