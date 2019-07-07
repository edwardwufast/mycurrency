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
Excel result example: https://www.dropbox.com/s/7m76n1gn8kkkzm5/%E8%9E%A2%E5%B9%95%E6%88%AA%E5%9C%96%202019-07-07%2017.29.04.png?dl=0

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
```
[~/mycurrency] (master) 0h11m $ suggest JPY
嘗試取得台銀資料
分析
發送報告至line
報告如下：
{'trend': '上漲', 'max_price': '0.2948', 'min_price': '0.2789', 'min_price_of_month': '0.2895', 'max_price_of_month': '0.2948', 'today_data': 現金買入    0.2785
現金賣出    0.2913
即期買入    0.2858
即期賣出    0.2898
Name: 2019-07-05 00:00:00, dtype: object, 'best_banks': (          現鈔買入    現鈔賣出    即期買入    即期賣出   更新時間               現鈔手續費
泰國盤谷銀行      --      --  0.2864  0.2904  17:26              免手續費
玉山銀行網銀      --      --  0.2861  0.2875  17:24           最低NT$100
王道銀行    0.2823  0.2893  0.2845  0.2885  17:24           最低NT$100
兆豐銀行    0.2776  0.2903  0.2848  0.2889  17:24               免手續費
星展銀行    0.2829  0.2904  0.2845  0.2888  17:21      總額1%,最低NT$100
台新銀行    0.2827  0.2907   0.285  0.2885  17:24            有賬戶免手續費
花旗銀行    0.2825  0.2908  0.2848  0.2885  17:24   總額0.35%,最低NT$100
玉山銀行    0.2838  0.2908  0.2848  0.2888  17:24     每筆NT$100 ATM免收 ,           現鈔買入    現鈔賣出    即期買入    即期賣出   更新時間               現鈔手續費
郵局      0.2783   0.292      --      --  17:24               免手續費
玉山銀行網銀      --      --  0.2861  0.2875  17:24           最低NT$100
王道銀行    0.2823  0.2893  0.2845  0.2885  17:24           最低NT$100
花旗銀行    0.2825  0.2908  0.2848  0.2885  17:24   總額0.35%,最低NT$100
台新銀行    0.2827  0.2907   0.285  0.2885  17:24            有賬戶免手續費
玉山銀行    0.2838  0.2908  0.2848  0.2888  17:24     每筆NT$100 ATM免收
星展銀行    0.2829  0.2904  0.2845  0.2888  17:21      總額1%,最低NT$100
兆豐銀行    0.2776  0.2903  0.2848  0.2889  17:24               免手續費 )}
```

It will also send report to line if you provide line token in configuration file /etc/mycurrency/mycurrency.config

Apply for line token here: https://notify-bot.line.me/zh_TW/

3. Provide which bank have cheaper price:

```
bestbank <currency>
```
For example:


```
[~/mycurrency] (master) 0h3m $ bestbank JPY
The top8 best cash sell price for currency JPY
=======================================================
          現鈔買入    現鈔賣出    即期買入    即期賣出   更新時間               現鈔手續費
泰國盤谷銀行      --      --  0.2864  0.2904  17:12              免手續費
玉山銀行網銀      --      --  0.2861  0.2875  17:12           最低NT$100
王道銀行    0.2823  0.2893  0.2845  0.2885  17:12           最低NT$100
兆豐銀行    0.2776  0.2903  0.2848  0.2889  17:12               免手續費
星展銀行    0.2829  0.2904  0.2845  0.2888  17:14      總額1%,最低NT$100
台新銀行    0.2827  0.2907   0.285  0.2885  17:12            有賬戶免手續費
玉山銀行    0.2838  0.2908  0.2848  0.2888  17:12     每筆NT$100 ATM免收
花旗銀行    0.2825  0.2908  0.2848  0.2885  17:12   總額0.35%,最低NT$100
=======================================================
The top8 best spot sell price for currency JPY
=======================================================
          現鈔買入    現鈔賣出    即期買入    即期賣出   更新時間               現鈔手續費
郵局      0.2783   0.292      --      --  17:12               免手續費
玉山銀行網銀      --      --  0.2861  0.2875  17:12           最低NT$100
花旗銀行    0.2825  0.2908  0.2848  0.2885  17:12   總額0.35%,最低NT$100
王道銀行    0.2823  0.2893  0.2845  0.2885  17:12           最低NT$100
台新銀行    0.2827  0.2907   0.285  0.2885  17:12            有賬戶免手續費
玉山銀行    0.2838  0.2908  0.2848  0.2888  17:12     每筆NT$100 ATM免收
星展銀行    0.2829  0.2904  0.2845  0.2888  17:14      總額1%,最低NT$100
兆豐銀行    0.2776  0.2903  0.2848  0.2889  17:12               免手續費
```
# requirement

python 3.7
