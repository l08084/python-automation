import time
import os
import requests
from selenium import webdriver
import chromedriver_binary
from d_credentials import *

# ユーザIDとパスワードを別ファイルから取得する
user_id = ID
password = PASS

# Chromeを起動
driver = webdriver.Chrome()

# Dカードの利用明細についてのページを開く
driver.get('https://d-card.smt.docomo.ne.jp/tknsrv?strURL=https%3A%2F%2Fwww5.dcmx.jp%2Fdcmx%2Fmeisai%3FprocessCode%3D03Meisai%26pn%3D1#_ga=2.194953003.729480172.1567333046-1119956819.1567333046')
time.sleep(3)

# ログイン画面のユーザー名にキーを送信
u = driver.find_element_by_name('authid')
u.send_keys(user_id)
u.submit()

# ログイン画面のパスワードにキーを送信
u = driver.find_element_by_name('authpass')
u.send_keys(password)
u.submit()

# 今月の利用明細CSVをダウンロードする
driver.execute_script("doSubmitForm(document.download_form)")

# 60秒待ってから終了する
time.sleep(60)
driver.quit()
