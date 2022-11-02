"""
【Python】dlibで顔検出
https://predora005.hatenablog.com/entry/2021/08/30/190000
"""

import cv2
import dlib
import glob

hono="./images/hono"
katoshi="./images/katoshi"
kyonko="./images/kyonko"
otake="./images/otake"
rena="./images/rena"

#入力画像
in_dirs=[hono, katoshi, kyonko, otake, rena]

#出力画像
out_dirs=[]
for i in range(len(in_dirs)):
    out_dirs.append(in_dirs[i]+"_face")
    print(out_dirs[i])

# #画像のID
fid=1000

# #画像のリサイズするか（しない）
flag_resize=False

# #Dlibのインスタンス
detector=dlib.get_frontal_face_detector()

#顔画像を取得して保存
def get_face(fname,index):
    global fid
    #画像読み込み
    img=cv2.imread(fname)

    #サイズが大きければリサイズ
    if flag_resize:
        img=cv2.resize(img, None, fx=0.2, fy=0.2)

    #顔検出
    dets=detector(img)
    for i,d in enumerate(dets):
        x1=int(d.left())
        y1=int(d.top())
        x2=int(d.right())
        y2=int(d.bottom())
        im=img[y1:y2, x1:x2]

        #リサイズ(128x128)にして保存
        try:
            im=cv2.resize(im, (128,128))
        except:
            continue
        
        out=out_dirs[index]+"/"+str(fid)+".jpg"
        cv2.imwrite(out, im)
        fid+=1
    

# #指定したフォルダにある画像から顔抽出
for i in range(1,len(in_dirs)): 
    files=glob.glob(in_dirs[i]+"/*")

    for file in files:
        print(file)
        get_face(fname=file, index=i)

    print(f"{in_dirs[i]} ok.")


"""
元画像のリサイズなしの方が多く顔検出できた
リサイズすると、人物が変形しがち
田村保乃:251, 223
加藤史帆:261, 245
齊藤京子:284, 250
高本彩花:262, 239
守屋麗奈:249, 206
"""