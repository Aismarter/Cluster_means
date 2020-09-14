import xlrd
import xlwt

def get_info4col(excel_path,excel_sheet,row, col,end=None):
    Excelfile = xlrd.open_workbook(excel_path)
    Excel_sheet = Excelfile.sheet_by_name(excel_sheet)
    rowNum = Excel_sheet.nrows
    colNum = Excel_sheet.ncols
    if end == None:
        ce = colNum
        re = rowNum
    else:
        ce = end[0]
        re = end[1]
    excel_content =  []
    for n in range(col, ce):
        for i in range(row, re):
            excel_content.append(round(Excel_sheet.cell(n,i).value,2))
    return excel_content




