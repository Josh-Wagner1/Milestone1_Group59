# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Nutritional Food App"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 60 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_btnContinue = wx.Button( self, wx.ID_ANY, _(u"Continue"), wx.DefaultPosition, wx.Size( 400,50 ), 0 )
        self.m_btnContinue.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_btnContinue.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.m_btnContinue.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer3.Add( self.m_btnContinue, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )

        self.m_btnExit = wx.Button( self, wx.ID_ANY, _(u"Exit"), wx.DefaultPosition, wx.Size( 400,50 ), 0 )
        self.m_btnExit.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_btnExit.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        self.m_btnExit.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

        bSizer3.Add( self.m_btnExit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )


        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_btnContinue.Bind( wx.EVT_BUTTON, self.f_Continue )
        self.m_btnExit.Bind( wx.EVT_BUTTON, self.f_Exit )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def f_Continue( self, event ):
        event.Skip()

    def f_Exit( self, event ):
        event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer5.Add( ( 50, 0), 0, wx.EXPAND, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )


        bSizer5.Add( ( 90, 0), 0, wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Food Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )


        bSizer5.Add( ( 62, 0), 0, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Breakdown"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer5.Add( self.m_staticText4, 0, wx.ALL, 5 )


        bSizer5.Add( ( 30, 0), 0, wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Weight Calculator"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,5 ), wx.LI_HORIZONTAL )
        self.m_staticline1.SetMaxSize( wx.Size( 250,5 ) )

        bSizer6.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 0 )

        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,5 ), wx.LI_HORIZONTAL )
        self.m_staticline2.SetMaxSize( wx.Size( 250,5 ) )

        bSizer6.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 0 )

        self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,5 ), wx.LI_HORIZONTAL )
        self.m_staticline3.SetMaxSize( wx.Size( 250,5 ) )

        bSizer6.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 0 )

        self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,5 ), wx.LI_HORIZONTAL )
        self.m_staticline4.SetMaxSize( wx.Size( 250,5 ) )

        bSizer6.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )


        bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )


        bSizer7.Add( ( 100, 0), 1, wx.EXPAND, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Panel_title"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        self.m_staticText6.SetFont( wx.Font( 26, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer7.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20 )


        bSizer7.Add( ( 100, 0), 1, wx.EXPAND, 5 )


        bSizer4.Add( bSizer7, 0, wx.EXPAND, 5 )

        self.m_NutritionFilter = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,400 ), 0 )
        self.m_NutritionFilter.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_NutritionFilter.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        self.m_NutritionFilter.Hide()

        self.m_NutritionRange = wx.Panel( self.m_NutritionFilter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_NutritionRange.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )


        bSizer8.Add( ( 0, 15), 0, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer9.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_staticText7 = wx.StaticText( self.m_NutritionRange, wx.ID_ANY, _(u"Food"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer9.Add( self.m_staticText7, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer9, 0, 0, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer10.Add( ( 75, 0), 1, wx.EXPAND, 5 )

        m_cbNRChoices = []
        self.m_cbNR = wx.ComboBox( self.m_NutritionRange, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), m_cbNRChoices, 0 )
        self.m_cbNR.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer10.Add( self.m_cbNR, 0, wx.ALL, 5 )


        bSizer10.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        self.m_btnNR = wx.Button( self.m_NutritionRange, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.Size( 125,30 ), 0 )
        self.m_btnNR.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_btnNR.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.m_btnNR.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer10.Add( self.m_btnNR, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer10, 0, 0, 5 )


        bSizer8.Add( ( 0, 5), 0, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer11.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_staticText8 = wx.StaticText( self.m_NutritionRange, wx.ID_ANY, _(u"Min"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer11.Add( self.m_staticText8, 0, wx.ALL, 5 )


        bSizer11.Add( ( 60, 0), 0, wx.EXPAND, 5 )

        self.m_staticText9 = wx.StaticText( self.m_NutritionRange, wx.ID_ANY, _(u"Max"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        self.m_staticText9.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer11.Add( self.m_staticText9, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer11, 0, 0, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_txtMin = wx.TextCtrl( self.m_NutritionRange, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        self.m_txtMin.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer12.Add( self.m_txtMin, 0, wx.ALL, 5 )


        bSizer12.Add( ( 40, 0), 0, wx.EXPAND, 5 )

        self.m_txtMax = wx.TextCtrl( self.m_NutritionRange, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        self.m_txtMax.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer12.Add( self.m_txtMax, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer12, 0, 0, 5 )


        bSizer8.Add( ( 0, 15), 0, 0, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer13.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_grid1 = wx.grid.Grid( self.m_NutritionRange, wx.ID_ANY, wx.DefaultPosition, wx.Size( 550,180 ), 0 )

        # Grid
        self.m_grid1.CreateGrid( 10, 6 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer13.Add( self.m_grid1, 0, wx.ALL, 5 )


        bSizer8.Add( bSizer13, 1, wx.EXPAND, 5 )


        self.m_NutritionRange.SetSizer( bSizer8 )
        self.m_NutritionRange.Layout()
        bSizer8.Fit( self.m_NutritionRange )
        self.m_NutritionFilter.AddPage( self.m_NutritionRange, _(u"Nutrition Range"), False )
        self.m_NutritionLevel = wx.Panel( self.m_NutritionFilter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer14 = wx.BoxSizer( wx.VERTICAL )


        bSizer14.Add( ( 0, 15), 0, 0, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer15.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_staticText10 = wx.StaticText( self.m_NutritionLevel, wx.ID_ANY, _(u"Food"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        self.m_staticText10.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer15.Add( self.m_staticText10, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer15, 0, 0, 5 )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer16.Add( ( 75, 0), 1, wx.EXPAND, 5 )

        m_cbNLChoices = []
        self.m_cbNL = wx.ComboBox( self.m_NutritionLevel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), m_cbNLChoices, 0 )
        self.m_cbNL.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer16.Add( self.m_cbNL, 0, wx.ALL, 5 )


        bSizer16.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        self.m_btnNL = wx.Button( self.m_NutritionLevel, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.Size( 125,30 ), 0 )
        self.m_btnNL.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_btnNL.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.m_btnNL.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer16.Add( self.m_btnNL, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer16, 0, 0, 5 )


        bSizer14.Add( ( 0, 5), 0, 0, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer17.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_staticText11 = wx.StaticText( self.m_NutritionLevel, wx.ID_ANY, _(u"Level"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        self.m_staticText11.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText11.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer17.Add( self.m_staticText11, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer17, 0, 0, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer18.Add( ( 75, 0), 1, wx.EXPAND, 5 )

        m_cbNLLChoices = [ _(u"Low"), _(u"Medium"), _(u"High") ]
        self.m_cbNLL = wx.ComboBox( self.m_NutritionLevel, wx.ID_ANY, _(u"Low"), wx.DefaultPosition, wx.Size( 125,-1 ), m_cbNLLChoices, 0 )
        self.m_cbNLL.SetSelection( 0 )
        self.m_cbNLL.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer18.Add( self.m_cbNLL, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer18, 0, 0, 5 )


        bSizer14.Add( ( 0, 15), 0, 0, 5 )

        bSizer19 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer19.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_gridNL = wx.grid.Grid( self.m_NutritionLevel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 550,180 ), 0 )

        # Grid
        self.m_gridNL.CreateGrid( 10, 6 )
        self.m_gridNL.EnableEditing( True )
        self.m_gridNL.EnableGridLines( True )
        self.m_gridNL.EnableDragGridSize( False )
        self.m_gridNL.SetMargins( 0, 0 )

        # Columns
        self.m_gridNL.EnableDragColMove( False )
        self.m_gridNL.EnableDragColSize( True )
        self.m_gridNL.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_gridNL.EnableDragRowSize( True )
        self.m_gridNL.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_gridNL.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer19.Add( self.m_gridNL, 0, wx.ALL, 5 )


        bSizer14.Add( bSizer19, 1, wx.EXPAND, 5 )


        self.m_NutritionLevel.SetSizer( bSizer14 )
        self.m_NutritionLevel.Layout()
        bSizer14.Fit( self.m_NutritionLevel )
        self.m_NutritionFilter.AddPage( self.m_NutritionLevel, _(u"Nutrition Level"), True )

        bSizer4.Add( self.m_NutritionFilter, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_FoodSearch = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,400 ), wx.TAB_TRAVERSAL )
        self.m_FoodSearch.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        self.m_FoodSearch.Hide()
        self.m_FoodSearch.SetMaxSize( wx.Size( 700,400 ) )

        bSizer20 = wx.BoxSizer( wx.VERTICAL )


        bSizer20.Add( ( 0, 15), 0, 0, 5 )

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer21.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_staticText12 = wx.StaticText( self.m_FoodSearch, wx.ID_ANY, _(u"Food"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        self.m_staticText12.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer21.Add( self.m_staticText12, 0, wx.ALL, 5 )


        bSizer20.Add( bSizer21, 0, 0, 5 )

        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer22.Add( ( 75, 0), 1, wx.EXPAND, 5 )

        m_cbFSChoices = []
        self.m_cbFS = wx.ComboBox( self.m_FoodSearch, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), m_cbFSChoices, 0 )
        self.m_cbFS.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer22.Add( self.m_cbFS, 0, wx.ALL, 5 )


        bSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        self.m_btnFS = wx.Button( self.m_FoodSearch, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.Size( 125,30 ), 0 )
        self.m_btnFS.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_btnFS.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.m_btnFS.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer22.Add( self.m_btnFS, 0, wx.ALL, 5 )


        bSizer20.Add( bSizer22, 0, 0, 5 )


        bSizer20.Add( ( 0, 15), 0, 0, 5 )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer23.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_gridFS = wx.grid.Grid( self.m_FoodSearch, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,300 ), 0 )

        # Grid
        self.m_gridFS.CreateGrid( 10, 6 )
        self.m_gridFS.EnableEditing( True )
        self.m_gridFS.EnableGridLines( True )
        self.m_gridFS.EnableDragGridSize( False )
        self.m_gridFS.SetMargins( 0, 0 )

        # Columns
        self.m_gridFS.EnableDragColMove( False )
        self.m_gridFS.EnableDragColSize( True )
        self.m_gridFS.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_gridFS.EnableDragRowSize( True )
        self.m_gridFS.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_gridFS.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer23.Add( self.m_gridFS, 0, wx.ALL, 5 )


        bSizer20.Add( bSizer23, 1, wx.EXPAND, 5 )


        self.m_FoodSearch.SetSizer( bSizer20 )
        self.m_FoodSearch.Layout()
        bSizer4.Add( self.m_FoodSearch, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_NutritionBreakdown = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,400 ), wx.TAB_TRAVERSAL )
        self.m_NutritionBreakdown.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        self.m_NutritionBreakdown.Hide()

        bSizer24 = wx.BoxSizer( wx.VERTICAL )


        bSizer24.Add( ( 0, 15), 0, 0, 5 )

        bSizer25 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer25.Add( ( 75, 0), 0, 0, 5 )

        self.m_staticText13 = wx.StaticText( self.m_NutritionBreakdown, wx.ID_ANY, _(u"Food"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        self.m_staticText13.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText13.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer25.Add( self.m_staticText13, 0, wx.ALL, 5 )


        bSizer24.Add( bSizer25, 0, 0, 5 )

        bSizer26 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer26.Add( ( 75, 0), 1, wx.EXPAND, 5 )

        m_cbNBChoices = []
        self.m_cbNB = wx.ComboBox( self.m_NutritionBreakdown, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), m_cbNBChoices, 0 )
        self.m_cbNB.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer26.Add( self.m_cbNB, 0, wx.ALL, 5 )


        bSizer26.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        self.m_btnNB = wx.Button( self.m_NutritionBreakdown, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.Size( 125,30 ), 0 )
        self.m_btnNB.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_btnNB.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.m_btnNB.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer26.Add( self.m_btnNB, 0, wx.ALL, 5 )


        bSizer24.Add( bSizer26, 0, 0, 5 )

        bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_NBGraph = wx.Panel( self.m_NutritionBreakdown, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.TAB_TRAVERSAL )
        bSizer27.Add( self.m_NBGraph, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_PieChart = wx.Panel( self.m_NutritionBreakdown, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.TAB_TRAVERSAL )
        bSizer27.Add( self.m_PieChart, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer24.Add( bSizer27, 1, wx.EXPAND, 5 )


        self.m_NutritionBreakdown.SetSizer( bSizer24 )
        self.m_NutritionBreakdown.Layout()
        bSizer4.Add( self.m_NutritionBreakdown, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_WeightCalculator = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,400 ), wx.TAB_TRAVERSAL )
        self.m_WeightCalculator.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        self.m_WeightCalculator.Hide()

        bSizer28 = wx.BoxSizer( wx.VERTICAL )


        bSizer28.Add( ( 0, 15), 0, 0, 5 )

        bSizer29 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer29.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_staticText14 = wx.StaticText( self.m_WeightCalculator, wx.ID_ANY, _(u"Food"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        self.m_staticText14.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer29.Add( self.m_staticText14, 0, wx.ALL, 5 )


        bSizer28.Add( bSizer29, 0, 0, 5 )

        bSizer30 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer30.Add( ( 75, 0), 1, wx.EXPAND, 5 )

        m_cbWCChoices = []
        self.m_cbWC = wx.ComboBox( self.m_WeightCalculator, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), m_cbWCChoices, 0 )
        self.m_cbWC.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer30.Add( self.m_cbWC, 0, wx.ALL, 5 )


        bSizer30.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        self.m_btnWC = wx.Button( self.m_WeightCalculator, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.Size( 125,30 ), 0 )
        self.m_btnWC.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_btnWC.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.m_btnWC.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer30.Add( self.m_btnWC, 0, wx.ALL, 5 )


        bSizer28.Add( bSizer30, 0, 0, 5 )


        bSizer28.Add( ( 0, 5), 0, 0, 5 )

        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer31.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_staticText15 = wx.StaticText( self.m_WeightCalculator, wx.ID_ANY, _(u"Weight (g)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        self.m_staticText15.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
        self.m_staticText15.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer31.Add( self.m_staticText15, 0, wx.ALL, 5 )


        bSizer28.Add( bSizer31, 0, 0, 5 )

        bSizer32 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer32.Add( ( 75, 0), 0, wx.EXPAND, 5 )

        self.m_txtWeight = wx.TextCtrl( self.m_WeightCalculator, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
        self.m_txtWeight.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer32.Add( self.m_txtWeight, 0, wx.ALL, 5 )


        bSizer28.Add( bSizer32, 0, 0, 5 )


        bSizer28.Add( ( 0, 15), 0, 0, 5 )

        bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_gridWC = wx.grid.Grid( self.m_WeightCalculator, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), 0 )

        # Grid
        self.m_gridWC.CreateGrid( 10, 6 )
        self.m_gridWC.EnableEditing( True )
        self.m_gridWC.EnableGridLines( True )
        self.m_gridWC.EnableDragGridSize( False )
        self.m_gridWC.SetMargins( 0, 0 )

        # Columns
        self.m_gridWC.EnableDragColMove( False )
        self.m_gridWC.EnableDragColSize( True )
        self.m_gridWC.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_gridWC.EnableDragRowSize( True )
        self.m_gridWC.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_gridWC.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer33.Add( self.m_gridWC, 0, wx.ALL, 5 )

        self.m_WCGraph = wx.Panel( self.m_WeightCalculator, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.TAB_TRAVERSAL )
        bSizer33.Add( self.m_WCGraph, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer28.Add( bSizer33, 1, wx.EXPAND, 5 )


        self.m_WeightCalculator.SetSizer( bSizer28 )
        self.m_WeightCalculator.Layout()
        bSizer4.Add( self.m_WeightCalculator, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_staticText2.Bind( wx.EVT_LEFT_DOWN, self.f_OpenNF )
        self.m_staticText3.Bind( wx.EVT_LEFT_DOWN, self.f_OpenFS )
        self.m_staticText4.Bind( wx.EVT_LEFT_DOWN, self.f_OpenNB )
        self.m_staticText5.Bind( wx.EVT_LEFT_DOWN, self.f_OpenWC )
        self.m_btnNR.Bind( wx.EVT_BUTTON, self.f_NRFilter )
        self.m_btnNL.Bind( wx.EVT_BUTTON, self.f_NLFilter )
        self.m_btnFS.Bind( wx.EVT_BUTTON, self.f_FSSearch )
        self.m_btnNB.Bind( wx.EVT_BUTTON, self.f_NBSearch )
        self.m_btnWC.Bind( wx.EVT_BUTTON, self.f_WCCalculate )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def f_OpenNF( self, event ):
        event.Skip()

    def f_OpenFS( self, event ):
        event.Skip()

    def f_OpenNB( self, event ):
        event.Skip()

    def f_OpenWC( self, event ):
        event.Skip()

    def f_NRFilter( self, event ):
        event.Skip()

    def f_NLFilter( self, event ):
        event.Skip()

    def f_FSSearch( self, event ):
        event.Skip()

    def f_NBSearch( self, event ):
        event.Skip()

    def f_WCCalculate( self, event ):
        event.Skip()


