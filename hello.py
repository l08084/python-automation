import time
from selenium import webdriver

# Chromeを起動する
driver = webdriver.Chrome()
# Googleのページを開く
driver.get('https://www.google.com')
# ページが開くまで待つ
time.sleep(5)
# 検索ボックスのオブジェクトを得る
q = driver.find_element_by_name('q')
# 検索ボックスにキーを送信する
q.send_keys('まちカドまぞく')
# フォームを投稿する
q.submit()
# 結果を30秒表示して終了する
time.sleep(30)
driver.quit()