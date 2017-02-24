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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ggplot2 - Command Generator", pos = wx.DefaultPosition, size = wx.Size( 1199,779 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 240 ) )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Data Frame:", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer4.Add( self.m_textCtrl1, 0, wx.ALL, 1 )
		
		
		bSizer2.Add( bSizer4, 0, 0, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Geom:", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer41.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choice1Choices = [ u"geom_line", u"geom_abline", u"geom_bar" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice1Choices, wx.CB_SORT )
		self.m_choice1.SetSelection( 0 )
		bSizer41.Add( self.m_choice1, 0, wx.ALL, 1 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer41.Add( bSizer8, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.Add( bSizer41, 0, 0, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Aesthetics:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText116 = wx.StaticText( self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText116.Wrap( -1 )
		bSizer10.Add( self.m_staticText116, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_x = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer10.Add( self.aes_x, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer14.Add( bSizer10, 0, 0, 0 )
		
		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"y", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText111.Wrap( -1 )
		bSizer101.Add( self.m_staticText111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_y = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer101.Add( self.aes_y, 0, wx.ALL, 1 )
		
		
		bSizer14.Add( bSizer101, 0, 0, 5 )
		
		bSizer102 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText112 = wx.StaticText( self, wx.ID_ANY, u"group", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText112.Wrap( -1 )
		bSizer102.Add( self.m_staticText112, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_group = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer102.Add( self.aes_group, 0, wx.ALL, 1 )
		
		
		bSizer14.Add( bSizer102, 0, 0, 5 )
		
		bSizer103 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText113 = wx.StaticText( self, wx.ID_ANY, u"color", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText113.Wrap( -1 )
		bSizer103.Add( self.m_staticText113, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_color = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer103.Add( self.aes_color, 0, wx.ALL, 1 )
		
		
		bSizer14.Add( bSizer103, 0, 0, 5 )
		
		bSizer104 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText114 = wx.StaticText( self, wx.ID_ANY, u"linetype", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText114.Wrap( -1 )
		bSizer104.Add( self.m_staticText114, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_linetype = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer104.Add( self.aes_linetype, 0, wx.ALL, 1 )
		
		
		bSizer14.Add( bSizer104, 0, 0, 5 )
		
		
		bSizer14.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer105 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText115 = wx.StaticText( self, wx.ID_ANY, u"size", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText115.Wrap( -1 )
		bSizer105.Add( self.m_staticText115, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_size = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer105.Add( self.aes_size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer15.Add( bSizer105, 0, 0, 5 )
		
		bSizer1051 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1151 = wx.StaticText( self, wx.ID_ANY, u"alpha", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1151.Wrap( -1 )
		bSizer1051.Add( self.m_staticText1151, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_alpha = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer1051.Add( self.aes_alpha, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer15.Add( bSizer1051, 0, 0, 5 )
		
		bSizer10511 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11511 = wx.StaticText( self, wx.ID_ANY, u"weight", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText11511.Wrap( -1 )
		bSizer10511.Add( self.m_staticText11511, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_weight = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer10511.Add( self.aes_weight, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer15.Add( bSizer10511, 0, 0, 5 )
		
		bSizer105111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText115111 = wx.StaticText( self, wx.ID_ANY, u"fill", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText115111.Wrap( -1 )
		bSizer105111.Add( self.m_staticText115111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_fill = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer105111.Add( self.aes_fill, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer15.Add( bSizer105111, 0, 0, 5 )
		
		
		bSizer15.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Faceting:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		self.m_staticText42.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer52.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer52.AddSpacer( ( 25, 0), 1, wx.EXPAND, 5 )
		
		self.m_checkBox7 = wx.CheckBox( self, wx.ID_ANY, u"Facet Wrap", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer52.Add( self.m_checkBox7, 0, wx.ALL, 5 )
		
		
		bSizer52.AddSpacer( ( 25, 0), 1, wx.EXPAND, 5 )
		
		self.m_checkBox8 = wx.CheckBox( self, wx.ID_ANY, u"Facet Grid", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer52.Add( self.m_checkBox8, 0, wx.ALL, 5 )
		
		
		bSizer51.Add( bSizer52, 0, 0, 5 )
		
		bSizer79 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer142 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer107 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1162 = wx.StaticText( self, wx.ID_ANY, u"facets", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1162.Wrap( -1 )
		bSizer107.Add( self.m_staticText1162, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_x2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.aes_x2.Enable( False )
		
		bSizer107.Add( self.aes_x2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer142.Add( bSizer107, 0, 0, 0 )
		
		bSizer1012 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1112 = wx.StaticText( self, wx.ID_ANY, u"margins", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1112.Wrap( -1 )
		bSizer1012.Add( self.m_staticText1112, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_checkBox9 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox9.Enable( False )
		
		bSizer1012.Add( self.m_checkBox9, 0, wx.ALL, 5 )
		
		
		bSizer142.Add( bSizer1012, 0, 0, 5 )
		
		bSizer1022 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1122 = wx.StaticText( self, wx.ID_ANY, u"scales", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1122.Wrap( -1 )
		bSizer1022.Add( self.m_staticText1122, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		m_comboBox4Choices = [ u"fixed", u"free_x", u"free_y", u"free" ]
		self.m_comboBox4 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 150,-1 ), m_comboBox4Choices, wx.CB_DROPDOWN )
		self.m_comboBox4.SetSelection( 0 )
		self.m_comboBox4.Enable( False )
		
		bSizer1022.Add( self.m_comboBox4, 1, wx.ALL|wx.EXPAND, 1 )
		
		
		bSizer142.Add( bSizer1022, 0, 0, 5 )
		
		bSizer1031 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1131 = wx.StaticText( self, wx.ID_ANY, u"space", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1131.Wrap( -1 )
		bSizer1031.Add( self.m_staticText1131, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		m_comboBox41Choices = [ u"fixed", u"free_x", u"free_y", u"free" ]
		self.m_comboBox41 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 150,-1 ), m_comboBox41Choices, wx.CB_DROPDOWN )
		self.m_comboBox41.SetSelection( 0 )
		self.m_comboBox41.Enable( False )
		
		bSizer1031.Add( self.m_comboBox41, 0, wx.ALL, 1 )
		
		
		bSizer142.Add( bSizer1031, 0, 0, 5 )
		
		
		bSizer142.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer79.Add( bSizer142, 1, wx.EXPAND, 5 )
		
		bSizer1421 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1071 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11621 = wx.StaticText( self, wx.ID_ANY, u"drop", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText11621.Wrap( -1 )
		bSizer1071.Add( self.m_staticText11621, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_checkBox92 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox92.Enable( False )
		
		bSizer1071.Add( self.m_checkBox92, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1071.AddSpacer( ( 10, 0), 0, wx.EXPAND, 0 )
		
		
		bSizer1421.Add( bSizer1071, 0, 0, 0 )
		
		bSizer10121 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer1421.Add( bSizer10121, 0, 0, 5 )
		
		bSizer10221 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11221 = wx.StaticText( self, wx.ID_ANY, u"nrow", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText11221.Wrap( -1 )
		bSizer10221.Add( self.m_staticText11221, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_textCtrl48 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		self.m_textCtrl48.Enable( False )
		
		bSizer10221.Add( self.m_textCtrl48, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_staticText11311 = wx.StaticText( self, wx.ID_ANY, u"ncol", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText11311.Wrap( -1 )
		bSizer10221.Add( self.m_staticText11311, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_textCtrl49 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		self.m_textCtrl49.Enable( False )
		
		bSizer10221.Add( self.m_textCtrl49, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer1421.Add( bSizer10221, 0, 0, 5 )
		
		
		bSizer1421.AddSpacer( ( 0, 0), 0, wx.EXPAND, 5 )
		
		bSizer1041 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1141 = wx.StaticText( self, wx.ID_ANY, u"labeller", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1141.Wrap( -1 )
		bSizer1041.Add( self.m_staticText1141, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		m_comboBox16Choices = [ u"label_value", u"label_both", u"label_bquote", u"label_parsed", u"(custom...)" ]
		self.m_comboBox16 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox16Choices, 0 )
		self.m_comboBox16.SetSelection( 0 )
		self.m_comboBox16.Enable( False )
		
		bSizer1041.Add( self.m_comboBox16, 1, wx.ALL|wx.EXPAND, 1 )
		
		
		bSizer1421.Add( bSizer1041, 0, wx.EXPAND, 5 )
		
		bSizer10411 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11411 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText11411.Wrap( -1 )
		bSizer10411.Add( self.m_staticText11411, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_linetype11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.aes_linetype11.Enable( False )
		
		bSizer10411.Add( self.aes_linetype11, 0, wx.ALL, 1 )
		
		
		bSizer1421.Add( bSizer10411, 1, wx.EXPAND, 5 )
		
		
		bSizer79.Add( bSizer1421, 0, wx.EXPAND, 5 )
		
		
		bSizer51.Add( bSizer79, 0, 0, 5 )
		
		
		bSizer2.Add( bSizer51, 0, wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer131 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Theme:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		self.m_staticText51.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer45.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		
		bSizer45.AddSpacer( ( 10, 0), 1, wx.EXPAND, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"B/W", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Grey", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.m_checkBox2, 0, wx.ALL, 5 )
		
		
		bSizer141.Add( bSizer45, 0, wx.EXPAND, 5 )
		
		bSizer96 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer96.AddSpacer( ( 1, 0), 1, wx.EXPAND, 5 )
		
		self.m_checkBox17 = wx.CheckBox( self, wx.ID_ANY, u"Minimal", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer96.Add( self.m_checkBox17, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_checkBox18 = wx.CheckBox( self, wx.ID_ANY, u"Classic", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer96.Add( self.m_checkBox18, 0, wx.ALL, 5 )
		
		
		bSizer141.Add( bSizer96, 1, wx.EXPAND, 5 )
		
		bSizer106 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1161 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1161.Wrap( -1 )
		bSizer106.Add( self.m_staticText1161, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_x1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer106.Add( self.aes_x1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer141.Add( bSizer106, 0, 0, 0 )
		
		bSizer1011 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1111 = wx.StaticText( self, wx.ID_ANY, u"X Label", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1111.Wrap( -1 )
		bSizer1011.Add( self.m_staticText1111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_y1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer1011.Add( self.aes_y1, 0, wx.ALL, 1 )
		
		
		bSizer141.Add( bSizer1011, 0, 0, 5 )
		
		bSizer1021 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1121 = wx.StaticText( self, wx.ID_ANY, u"Y Label", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1121.Wrap( -1 )
		bSizer1021.Add( self.m_staticText1121, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_group1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer1021.Add( self.aes_group1, 0, wx.ALL, 1 )
		
		
		bSizer141.Add( bSizer1021, 0, 0, 5 )
		
		
		bSizer131.Add( bSizer141, 0, 0, 5 )
		
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer451 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText511 = wx.StaticText( self, wx.ID_ANY, u"Legend:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText511.Wrap( -1 )
		self.m_staticText511.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer451.Add( self.m_staticText511, 0, wx.ALL, 5 )
		
		
		bSizer451.AddSpacer( ( 10, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer151.Add( bSizer451, 1, wx.EXPAND, 5 )
		
		bSizer1052 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1152 = wx.StaticText( self, wx.ID_ANY, u"Position", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1152.Wrap( -1 )
		bSizer1052.Add( self.m_staticText1152, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		m_comboBox1Choices = [ u"none", u"top", u"bottom", u"left", u"right", u"(manual)", u"manual" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, wx.CB_DROPDOWN )
		self.m_comboBox1.SetSelection( 2 )
		bSizer1052.Add( self.m_comboBox1, 0, wx.ALL, 1 )
		
		self.aes_size1 = wx.TextCtrl( self, wx.ID_ANY, u"c(X,Y)", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.aes_size1.Enable( False )
		
		bSizer1052.Add( self.aes_size1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer151.Add( bSizer1052, 0, wx.EXPAND, 5 )
		
		bSizer10512 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11512 = wx.StaticText( self, wx.ID_ANY, u"Direction", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText11512.Wrap( -1 )
		bSizer10512.Add( self.m_staticText11512, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		m_comboBox2Choices = [ u"horizontal", u"vertical" ]
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		self.m_comboBox2.SetSelection( 1 )
		bSizer10512.Add( self.m_comboBox2, 0, wx.ALL, 1 )
		
		
		bSizer151.Add( bSizer10512, 0, 0, 5 )
		
		bSizer105112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText115112 = wx.StaticText( self, wx.ID_ANY, u"Rows", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText115112.Wrap( -1 )
		bSizer105112.Add( self.m_staticText115112, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_weight1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer105112.Add( self.aes_weight1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_staticText1151121 = wx.StaticText( self, wx.ID_ANY, u"Cols", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1151121.Wrap( -1 )
		bSizer105112.Add( self.m_staticText1151121, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_textCtrl29 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer105112.Add( self.m_textCtrl29, 0, wx.ALL, 1 )
		
		
		bSizer151.Add( bSizer105112, 0, wx.EXPAND, 5 )
		
		bSizer1051111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1151111 = wx.StaticText( self, wx.ID_ANY, u"Leg. Title", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText1151111.Wrap( -1 )
		bSizer1051111.Add( self.m_staticText1151111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.aes_fill1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer1051111.Add( self.aes_fill1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer151.Add( bSizer1051111, 0, 0, 5 )
		
		
		bSizer131.Add( bSizer151, 0, 0, 5 )
		
		
		bSizer2.Add( bSizer131, 0, 0, 5 )
		
		bSizer49 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Add Theme Element:", wx.DefaultPosition, wx.Size( 125,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText40.Wrap( -1 )
		bSizer49.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		m_comboBox3Choices = []
		self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		bSizer49.Add( self.m_comboBox3, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer49.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer2.Add( bSizer49, 0, wx.EXPAND, 5 )
		
		bSizer50 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Elements:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		bSizer50.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 1, 2 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( True )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.SetColSize( 0, 92 )
		self.m_grid1.SetColSize( 1, 311 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 0 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( False )
		self.m_grid1.SetRowLabelSize( 0 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer50.Add( self.m_grid1, 0, wx.ALL|wx.EXPAND, 1 )
		
		
		bSizer2.Add( bSizer50, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 0, 0, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1411 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1142 = wx.StaticText( self, wx.ID_ANY, u"Scales:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1142.Wrap( -1 )
		self.m_staticText1142.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer1411.Add( self.m_staticText1142, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer1411, 0, wx.EXPAND, 5 )
		
		bSizer1422 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer145 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer145.AddSpacer( ( 0, 5), 0, 0, 5 )
		
		self.m_staticText1153 = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1153.Wrap( -1 )
		bSizer145.Add( self.m_staticText1153, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer145.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer1422.Add( bSizer145, 0, wx.EXPAND, 5 )
		
		bSizer143 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer144 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer114 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11531 = wx.StaticText( self, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11531.Wrap( -1 )
		bSizer114.Add( self.m_staticText11531, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox27Choices = [ u"scale_x_continuous", u"scale_x_log10", u"scale_x_reverse", u"scale_x_sqrt", u"scale_x_date", u"scale_x_datetime", u"scale_x_discrete", u"scale_x_", wx.EmptyString ]
		self.m_comboBox27 = wx.ComboBox( self, wx.ID_ANY, u"scale_x_continuous", wx.DefaultPosition, wx.Size( 150,-1 ), m_comboBox27Choices, 0 )
		self.m_comboBox27.SetSelection( 0 )
		bSizer114.Add( self.m_comboBox27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Set Parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer114.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer144.Add( bSizer114, 0, wx.EXPAND, 5 )
		
		bSizer1141 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText115311 = wx.StaticText( self, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText115311.Wrap( -1 )
		bSizer1141.Add( self.m_staticText115311, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox271Choices = [ u"scale_x_continuous", u"scale_x_log10", u"scale_x_reverse", u"scale_x_sqrt", u"scale_x_date", u"scale_x_datetime", u"scale_x_discrete", u"scale_x_", wx.EmptyString ]
		self.m_comboBox271 = wx.ComboBox( self, wx.ID_ANY, u"scale_x_continuous", wx.DefaultPosition, wx.Size( 150,-1 ), m_comboBox271Choices, 0 )
		self.m_comboBox271.SetSelection( 0 )
		bSizer1141.Add( self.m_comboBox271, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button121 = wx.Button( self, wx.ID_ANY, u"Set Parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button121.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1141.Add( self.m_button121, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer144.Add( bSizer1141, 0, wx.EXPAND, 5 )
		
		
		bSizer143.Add( bSizer144, 1, wx.EXPAND, 5 )
		
		
		bSizer1422.Add( bSizer143, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer1422, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer1.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer140 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer140.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer140, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_comboBox16.Bind( wx.EVT_COMBOBOX, self.set_labeller )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.check_theme_bw )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.check_theme_grey )
		self.m_checkBox17.Bind( wx.EVT_CHECKBOX, self.check_theme_minimal )
		self.m_checkBox18.Bind( wx.EVT_CHECKBOX, self.check_theme_classic )
		self.m_comboBox1.Bind( wx.EVT_COMBOBOX, self.set_legend_pos )
		self.m_comboBox2.Bind( wx.EVT_COMBOBOX, self.set_legend_dir )
		self.m_button1.Bind( wx.EVT_BUTTON, self.add_theme_element )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def set_labeller( self, event ):
		event.Skip()
	
	def check_theme_bw( self, event ):
		event.Skip()
	
	def check_theme_grey( self, event ):
		event.Skip()
	
	def check_theme_minimal( self, event ):
		event.Skip()
	
	def check_theme_classic( self, event ):
		event.Skip()
	
	def set_legend_pos( self, event ):
		event.Skip()
	
	def set_legend_dir( self, event ):
		event.Skip()
	
	def add_theme_element( self, event ):
		event.Skip()
	

###########################################################################
## Class DialogElemLne
###########################################################################

class DialogElemLne ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Line Element", pos = wx.DefaultPosition, size = wx.Size( 328,337 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer97 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText75 = wx.StaticText( self, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText75.Wrap( -1 )
		bSizer98.Add( self.m_staticText75, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"R Color", wx.DefaultPosition, wx.Size( 75,-1 ), wx.ALIGN_CENTRE|wx.RAISED_BORDER )
		self.m_staticText91.Wrap( -1 )
		self.m_staticText91.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer98.Add( self.m_staticText91, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_checkBox191 = wx.CheckBox( self, wx.ID_ANY, u"set RGB", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer98.Add( self.m_checkBox191, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPicker1 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.m_colourPicker1.Enable( False )
		
		bSizer98.Add( self.m_colourPicker1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer98, 0, 0, 5 )
		
		bSizer99 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText76 = wx.StaticText( self, wx.ID_ANY, u"Size", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText76.Wrap( -1 )
		bSizer99.Add( self.m_staticText76, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl52 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer99.Add( self.m_textCtrl52, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer99, 0, 0, 5 )
		
		bSizer991 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText761 = wx.StaticText( self, wx.ID_ANY, u"Line Type", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText761.Wrap( -1 )
		bSizer991.Add( self.m_staticText761, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox17Choices = [ u"0 = blank", u"1 = solid", u"2 = dashed", u"3 = dotted", u"4 = dotdash", u"5 = longdash", u"6 = twodash", u"(custom, enter string)", wx.EmptyString, wx.EmptyString ]
		self.m_comboBox17 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox17Choices, wx.CB_DROPDOWN )
		self.m_comboBox17.SetSelection( 0 )
		bSizer991.Add( self.m_comboBox17, 0, wx.ALL, 5 )
		
		self.m_textCtrl521 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.m_textCtrl521.Enable( False )
		
		bSizer991.Add( self.m_textCtrl521, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer991, 0, 0, 5 )
		
		bSizer992 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText762 = wx.StaticText( self, wx.ID_ANY, u"Line End", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText762.Wrap( -1 )
		bSizer992.Add( self.m_staticText762, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox18Choices = [ u"butt", u"round", u"square", u"squre" ]
		self.m_comboBox18 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox18Choices, 0 )
		self.m_comboBox18.SetSelection( 0 )
		bSizer992.Add( self.m_comboBox18, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer992, 0, 0, 5 )
		
		bSizer105 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText80 = wx.StaticText( self, wx.ID_ANY, u"R String:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )
		self.m_staticText80.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer105.Add( self.m_staticText80, 0, wx.ALL, 5 )
		
		self.m_textCtrl56 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer105.Add( self.m_textCtrl56, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer97.Add( bSizer105, 1, wx.EXPAND, 5 )
		
		bSizer106 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer106.Add( self.m_button2, 1, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer106.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer106, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer97 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_staticText91.Bind( wx.EVT_RIGHT_DOWN, self.choose_r_color )
		self.m_checkBox191.Bind( wx.EVT_CHECKBOX, self.eline_setrgb_check )
		self.m_colourPicker1.Bind( wx.EVT_COLOURPICKER_CHANGED, self.eline_recalc )
		self.m_textCtrl52.Bind( wx.EVT_TEXT, self.eline_recalc )
		self.m_comboBox17.Bind( wx.EVT_COMBOBOX, self.eline_recalc )
		self.m_comboBox17.Bind( wx.EVT_TEXT, self.eline_recalc )
		self.m_textCtrl521.Bind( wx.EVT_TEXT, self.eline_recalc )
		self.m_comboBox18.Bind( wx.EVT_COMBOBOX, self.eline_recalc )
		self.m_button2.Bind( wx.EVT_BUTTON, self.eline_return )
		self.m_button3.Bind( wx.EVT_BUTTON, self.eline_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def choose_r_color( self, event ):
		event.Skip()
	
	def eline_setrgb_check( self, event ):
		event.Skip()
	
	def eline_recalc( self, event ):
		event.Skip()
	
	
	
	
	
	
	def eline_return( self, event ):
		event.Skip()
	
	def eline_cancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Dialog_Continuous_Scale
###########################################################################

class Dialog_Continuous_Scale ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Continuous Scale", pos = wx.DefaultPosition, size = wx.Size( 568,543 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer78 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer78.AddSpacer( ( 0, 5), 0, 0, 5 )
		
		bSizer79 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"Aesthetic: ", wx.DefaultPosition, wx.Size( 75,-1 ), wx.ALIGN_LEFT )
		self.m_staticText56.Wrap( -1 )
		self.m_staticText56.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer79.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		bSizer79.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer78.Add( bSizer79, 0, wx.EXPAND, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer78.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer80 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"minor_breaks", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText58.Wrap( -1 )
		bSizer80.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_textCtrl49 = wx.TextCtrl( self, wx.ID_ANY, u"(used only with datetime scales)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl49.Enable( False )
		
		bSizer80.Add( self.m_textCtrl49, 1, wx.ALL, 1 )
		
		
		bSizer78.Add( bSizer80, 0, wx.EXPAND, 5 )
		
		bSizer801 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText581 = wx.StaticText( self, wx.ID_ANY, u"limits:", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText581.Wrap( -1 )
		bSizer801.Add( self.m_staticText581, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_staticText70 = wx.StaticText( self, wx.ID_ANY, u"Min", wx.DefaultPosition, wx.Size( 35,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText70.Wrap( -1 )
		bSizer801.Add( self.m_staticText70, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_textCtrl33 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer801.Add( self.m_textCtrl33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Max", wx.DefaultPosition, wx.Size( 35,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText71.Wrap( -1 )
		bSizer801.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_textCtrl34 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer801.Add( self.m_textCtrl34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer78.Add( bSizer801, 0, wx.EXPAND, 5 )
		
		bSizer802 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText582 = wx.StaticText( self, wx.ID_ANY, u"breaks", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText582.Wrap( -1 )
		bSizer802.Add( self.m_staticText582, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_textCtrl37 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer802.Add( self.m_textCtrl37, 1, wx.ALL, 1 )
		
		
		bSizer78.Add( bSizer802, 0, wx.EXPAND, 5 )
		
		bSizer803 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText583 = wx.StaticText( self, wx.ID_ANY, u"labels", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText583.Wrap( -1 )
		bSizer803.Add( self.m_staticText583, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_textCtrl371 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer803.Add( self.m_textCtrl371, 1, wx.ALL, 1 )
		
		
		bSizer78.Add( bSizer803, 0, wx.EXPAND, 5 )
		
		bSizer804 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText584 = wx.StaticText( self, wx.ID_ANY, u"oob", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText584.Wrap( -1 )
		bSizer804.Add( self.m_staticText584, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		m_comboBox11Choices = [ u"censor", u"squish" ]
		self.m_comboBox11 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 100,-1 ), m_comboBox11Choices, 0 )
		self.m_comboBox11.SetSelection( 0 )
		bSizer804.Add( self.m_comboBox11, 0, wx.ALL, 1 )
		
		
		bSizer78.Add( bSizer804, 0, wx.EXPAND, 5 )
		
		bSizer805 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText585 = wx.StaticText( self, wx.ID_ANY, u"palette", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText585.Wrap( -1 )
		bSizer805.Add( self.m_staticText585, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer805.Add( self.m_textCtrl41, 0, wx.ALL, 1 )
		
		
		bSizer78.Add( bSizer805, 0, wx.EXPAND, 5 )
		
		bSizer806 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText586 = wx.StaticText( self, wx.ID_ANY, u"name", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText586.Wrap( -1 )
		bSizer806.Add( self.m_staticText586, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_textCtrl42 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer806.Add( self.m_textCtrl42, 0, wx.ALL, 1 )
		
		
		bSizer78.Add( bSizer806, 0, wx.EXPAND, 5 )
		
		bSizer807 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText587 = wx.StaticText( self, wx.ID_ANY, u"rescaler", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText587.Wrap( -1 )
		bSizer807.Add( self.m_staticText587, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		m_comboBox12Choices = [ u"rescale", u"(custom)" ]
		self.m_comboBox12 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.Size( 100,-1 ), m_comboBox12Choices, 0 )
		self.m_comboBox12.SetSelection( 0 )
		bSizer807.Add( self.m_comboBox12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_textCtrl43 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_textCtrl43.Enable( False )
		
		bSizer807.Add( self.m_textCtrl43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer78.Add( bSizer807, 0, wx.EXPAND, 5 )
		
		bSizer8061 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5861 = wx.StaticText( self, wx.ID_ANY, u"scale_name", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText5861.Wrap( -1 )
		bSizer8061.Add( self.m_staticText5861, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_textCtrl45 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer8061.Add( self.m_textCtrl45, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer78.Add( bSizer8061, 0, wx.EXPAND, 5 )
		
		bSizer8062 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5862 = wx.StaticText( self, wx.ID_ANY, u"guide", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText5862.Wrap( -1 )
		bSizer8062.Add( self.m_staticText5862, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_textCtrl46 = wx.TextCtrl( self, wx.ID_ANY, u"guide_legend", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl46.Enable( False )
		self.m_textCtrl46.SetToolTipString( u"disabled for now because I don't fully understand guides" )
		
		bSizer8062.Add( self.m_textCtrl46, 0, wx.ALL, 1 )
		
		
		bSizer78.Add( bSizer8062, 0, wx.EXPAND, 5 )
		
		bSizer80621 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText58621 = wx.StaticText( self, wx.ID_ANY, u"expand", wx.DefaultPosition, wx.Size( 90,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText58621.Wrap( -1 )
		bSizer80621.Add( self.m_staticText58621, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.m_staticText77 = wx.StaticText( self, wx.ID_ANY, u"Mult", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText77.Wrap( -1 )
		bSizer80621.Add( self.m_staticText77, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_textCtrl35 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer80621.Add( self.m_textCtrl35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_staticText78 = wx.StaticText( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText78.Wrap( -1 )
		bSizer80621.Add( self.m_staticText78, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_textCtrl36 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		bSizer80621.Add( self.m_textCtrl36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		
		bSizer78.Add( bSizer80621, 0, wx.EXPAND, 5 )
		
		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer78.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer105 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText80 = wx.StaticText( self, wx.ID_ANY, u"R String:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )
		self.m_staticText80.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer105.Add( self.m_staticText80, 0, wx.ALL, 5 )
		
		self.m_textCtrl56 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl56.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer105.Add( self.m_textCtrl56, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer105, 1, wx.EXPAND, 5 )
		
		bSizer106 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer106.Add( self.m_button2, 1, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer106.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer78.Add( bSizer106, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer78 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.eline_return )
		self.m_button3.Bind( wx.EVT_BUTTON, self.eline_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def eline_return( self, event ):
		event.Skip()
	
	def eline_cancel( self, event ):
		event.Skip()
	

###########################################################################
## Class DialogElemRect
###########################################################################

class DialogElemRect ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Rectangle Element", pos = wx.DefaultPosition, size = wx.Size( 328,337 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer97 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer981 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText751 = wx.StaticText( self, wx.ID_ANY, u"Fill", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText751.Wrap( -1 )
		bSizer981.Add( self.m_staticText751, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText911 = wx.StaticText( self, wx.ID_ANY, u"R Color", wx.DefaultPosition, wx.Size( 75,-1 ), wx.ALIGN_CENTRE|wx.RAISED_BORDER )
		self.m_staticText911.Wrap( -1 )
		self.m_staticText911.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer981.Add( self.m_staticText911, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_checkBox191 = wx.CheckBox( self, wx.ID_ANY, u"set RGB", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer981.Add( self.m_checkBox191, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPicker11 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.m_colourPicker11.Enable( False )
		
		bSizer981.Add( self.m_colourPicker11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer981, 0, 0, 5 )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText75 = wx.StaticText( self, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText75.Wrap( -1 )
		bSizer98.Add( self.m_staticText75, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"R Color", wx.DefaultPosition, wx.Size( 75,-1 ), wx.ALIGN_CENTRE|wx.RAISED_BORDER )
		self.m_staticText91.Wrap( -1 )
		self.m_staticText91.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer98.Add( self.m_staticText91, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1 )
		
		self.m_checkBox19 = wx.CheckBox( self, wx.ID_ANY, u"set RGB", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer98.Add( self.m_checkBox19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_colourPicker1 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.m_colourPicker1.Enable( False )
		
		bSizer98.Add( self.m_colourPicker1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer98, 0, 0, 5 )
		
		bSizer99 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText76 = wx.StaticText( self, wx.ID_ANY, u"Size", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText76.Wrap( -1 )
		bSizer99.Add( self.m_staticText76, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl52 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer99.Add( self.m_textCtrl52, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer99, 0, 0, 5 )
		
		bSizer991 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText761 = wx.StaticText( self, wx.ID_ANY, u"Line Type", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText761.Wrap( -1 )
		bSizer991.Add( self.m_staticText761, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_comboBox17Choices = [ u"0 = blank", u"1 = solid", u"2 = dashed", u"3 = dotted", u"4 = dotdash", u"5 = longdash", u"6 = twodash", u"(custom, enter string)", wx.EmptyString, wx.EmptyString ]
		self.m_comboBox17 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox17Choices, wx.CB_DROPDOWN )
		self.m_comboBox17.SetSelection( 0 )
		bSizer991.Add( self.m_comboBox17, 0, wx.ALL, 5 )
		
		self.m_textCtrl521 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.m_textCtrl521.Enable( False )
		
		bSizer991.Add( self.m_textCtrl521, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer991, 0, 0, 5 )
		
		bSizer105 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText80 = wx.StaticText( self, wx.ID_ANY, u"R String:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )
		self.m_staticText80.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer105.Add( self.m_staticText80, 0, wx.ALL, 5 )
		
		self.m_textCtrl56 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer105.Add( self.m_textCtrl56, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer97.Add( bSizer105, 1, wx.EXPAND, 5 )
		
		bSizer106 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer106.Add( self.m_button2, 1, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer106.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer106, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer97 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_staticText911.Bind( wx.EVT_RIGHT_DOWN, self.choose_r_color )
		self.m_checkBox191.Bind( wx.EVT_CHECKBOX, self.erect_fill_check_setrgb )
		self.m_colourPicker11.Bind( wx.EVT_COLOURPICKER_CHANGED, self.erect_recalc )
		self.m_staticText91.Bind( wx.EVT_RIGHT_DOWN, self.choose_r_color )
		self.m_checkBox19.Bind( wx.EVT_CHECKBOX, self.erect_color_check_setrgb )
		self.m_colourPicker1.Bind( wx.EVT_COLOURPICKER_CHANGED, self.erect_recalc )
		self.m_textCtrl52.Bind( wx.EVT_TEXT, self.erect_recalc )
		self.m_comboBox17.Bind( wx.EVT_COMBOBOX, self.erect_recalc )
		self.m_comboBox17.Bind( wx.EVT_TEXT, self.erect_recalc )
		self.m_textCtrl521.Bind( wx.EVT_TEXT, self.erect_recalc )
		self.m_button2.Bind( wx.EVT_BUTTON, self.erect_return )
		self.m_button3.Bind( wx.EVT_BUTTON, self.erect_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def choose_r_color( self, event ):
		event.Skip()
	
	def erect_fill_check_setrgb( self, event ):
		event.Skip()
	
	def erect_recalc( self, event ):
		event.Skip()
	
	
	def erect_color_check_setrgb( self, event ):
		event.Skip()
	
	
	
	
	
	
	def erect_return( self, event ):
		event.Skip()
	
	def erect_cancel( self, event ):
		event.Skip()
	

###########################################################################
## Class pnlAesthetics
###########################################################################

class pnlAesthetics ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 432,162 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DialogElementText
###########################################################################

class DialogElementText ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Text Element", pos = wx.DefaultPosition, size = wx.Size( 336,364 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer97 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText75 = wx.StaticText( self, wx.ID_ANY, u"Font", wx.DefaultPosition, wx.Size( 75,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText75.Wrap( -1 )
		bSizer98.Add( self.m_staticText75, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_fontPicker1 = wx.FontPickerCtrl( self, wx.ID_ANY, wx.NullFont, wx.DefaultPosition, wx.DefaultSize, wx.FNTP_DEFAULT_STYLE )
		self.m_fontPicker1.SetMaxPointSize( 100 ) 
		bSizer98.Add( self.m_fontPicker1, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer98, 0, 0, 5 )
		
		bSizer99 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText76 = wx.StaticText( self, wx.ID_ANY, u"hjust", wx.DefaultPosition, wx.Size( 75,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText76.Wrap( -1 )
		bSizer99.Add( self.m_staticText76, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl52 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer99.Add( self.m_textCtrl52, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText763 = wx.StaticText( self, wx.ID_ANY, u"vjust", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText763.Wrap( -1 )
		bSizer99.Add( self.m_staticText763, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl522 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer99.Add( self.m_textCtrl522, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer99, 0, 0, 5 )
		
		bSizer991 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText761 = wx.StaticText( self, wx.ID_ANY, u"Angle", wx.DefaultPosition, wx.Size( 75,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText761.Wrap( -1 )
		bSizer991.Add( self.m_staticText761, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl521 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.m_textCtrl521.SetToolTipString( u"in degrees" )
		
		bSizer991.Add( self.m_textCtrl521, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer991, 0, 0, 5 )
		
		bSizer992 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText762 = wx.StaticText( self, wx.ID_ANY, u"Line Height", wx.DefaultPosition, wx.Size( 75,-1 ), wx.ALIGN_RIGHT )
		self.m_staticText762.Wrap( -1 )
		bSizer992.Add( self.m_staticText762, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl72 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		bSizer992.Add( self.m_textCtrl72, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer992, 0, 0, 5 )
		
		bSizer105 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText80 = wx.StaticText( self, wx.ID_ANY, u"R String:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )
		self.m_staticText80.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer105.Add( self.m_staticText80, 0, wx.ALL, 5 )
		
		self.m_textCtrl56 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer105.Add( self.m_textCtrl56, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer97.Add( bSizer105, 1, wx.EXPAND, 5 )
		
		bSizer106 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer106.Add( self.m_button2, 1, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer106.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer106, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer97 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_fontPicker1.Bind( wx.EVT_FONTPICKER_CHANGED, self.etext_recalc_string )
		self.m_textCtrl52.Bind( wx.EVT_TEXT, self.etext_recalc_string )
		self.m_button2.Bind( wx.EVT_BUTTON, self.etext_return )
		self.m_button3.Bind( wx.EVT_BUTTON, self.etext_cancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def etext_recalc_string( self, event ):
		event.Skip()
	
	
	def etext_return( self, event ):
		event.Skip()
	
	def etext_cancel( self, event ):
		event.Skip()
	

###########################################################################
## Class Dialog_RcolorPicker
###########################################################################

class Dialog_RcolorPicker ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1010,870 ), style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer121 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"R_colors.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_bitmap2, 0, wx.ALL, 0 )
		
		
		self.SetSizer( bSizer121 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_bitmap2.Bind( wx.EVT_RIGHT_DOWN, self.r_color_clicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def r_color_clicked( self, event ):
		event.Skip()
	

