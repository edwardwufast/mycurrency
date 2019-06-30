import os
import time

import twder

from mycurrency.injector import twderinjector
from mycurrency.utils import initiate_new_book

excel_path = 'test_book.xlsx'
items = ['CNY', 'THB']


def test_inject_data(workbook):

    injector = twderinjector(excel_path, items)
    injector.inject_data()

def test_inject_sixmonth_data(workbook):

    injector = twderinjector(excel_path, items)
    injector.inject_sixmonth_data('JPY')
