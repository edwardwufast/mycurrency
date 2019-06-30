import configparser
from pathlib import Path

import requests
import twder

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
