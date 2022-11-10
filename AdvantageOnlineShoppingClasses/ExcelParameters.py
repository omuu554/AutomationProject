from openpyxl import Workbook
from openpyxl import load_workbook


class ExcelParemters:
    def __init__(self):
        self.workbook = load_workbook(filename="Parameters.xlsx")
        self.Parameters = self.workbook.active

    def Get_TestParameters_Dict(self,TestNumber:int):
        TestNumber = TestNumber + 1
        ParametersDict = {}
        info = {}
        for row in self.Parameters.iter_rows(min_row=2, max_row=31, min_col=1, max_col=12, values_only=True):
            if (row[0] is not None):
                currentObject = row[0]
                info = {}
            info[row[1]] = row[TestNumber]
            ParametersDict[currentObject] = info

        return ParametersDict


    def Close_Workbook(self):
        self.workbook.close()









excelSheet = ExcelParemters()
print(excelSheet.Get_TestParameters_Dict(1))








