import wx
import wx.grid
import pandas as pd
import re

from template_frame import MyFrame1 as WelFrame
from template_frame import MyFrame2 as MFrame

from all_functions import load_data, filter_food_by_name, nutrition_level_filter, nutrition_filter_min_max, nutrition_range_filter, filter_food_by_exact_name, calculate_nutrients, nutrition_breakdown

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

    def GetColLabelValue(self, col):
        return self.data.columns[col]
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
        self.CurrPanel = self.m_FoodSearch
        self.df = load_data(r".\Food_Nutrition_Dataset.csv")
        self.table = DTable(self.df)
        # Create grid
        self.m_gridFS.SetTable(self.table, takeOwnership=True)
        self.m_gridFS.AutoSize()
        # self.m_gridNR.SetTable(self.table, takeOwnership=True)
        # self.m_gridNR.AutoSize()
        # self.m_gridNL.SetTable(self.table, takeOwnership=True)
        # self.m_gridNL.AutoSize()
        self.f_OpenFS(None)

    # All f_Open functions are used to open frames when the labels on the top bar are clicked.
    def f_OpenNF( self, event ):
        self.CurrPanel.Hide()
        self.CurrPanel = self.m_NutritionFilter
        self.m_staticText6.SetLabel("Nutrition Filter")
        self.Layout()
        self.CurrPanel.SetPosition((142, 129))

        # Create grid

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
        nutrient_input = self.m_cbNR.GetValue()
        min_input = float(self.m_txtMin.GetValue())
        max_input = float(self.m_txtMax.GetValue())
        df = self.table.data

        search_result = df[nutrition_range_filter(nutrient_input, min_input, max_input, df)]

        result_table = DTable(search_result)
        self.m_gridNR.ClearGrid()
        self.m_gridNR.SetTable(result_table, True)
        self.m_gridNR.AutoSize()
        self.Layout()

    def f_NLFilter(self, event):
        nutrient_input = self.m_cbNL.GetValue()
        level_input = self.m_cbNLL.GetValue()
        df = self.table.data

        search_result = df[nutrition_level_filter(nutrient_input, level_input.strip(), df)]
        result_table = DTable(search_result)

        self.m_gridNL.ClearGrid()
        self.m_gridNL.SetTable(result_table, takeOwnership=True)
        self.m_gridNL.AutoSize()

    def f_FSSearch( self, event ):
        search_input = self.m_cbFS.GetValue()
        data = self.table.data

        search_result = filter_food_by_name(search_input, data)
        table = DTable(search_result)

        self.m_gridFS.ClearGrid()
        self.m_gridFS.SetTable(table,takeOwnership=True)
        self.m_gridFS.AutoSize()
        self.Layout()

    def f_NBSearch( self, event ):
        search = self.m_cbNB.GetValue()
        data = self.table.data

        selected_food = nutrition_breakdown(search, data)

        print(type(selected_food))
        print(selected_food)


    def f_WCCalculate( self, event ):
        search = self.m_cbWC.GetValue()
        weight = float(self.m_txtWeight.GetValue())
        data = self.table.data
        calc_result = calculate_nutrients(search, data, weight)

        self.m_gridWC.ClearGrid()
        self.m_gridWC.SetColLabelValue(0, "Nutrient")
        self.m_gridWC.SetColLabelValue(0, "value (g)")

        for row, (i, j) in enumerate(calc_result.items()):
            self.m_gridWC.SetCellValue(row, 0, str(i))
            self.m_gridWC.SetCellValue(row, 1, str(j))

        self.m_gridWC.AutoSize()
        self.Layout()


if __name__ == "__main__":

    app = wx.App()
    frame = WelcomeFrame()
    app.MainLoop()