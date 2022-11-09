"""
Pythonでデータセットを作る方法とデータセットの中身を確認する方法（npz編）
https://tomomai.com/python-dataset/
"""

#画像ファイルを読み込んでnumpy配列に変換
#画像にラベルをつけて保存

import numpy as np
import glob, os, random
from PIL import Image

#保存ファイル名, npzファイル
out_file="./images/dataset.npz"
#利用する画像の枚数
Nmax=200
#画像データ
x=[]
#画像ラベル
y=[]

#main
def main():
    #指定した画像ファイル、ラベルを関数に渡す
    classes=5
    hono="./images/hono_face"
    katoshi="./images/katoshi_face"
    kyonko="./images/kyonko_face"
    otake="./images/otake_face"
    rena="./images/rena_face"

    paths=[hono, katoshi, kyonko, otake, rena]

    for i in range(classes):
        get_dataset(path=paths[i], label=i)

    #データセットの保存
    np.savez(out_file, x=x, y=y)
    print("make_dataset completed: "+out_file, len(x))

#データセットを作る関数、引数：画像ファイルのパス、ラベル
def get_dataset(path, label):
    #フォルダ内画像ファイル読み込み
    files=glob.glob(path+"/*.jpg")
    random.shuffle(files)

    #各ファイルの処理
    num=0
    for f in files:
        if num>=Nmax:
            break
        num+=1

        #画像ファイル一枚読み込み
        img=Image.open(f)
        #RGB変換
        img=img.convert("RGB")
        #numpy配列に変換、0-1に正規化
        img=np.asarray(img)
        img=img/225
        #x,yに画像とラベルを追加
        x.append(img)
        y.append(label)
    print(f"{label}:{len(x)}")

if __name__=='__main__':
    main()
