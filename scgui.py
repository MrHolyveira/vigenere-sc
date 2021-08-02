# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ScGuiMainFrame
###########################################################################

class ScGuiMainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 770,484 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook5 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnGenerate = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnGenerate, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 1, 0, 5 )
		
		
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
	
	def __del__( self ):
		pass
	

