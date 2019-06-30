import os

import pytest

from mycurrency.utils import initiate_new_book
from mycurrency.analyzer import analyzer

excel_path = 'test_book.xlsx'

@pytest.fixture(scope="module")
def workbook():
    if os.path.exists(excel_path):
        os.remove(excel_path)
    initiate_new_book(excel_path)

@pytest.fixture(scope="module")
def jpy_analyzer():
    yield analyzer('JPY')
