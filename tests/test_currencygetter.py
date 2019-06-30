import twder

from mycurrency.currencygetter import currency_to_excel


def test_currency_to_excel():

    currency_to_excel('test_book.xlsx')
    
