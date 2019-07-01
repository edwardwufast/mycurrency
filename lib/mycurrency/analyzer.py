# -*- coding: utf-8 -*-
import configparser
from pathlib import Path

import requests
import twder
import pandas
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor

config = configparser.ConfigParser()
base_path = Path(__file__).parent
file_path = (base_path / "../../mycurrency.config").resolve()
config.read(file_path)

TOKEN = config['default']['line_token']


class analyzer:

    def __init__(self, currency):
        self.currency = currency
        self.data = None
        self.report = None

    def fetch_data(self):
        self.data = twder.past_six_month(self.currency)

    def analyze(self):
        if self.data:
            pass

        else:
            print('No data to analyze. Call fetch_data method first.')

    def report(self):
        pass

    def _send_to_line(self, msg):
        line_url = "https://notify-api.line.me/api/notify"
        headers = {
            "Authorization": "Bearer " + TOKEN,
            "Content-Type" : "application/x-www-form-urlencoded"
        }

        payload = {'message': msg}
        r = requests.post(line_url, headers = headers, params = payload)

def get_low_currency_price_banks(currency):
    url = f'https://www.findrate.tw/{currency}/#.XRjSkVMkveR'
    result = requests.get(url)
    result.encoding = 'UTF-8'
    html = BeautifulSoup(result.text, 'html.parser')
    tables = html.findAll('table')
    extractor = Extractor(tables[1])
    extractor.parse()
    currency_table = extractor.return_list()
    columns = currency_table.pop(0)[1:]
    indices = [ data.pop(0).rstrip() for data in currency_table ]
    df = pandas.DataFrame(currency_table, columns=columns, index=indices)
    top8_cash_sell = df.sort_values(['現鈔賣出']).iloc[:8]
    top8_spot_sell = df.sort_values(['即期賣出']).iloc[:8]
    return (top8_cash_sell, top8_spot_sell)

