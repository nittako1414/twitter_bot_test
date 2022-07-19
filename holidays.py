import datetime
from bs4 import BeautifulSoup
import requests, json, os
import tweepy
from dotenv import find_dotenv, load_dotenv


# .env読み込み
# load_dotenv()
# api_key = os.getenv('api_key')
# api_key_secret = os.getenv('api_key_secret')
# access_token = os.getenv('access_token')
# access_token_secret = os.getenv('access_token_secret')

api_key = "rkq7sajRcLyN1axBEEi12jTgh"
api_key_secret = "un1hEVCysTU4WSjbdwkRW7qGKb4d73PGSItnC9vAyCNGMnWgqA"
access_token = "1431858272974229504-IkSA7gKQahyi9DkSyKA6Mu0XZuEJvJ"
access_token_secret = "dJS9EVYGOpuYXumkOidgyvpin6Nok4S7GyafWEsYCtYnq"

# Tweepyを利用し、OAuth認証にアクセストークンを設定
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Holidays JP APIのURL
holidays_url = "https://holidays-jp.github.io/api/v1/date.json"

# 祝日一覧APIからデータを取得
res = requests.get(holidays_url)
holidays = json.loads(res.text)
# 比較するための今日の日付
today = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d").date()
# 今日より後の日付の祝日を探す
for k, v in holidays.items():
    holiday = datetime.datetime.strptime(k, "%Y-%m-%d").date()
    # 今日より日付が後だったら（当日を含むので、<=比較）
    if today <= holiday:
        # 次の祝日（今日が2021-08-30の場合は、「2021-09-20」　）
        near_holiday_date = holiday
        # どういう祝日か（2021-09-20は、敬老の日）
        near_holiday_value = v
        # for文終わる
        break

# 祝日までの日数を計算（祝日から今日の日付を引く）
diff_date = near_holiday_date - today
# 文字列に変換
diff_date = str(diff_date.days)
# テキストを組み立てる
holiday_text = '次の祝日（' + near_holiday_value + '）までは' + diff_date + '日です。'

# print(holiday_text)   # 次の祝日（敬老の日）までは21日です。

# TLへの投稿テスト
# print("文章を入力してください。")
# text = input()  # ユーザーの入力を取得
# api.update_status(text)


# 阿部寛
# 阿部 寛さんのホームページのURL
url = 'http://abehiroshi.la.coocan.jp/'
# iframeで別HTMLを読んでるみたいなのでページのURL
page_url = 'top.htm'

# ページのデータを取得
response = requests.get(url + page_url)
html = response.content
soup = BeautifulSoup(html, "html.parser")
# HTMLデータから画像を探す
img_src = soup.find("img").get("src")

# 画像にアクセス
resp = requests.get(url + img_src)
# 404なら知らせる
if resp.status_code == 404:
    abe_text = '阿部 寛さんの画像リンクが切れています。'
else:
    abe_text = '画像は今日も問題ないです。'

# holiday_textの投稿
text = "@reentrant1732 今日の巡回結果だよ！\n \n" + holiday_text + '\n' + abe_text
api.update_status(text)



