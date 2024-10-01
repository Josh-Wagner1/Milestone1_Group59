# Import statements
import wx
import wx.grid
import pandas as pd
import re
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt
from itertools import islice

from template_frame import MyFrame1 as WelFrame
from template_frame import MyFrame2 as MFrame

from all_functions import load_data, filter_food_by_name, nutrition_level_filter, nutrition_filter_min_max, nutrition_range_filter, filter_food_by_exact_name, calculate_nutrients, nutrition_breakdown

# Class for defining the basic features of tables in the program
class DTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    # Explains itself
    def GetNumberRows(self):
        return len(self.data.index)

    # Explains itself
    def GetNumberCols(self):
        return len(self.data.columns)

    #Used to retrieve all the values
    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    # Explains itself
    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # Used to retrieve and display the column names
    def GetColLabelValue(self, col):
        return self.data.columns[col]

# Class for the welcome frame of the application
class WelcomeFrame(WelFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.Show()

    # Opens the next frame when the continue button is clicked
    def f_Continue( self, event ):
        self.Hide()
        main_frame = MainFrame()
        main_frame.Show()

    # Closes the application if clicked
    def f_Exit( self, event ):
        self.Close()

# Class for the main frame of the application
# There are 2 types of functions f_open[Frame name] and f_[Frame name]
# The former is used to open and close frames using the topbar
# While the latter is activated when the search button (or equivelent) is pressed.
class MainFrame(MFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.CurrPanel = self.m_FoodSearch
        self.df = load_data(r".\Food_Nutrition_Dataset.csv")
        self.table = DTable(self.df)

        # Create the grid shown on FS
        self.m_gridFS.SetTable(self.table, takeOwnership=True)
        self.m_gridFS.AutoSize()
        self.f_OpenFS(None)

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

    def f_setColumns(self, table):
        table.SetColLabelValue(0, "food")
        table.SetColLabelValue(1, "Caloric Value")
        table.SetColLabelValue(2, "Fat")
        table.SetColLabelValue(3, "Saturated Fats")
        table.SetColLabelValue(4, "Monounsaturated Fats")
        table.SetColLabelValue(5, "Polyunsaturated Fats")
        table.SetColLabelValue(6, "Carbohydrates")
        table.SetColLabelValue(7, "Sugars")
        table.SetColLabelValue(8, "Protein")
        table.SetColLabelValue(9, "Dietary Fibre")
        table.SetColLabelValue(10, "Cholesterol")
        table.SetColLabelValue(11, "Sodium")
        table.SetColLabelValue(12, "Water")
        table.SetColLabelValue(13, "Vitamin A")
        table.SetColLabelValue(14, "Vitamin B1")
        table.SetColLabelValue(15, "Vitamin B11")
        table.SetColLabelValue(16, "Vitamin B12")
        table.SetColLabelValue(17, "Vitamin B2")
        table.SetColLabelValue(18, "Vitamin B3")
        table.SetColLabelValue(19, "Vitamin B5")
        table.SetColLabelValue(20, "Vitamin B6")
        table.SetColLabelValue(21, "Vitamin C")
        table.SetColLabelValue(22, "Vitamin D")
        table.SetColLabelValue(23, "Vitamin E")
        table.SetColLabelValue(24, "Vitamin K")
        table.SetColLabelValue(25, "Calcium")
        table.SetColLabelValue(26, "Copper")
        table.SetColLabelValue(27, "Iron")
        table.SetColLabelValue(28, "Magnesium")
        table.SetColLabelValue(29, "Manganese")
        table.SetColLabelValue(30, "Phosphorus")
        table.SetColLabelValue(31, "Potassium")
        table.SetColLabelValue(32, "Selenium")
        table.SetColLabelValue(33, "Zinc")
        table.SetColLabelValue(34, "Nutrition Density")

    def f_NRFilter( self, event ):
        nutrient_input = self.m_txtNR.GetValue()
        min_input = self.m_txtMin.GetValue()
        max_input = self.m_txtMax.GetValue()
        df = self.table.data

        search_result = df[nutrition_range_filter(nutrient_input.strip(), min_input, max_input, df)]

        result_table = DTable(search_result)
        self.m_gridNR.ClearGrid()
        self.m_gridNR.SetTable(result_table, takeOwnership=True)
        self.f_setColumns(self.m_gridNR)
        self.Layout()

    def f_NLFilter(self, event):
        nutrient_input = self.m_txtNL.GetValue()
        level_input = self.m_cbNLL.GetValue()
        df = self.table.data

        search_result = df[nutrition_level_filter(nutrient_input.strip(), level_input.strip(), df)]
        result_table = DTable(search_result)

        self.m_gridNL.ClearGrid()
        self.m_gridNL.SetTable(result_table, takeOwnership=True)
        self.f_setColumns(self.m_gridNL)
        self.Layout()

    def f_FSSearch( self, event ):
        search_input = self.m_txtFS.GetValue()
        df = self.table.data

        search_result = filter_food_by_name(search_input.strip(), df)
        table = DTable(search_result)

        self.m_gridFS.ClearGrid()
        self.m_gridFS.SetTable(table, takeOwnership=True)
        self.m_gridFS.AutoSize()
        self.Layout()

    def f_NBSearch( self, event ):
        search = self.m_txtNB.GetValue()
        data = self.table.data

        nutrition = nutrition_breakdown(search, data).iloc[2:-1].reset_index()
        nutrition.columns = ['Nutrient', 'NutritionValue']
        nutrition = nutrition.sort_values(by='NutritionValue', ascending=False)

        
        nutritionTop8 = pd.concat([nutrition.head(8), 
                        pd.DataFrame({'Nutrient': ['Others'], 
                                'NutritionValue': [nutrition['NutritionValue'][8:].sum()]})], 
                                ignore_index=True)
        figure = self.plot_pie_chart(nutritionTop8.set_index('Nutrient')['NutritionValue'])
        h, w = self.m_NBGraph.GetSize()
        figure.set_size_inches(h / figure.get_dpi(), w / figure.get_dpi())
        canvas = FigureCanvasWxAgg(self.m_NBGraph, -1, figure)
        canvas.SetSize(self.m_NBGraph.GetSize())
        self.Layout()

    def plot_pie_chart(self, data):
            explode = [0.1] * len(data) 
            figure_score, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

            ax1.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, shadow=True, explode=explode, textprops={'fontsize': 7})
            ax1.set_title('Pie Chart')
            ax1.axis('equal') 

            ax2.bar(data.index, data, color='skyblue', edgecolor='black')
            ax2.set_title('Bar Chart')
            ax2.set_xlabel('Type of Nutrient')
            ax2.set_ylabel('Weight in grams')
            ax2.set_xticks(range(len(data)))
            ax2.set_xticklabels(data.index, rotation=45, ha='right', fontsize=8)

            plt.tight_layout()
            return figure_score

    def f_WCCalculate( self, event ):
        search = self.m_txtWC.GetValue()
        weight = self.m_txtWeight.GetValue()
        data = self.table.data
        calc_result = calculate_nutrients(search, data, weight)

        self.m_gridWC.ClearGrid()
        self.m_gridWC.SetColLabelValue(0, "Nutrient")
        self.m_gridWC.SetColLabelValue(1, "Scaled value (g)")

        for row, (i, j) in enumerate(islice(calc_result.items(), 1, None)):
            self.m_gridWC.SetCellValue(row, 0, str(i))
            self.m_gridWC.SetCellValue(row, 1, str(round(j, 2)))

        self.m_gridWC.AutoSize()
        self.Layout()

# Runs the application
if __name__ == "__main__":

    app = wx.App()
    frame = WelcomeFrame()
    app.MainLoop()