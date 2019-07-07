# -*- coding: utf-8 -*-
import configparser
from pathlib import Path

import requests
import twder
import pandas
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor

config = configparser.ConfigParser()
#base_path = Path(__file__).parent
#file_path = (base_path / "../../mycurrency.config").resolve()
config.read('/etc/mycurrency/mycurrency.config')

TOKEN = config['default']['line_token']


class analyzer:

    COLUME_NAME = ('時間', '現金買入', '現金賣出', '即期買入', '即期賣出')

    def __init__(self, currency):
        self.currency = currency
        self.data = None
        self.report = None

    def fetch_data(self):
        df = pandas.DataFrame(twder.past_six_month(self.currency), columns=analyzer.COLUME_NAME)
        df = df.set_index('時間')
        df.index = pandas.to_datetime(df.index)
        df = df.iloc[::-1]
        self.data = df


    def analyze(self):
        if type(self.data) == pandas.DataFrame:
            df = self.data
            report = {}
            avg10_df = df.rolling(window=10).mean()
            avg50_df = df.rolling(window=50).mean()
            if avg10_df['現金賣出'][-1] > avg50_df['現金賣出'][-1]:
                report['trend'] = '上漲'
            else:
                report['trend'] = '下跌'
            report['max_price'] = df['現金賣出'].max()
            report['min_price'] = df['現金賣出'].min()
            report['min_price_of_month'] = df['現金賣出'][-30:].min()
            report['max_price_of_month'] = df['現金賣出'][-30:].max()
            report['today_data'] = df.iloc[-1]
            report['best_banks'] = get_low_currency_price_banks(self.currency)
            self.report = report
        else:
            print('No data to analyze. Call fetch_data method first.')

    def send_report(self):
        try:
            data = self.report
            myreport = \
            f"貨幣：{self.currency}\n趨勢：{data['trend']}\n今日資料：{data['today_data']}\n30日現金賣出高點：{data['max_price_of_month']}\n30日現金賣出低點：{data['min_price_of_month']}"
            self._send_to_line(myreport)
        except KeyError:
            raise('please analyze first')

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

