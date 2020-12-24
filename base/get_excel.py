import xlrd
from  xlutils.copy import copy

class OpenExcel:

    #定义全局变量，定义获取表格基本信息

    def __init__(self,excel_add=None,sheet_id=None):
        if excel_add:
            self.file_name = excel_add
        else:
            self.file_name ='../config/data1.xls'

        if sheet_id:
            self.sheet_id = self.sheet_id
        else:
            self.sheet_id = 0

    # 获取单元格行数
    def get_lines(self):
        tabes = self.get_data()
        return tabes.nrows

    # 获取整个表格数据
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    '''获取某一个单元格内容'''
    def get_cell_value(self,row,col):
        return self.get_data().cell(row,col).value

    # 写入数据
    def write_value(self,row,col,value):
        id = self.sheet_id
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(id)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #根据对应的case_id 找对应的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    #根据依赖的case_id，找到对应case的行号
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_cols_data(0)
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1
     # 根据行号，找倒该行的内容
    def get_row_values(self,row):
        tablles = self.get_data()
        row_data = tablles.row.values(row)
        return row_data


     # 根据列号，获取谋一列的属性
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.get_data().col_values(col_id)
        else:
            cols = self.get_data().col_values(0)
        return cols




if __name__ == '__main__':
    open_e = OpenExcel('../config/Home_pageTestCase.xls')
    c= open_e.get_data()
    print(c)



