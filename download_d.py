import time
import os
import requests
from selenium import webdriver
import chromedriver_binary
from d_credentials import *


# パスワードの指定
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

# カード会社のページを開く
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

# データのダウンロードリンク先を取得
time.sleep(5)
# tag = driver.find_element_by_link_text('CSVをダウンロードする')
driver.execute_script("doSubmitForm(document.download_form)")
# driver.execute_script(
#     "document.querySelector('.csv-print_bottom p a').click();")

# 結果を30秒表示して終了する
time.sleep(30)
driver.quit()
