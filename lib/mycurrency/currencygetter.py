import datetime

import twder
import xlwings as xw

COLUME_NAME = ('時間', '現金買入', '現金賣出', '即期買入', '即期賣出')

def set_sheet_header(sheet):
    sheet.range("A1:E1").value = list(COLUME_NAME)

def currency_to_excel(excel_path):
    currencydict = twder.now_all()
    wb = xw.Book(excel_path)
    for currency, prices in currencydict.items():

        try:
            # 若有該試算表，就開啓它，並且寫入資料
            sheet = wb.sheets[currency]
            sheet.activate()
        except:
            sheet = wb.sheets.add(name=currency, after=wb.sheets[-1])
            set_sheet_header(sheet)
        finally:
            last_row = sheet.range("A1").end("down").row
            column_index = 1
            for price in prices:
                sheet.cells(last_row+1, column_index).value = price
                column_index += 1


