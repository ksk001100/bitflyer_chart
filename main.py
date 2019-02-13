import requests
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.font_manager import FontProperties
from datetime import datetime

# エンドポイント
end_point = 'https://bitflyer.jp/api/echo/price'

# APIからデータ取得
response = requests.get(end_point)
rate = json.loads(response.text)

# 日本語を表示するためにフォントを設定
fp = FontProperties(fname='ipaexg.ttf', size=15)

# ウィンドウを描画
fig = plt.figure(figsize=(12,8))

# データ用の配列を初期化
time_axis = [datetime.now() for _ in range(120)]
mid = [rate['mid'] for _ in range(120)]
bid = [rate['bid'] for _ in range(120)]
ask = [rate['ask'] for _ in range(120)]

# コールバック関数
def plot(loop_count):

    # グラフをリフレッシュ
    plt.cla()

    # APIからデータ取得
    response = requests.get(end_point)
    rate = json.loads(response.text)

    # 配列の先頭を削除
    time_axis.pop(0)
    mid.pop(0)
    bid.pop(0)
    ask.pop(0)

    # 配列の最後にデータを追加
    time_axis.append(datetime.now())
    mid.append(rate['mid'])
    bid.append(rate['bid'])
    ask.append(rate['ask'])

    # プロット
    plt.plot(time_axis, mid, label='仲値')
    plt.plot(time_axis, bid, label='買取価格')
    plt.plot(time_axis, ask, label='販売価格')

    # ラベル配置
    plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0, prop=fp) 
    plt.subplots_adjust(right=0.8)

# 1000ms(1s)でアニメーションを更新
ani = FuncAnimation(fig, plot, interval=1000)

# 描画
plt.show()
