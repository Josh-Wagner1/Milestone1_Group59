import wx
import wx.grid
import pandas as pd
import re

from template_frame import MyFrame1 as WelFrame
from template_frame import MyFrame2 as MFrame

from all_functions import filter_food_by_name, nutrition_level_filter, nutrition_filter_min_max, nutrition_range_filter

class WelcomeFrame(WelFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.Show()

    def f_Continue( self, event ):
        self.Hide()
        main_frame = MainFrame()
        main_frame.Show()

    def f_Exit( self, event ):
        self.Close()


class DTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

class MainFrame(MFrame):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")
        self.table = DTable(self.df)

        self.m_gridFS.SetTable(self.table, takeOwnership=True)
        self.m_gridFS.AutoSize()

        self.CurrPanel = self.m_FoodSearch
        self.m_staticText6.SetLabel("Food Search")
        self.m_FoodSearch.Show()
        self.Show()

    def f_OpenNF( self, event ):
        self.CurrPanel.Hide()
        self.CurrPanel = self.m_NutritionFilter
        self.m_staticText6.SetLabel("Nutrition Filter")
        self.Layout()
        self.CurrPanel.SetPosition((142, 129))
        self.m_NutritionFilter.Show()

    def f_OpenFS( self, event ):
        self.CurrPanel.Hide()
        self.CurrPanel = self.m_FoodSearch
        self.m_staticText6.SetLabel("Food Search")
        self.Layout()
        self.CurrPanel.SetPosition((142, 129))
        self.m_FoodSearch.Show()

    def f_OpenNB( self, event ):
        self.CurrPanel.Hide()
        self.CurrPanel = self.m_NutritionBreakdown
        self.m_staticText6.SetLabel("Nutrition Breakdown")
        self.Layout()
        self.CurrPanel.SetPosition((142, 129))
        self.m_NutritionBreakdown.Show()

    def f_OpenWC( self, event ):
        self.CurrPanel.Hide()
        self.CurrPanel = self.m_WeightCalculator
        self.m_staticText6.SetLabel("Weight Calculator")
        self.Layout()
        self.CurrPanel.SetPosition((142, 129))
        self.CurrPanel.Show()

    def f_NRFilter( self, event ):
        nutrition = self.m_cbNR.GetValue()

    def f_NLFilter(self, event):
        nutrition = self.m_cbNL.GetValue()
        level = self.m_cbNLL.GetValue()

    def f_FSSearch( self, event ):
        search = self.m_cbFS.GetValue()
        data = self.table.data

        result = filter_food_by_name(search, data)

        table = DTable(result)
        self.m_gridFS.ClearGrid()
        self.m_gridFS.SetTable(table,True)
        self.m_gridFS.AutoSize()

        self.Layout()

    def f_NBSearch( self, event ):
        search = self.m_cbNB.GetValue()

    def f_WCCalculate( self, event ):
        search = self.m_cbWC.GetValue()

if __name__ == "__main__":

    app = wx.App()
    frame = WelcomeFrame()
    app.MainLoop()