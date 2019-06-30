import datetime

import twder
import openpyxl
import numpy as np
import xlwings as xw


class injector:

    def __init__(self, excel_path, items):
        self.excel_path = excel_path
        self.items = items
        self.book = xw.Book(self.excel_path)

    def inject_data():
        pass

class twderinjector(injector):

    COLUME_NAME = ('時間', '現金買入', '現金賣出', '即期買入', '即期賣出')

    def _set_sheet_header(self, sheet):
        sheet.range("A1:E1").value = list(twderinjector.COLUME_NAME)

    def _currency_to_excel(self, currency):
        currency_data = twder.now(currency)
        sheet = self._get_sheet(currency)
        last_row = sheet.range("A1").end("down").row
        sheet.range((last_row+1, 1)).value = currency_data

    def _get_sheet(self, sheet_name):
        try:
            sheet = self.book.sheets[sheet_name]
            sheet.activate()
        except:
            sheet = self.book.sheets.add(name=sheet_name, after=self.book.sheets[-1])
            self._set_sheet_header(sheet)
        return sheet


    def inject_data(self):
        currencies = self.items
        [ self._currency_to_excel(currency) for currency in currencies ]

    def inject_sixmonth_data(self, currency):
        data = twder.past_six_month(currency)
        data = np.asarray(data)
        sheet = self._get_sheet(currency + '_six_month')
        sheet.range((2,1)).value = data


