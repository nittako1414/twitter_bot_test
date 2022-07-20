import requests
import json
import datetime
import tweepy

# twitterのapiデータ
api_key = "rkq7sajRcLyN1axBEEi12jTgh"
api_key_secret = "un1hEVCysTU4WSjbdwkRW7qGKb4d73PGSItnC9vAyCNGMnWgqA"
access_token = "1431858272974229504-IkSA7gKQahyi9DkSyKA6Mu0XZuEJvJ"
access_token_secret = "dJS9EVYGOpuYXumkOidgyvpin6Nok4S7GyafWEsYCtYnq"

# Tweepyを利用し、OAuth認証にアクセストークンを設定
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 今日の日付
date = datetime.datetime.today().strftime("%Y/%m/%d")

# 星座占いのAPIからデータ取得
# dateを足して「http://api.jugemkey.jp/api/horoscope/year/month/day」の形式にする
res = requests.get(url='http://api.jugemkey.jp/api/horoscope/free/' + date)

# print(json.dumps(json.loads(res.text), indent=4, ensure_ascii=False))

# 山羊座を取得
# {'horoscope': {date : [各星座のデータ] } }
horoscope = res.json()['horoscope'][date][9]
# print(horoscope)
rank = horoscope["rank"]
if rank < 5:
    text = '今日のあなたはサイコーです！'
    api.update_status(text)

