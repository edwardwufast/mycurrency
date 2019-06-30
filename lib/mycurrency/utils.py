import openpyxl

def initiate_new_book(excel_path):
    wb = openpyxl.Workbook()
    wb.save(excel_path)
