"""
元画像, 顔抽出, 水増し後
田村保乃:251, 223,
加藤史帆:261, 245,
齊藤京子:284, 250,
高本彩花:262, 239,
守屋麗奈:249, 206,

#データセットを作成してから水増し処理をして、そのデータで学習することにする
#水増し画像も保存すると容量がかさばるから

"""

########################################################
"""
データの水増し
0:オリジナル、1:回転、2:ぼかし
"""
import cv2
import numpy as np

photos=np.load("./images/dataset.npz")
x=photos['x']
y=photos['y']

x_new=[]
y_new=[]

for i, xi in enumerate(x):
  yi=y[i]
  for ang in range(-20, 20, 5):
    #オリジナル左右反転
    xi0=cv2.flip(xi, 1)
    x_new.append(xi0)
    y_new.append(yi)

    #回転
    center=(64, 64)
    mtx=cv2.getRotationMatrix2D(center, ang, 1.0)
    xi1=cv2.warpAffine(xi, mtx, (128,128))
    x_new.append(xi1)
    y_new.append(yi)

    #回転と左右反転
    xi10=cv2.flip(xi1, 1)
    x_new.append(xi10)
    y_new.append(yi)

    #ぼかし
    xi2=cv2.GaussianBlur(xi,(5,5),0)
    x_new.append(xi2)
    y_new.append(yi)

x=np.array(x_new)
y=np.array(y_new)

print(len(y))

########################################################
"""
データの水増し
0:オリジナル、1:回転、2:ぼかし
"""