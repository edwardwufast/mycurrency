import datetime

import twder
import openpyxl
import xlwings as xw


class injector:

    def __init__(self, excel_path, items):
        self.excel_path = excel_path
        self.items = items

    def inject_data():
        pass

class twderinjector(injector):

    COLUME_NAME = ('時間', '現金買入', '現金賣出', '即期買入', '即期賣出')

    def _set_sheet_header(self, sheet):
        sheet.range("A1:E1").value = list(twderinjector.COLUME_NAME)

    def _currency_to_excel(self, currency, book):
        currency_data = twder.now(currency)
        try:
            # 若有該試算表，就開啓它，並且寫入資料
            sheet = book.sheets[currency]
            sheet.activate()
        except:
            sheet = book.sheets.add(name=currency, after=book.sheets[-1])
            self._set_sheet_header(sheet)
        finally:
            last_row = sheet.range("A1").end("down").row
            sheet.range((last_row+1, 1)).value = currency_data

    def inject_data(self):
        currencies = self.items
        book = xw.Book(self.excel_path)
        [ self._currency_to_excel(currency, book) for currency in currencies ]
