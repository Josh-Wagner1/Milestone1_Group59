import wx
import wx.grid
import pandas as pd
import re

from template_frame import MyFrame1 as WelFrame
from template_frame import MyFrame2 as MFrame

from all_functions import filter_food_by_name

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



class MainFrame(MFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")
        # self.table = DataTable(self.df)

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

if __name__ == "__main__":

    app = wx.App()
    frame = WelcomeFrame()
    app.MainLoop()