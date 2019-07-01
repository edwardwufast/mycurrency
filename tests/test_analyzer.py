import pytest
from mycurrency.analyzer import get_low_currency_price_banks

def test_fetch_data(jpy_analyzer):

    jpy_analyzer.fetch_data()
    print(jpy_analyzer.data)

@pytest.mark.skip()
def test_send_to_line(jpy_analyzer):
    jpy_analyzer._send_to_line('test')

def test_get_low_currency_price_banks():
    get_low_currency_price_banks('JPY')

def test_analyze(jpy_analyzer):
    jpy_analyzer.analyze()
    print(jpy_analyzer.report)

def test_report(jpy_analyzer):
    jpy_analyzer.analyze()
    jpy_analyzer.send_report()
