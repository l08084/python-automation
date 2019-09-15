import time
import os
import requests
from selenium import webdriver
import chromedriver_binary
from rakuten_credentials import *

# ユーザIDとパスワードを別ファイルから取得する
user_id = ID
password = PASS
download_dir = os.path.dirname(__file__)

# 保存先などオプションを指定してChromeを起動
opt = webdriver.ChromeOptions()
opt.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "plugin.always_open_pdf_externally": True
})
driver = webdriver.Chrome(options=opt)

# 楽天カードの利用明細についてのページを開く
driver.get('https://www.rakuten-card.co.jp/e-navi/index.xhtml')
time.sleep(3)

# ログイン画面のユーザー欄にユーザIDを入力
driver.find_element_by_name('u').send_keys(user_id)

# ログイン画面のパスワード欄にパスワードを入力
driver.find_element_by_name('p').send_keys(password)

# ログインボタンを押下する
driver.find_element_by_id('loginButton').click()

# 利用明細画面に遷移する
driver.find_element_by_link_text('明細を見る').click()

# 利用明細CSVのダウンロードリンク先を取得
tag = driver.find_element_by_css_selector('.stmt-c-btn-dl.stmt-csv-btn')
href = tag.get_attribute('href')

# Chromeからクッキーデータを得る
c = {}
for cookie in driver.get_cookies():
    c[cookie['name']] = cookie['value']
# requestsを利用してデータのダウンロード
r = requests.get(href, cookies=c)
with open("rakuten-card.csv", 'wb') as f:
    f.write(r.content)

# 30秒待ってから終了する
time.sleep(30)
driver.quit()
