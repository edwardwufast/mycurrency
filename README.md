# mycurrency

This project is a homework on class.

# Install:
```
sudo python setup.py install
```
# Usage:
1. Save today's currency price in excel.

update_currency -e <excel_file_path> -c <currency>


avalible options of currency:
'CNY', 'THB', 'SEK', 'USD', 'IDR', 'AUD', 'NZD', 'PHP', 'MYR', 'GBP', 'ZAR', 'CHF', 'VND', 'EUR', 'KRW', 'SGD', 'JPY', 'CAD', 'HKD'

For example:
```
update_currency -e my.xlxs -c JPY USD CHF
```

If you get error like:

```
OSERROR: -1728
		MESSAGE: The object you are trying to access does not exist
		COMMAND: app(pid=28969).workbooks['ggf'].count(each=k.worksheet)
```
You have to allow the program to access excell file first by click 'yes' when excel ask you.

If you get no aem module error, try reinstall appscript.

2. Provide suggestion to buy or sell your currency.
```
suggest <currency>
```
For example:
```
suggest JPY
```
It will also send report to line if you provide line token in configuration file /etc/mycurrency/mycurrency.config
Apply line token here: https://notify-bot.line.me/zh_TW/

3. Provide which bank have cheaper price:

```
bestbank <currency>
```
For example:

```
bestbank JPY
```
# requirement

python 3.7
