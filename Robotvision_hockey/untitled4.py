# ライブラリのインポート
import copy
import time
import cv2
import numpy as np

from Ball import Ball


#中心の画素に類似した色の範囲を取得する関数



#画像から特定の範囲の色のみを抽出して二値画像にする関数



#上の関数で出た画像のオプティカルフローを取得



#メインの処理
# Webカメラ設定
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
ret, frame = cap.read() #frameは(480,640,3)
ball_img = cv2.imread("./image_data/ball.png")
stadium_img = cv2.imread("./image_data/stadium.png")
# Webカメラの画面の大きさにスタジアムを合わせる
stadium_img = cv2.resize(stadium_img, (frame.shape[1], frame.shape[0]))

# ボールの高さ、幅の[半分](半分だから注意！！)
# (注意!)今回ボールの大きさが H:198、W:200と両方偶数のためこれで良いが、奇数の場合は工夫が必要
ball_h, ball_w = ball_img.shape[0] // 2, ball_img.shape[1] // 2

# ボールの初期位置（中心座標)をスタジアムの中心に設定
idx_h = stadium_img.shape[0] // 2
idx_w = stadium_img.shape[1] // 2



ball = Ball(idx_h,idx_w,stadium_img.shape[0],stadium_img.shape[1],ball_h,ball_w)
# 実行
while True:
    time.sleep(0.01)
    
    ret, frame = cap.read() #frameは(480,640,3)
    stadium = copy.deepcopy(stadium_img)
   # print((ball.y - ball_h) ,(ball.y + ball_h), (ball.x- ball_w) , (ball.y + ball_w),ball.y,ball.x,ball_h,ball_w)
    stadium[(ball.y - ball_h) : (ball.y + ball_h), (ball.x- ball_w) : (ball.x + ball_w)] = ball_img
    cv2.imshow("output", stadium)
    ball.move()
    k = cv2.waitKey(1)

    

    if k == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

    