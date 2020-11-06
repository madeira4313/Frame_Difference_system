#!/usr/bin/env python3.8

#モジュールのインポート
import os
import cv2
from tqdm import tqdm
import numpy as np
import pathlib

def mkdiffimgfiles_0_0(foldar_name,first_num,last_num,th,time):

    # 閾値をstr化
    TH=str(th)

    #保存先パス名の取得
    basename = os.path.basename(foldar_name)
    p_sub = pathlib.Path(foldar_name)
    p_sub_name= str(p_sub.parent)

    # オープニング処理の実行値
    kernel = np.ones((5,5),np.uint8) # 5*5の矩形kernel、隣接2マスまで処理

    # 差分画像の保存先指定
    os.mkdir(p_sub_name+'/th_imgs/'+basename+'_'+time)

    # 作成する差分画像の開始から終了まで
    for num in tqdm(range (first_num,last_num)):

        ImA_num = num
        ImB_num = num+1

        ImA_name=str(ImA_num)
        ImB_name=str(ImB_num)

        fileA_name=ImA_name.zfill(6)+".jpg"
        fileB_name=ImB_name.zfill(6)+".jpg"
        diff_name=ImA_name.zfill(6)+"_diff.jpg"

        # 前後2画像ファイルの読み込み
        imA=cv2.imread(foldar_name+"/"+fileA_name,0)
        imB=cv2.imread(foldar_name+"/"+fileB_name,0)

        # 2ファイルから差分画像の作成
        img_dst = cv2.absdiff(imA,imB)

        # 閾値からバイナリー処理
        th, img_dst_binary = cv2.threshold(img_dst,th,255,cv2.THRESH_BINARY)

        # オープニング処理
        img_dst_binary_op = cv2.morphologyEx(img_dst_binary, cv2.MORPH_OPEN, kernel)

        #差分画像の保存
        cv2.imwrite(p_sub_name+'/th_imgs/'+basename+'_'+time+"/"+diff_name,img_dst_binary_op)

    # cv2モジュールの終了
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def mkdiffimgfiles_0_1(foldar_name,first_num,last_num,th,time):

    TH=str(th)
    basename = os.path.basename(foldar_name)
    p_sub = pathlib.Path(foldar_name)
    p_sub_name= str(p_sub.parent)
    kernel = np.ones((5,5),np.uint8) # 5*5の矩形kernel、隣接2マスまで処理
    os.mkdir(p_sub_name+'/th_imgs/'+basename+'_'+time)

    for num in tqdm(range (first_num,last_num)):

        ImA_num = num
        ImB_num = num+1

        ImA_name=str(ImA_num)
        ImB_name=str(ImB_num)

        fileA_name=ImA_name.zfill(6)+".jpg"
        fileB_name=ImB_name.zfill(6)+".jpg"
        diff_name=ImA_name.zfill(6)+"_diff.jpg"

        imA=cv2.imread(foldar_name+"/"+fileA_name,0)
        imB=cv2.imread(foldar_name+"/"+fileB_name,0)

        img_dst = cv2.absdiff(imA,imB)

        th, img_dst_binary = cv2.threshold(img_dst,th,255,cv2.THRESH_BINARY)

        cv2.imwrite(p_sub_name+'/th_imgs/'+basename+'_'+time+"/"+diff_name,img_dst_binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def mkdiffimgfiles_1_0(foldar_name,first_num,last_num,time):

    basename = os.path.basename(foldar_name)
    p_sub = pathlib.Path(foldar_name)
    p_sub_name= str(p_sub.parent)
    kernel = np.ones((5,5),np.uint8) # 5*5の矩形kernel、隣接2マスまで処理
    os.mkdir(p_sub_name+'/th_imgs/'+basename+"_"+time)

    for num in tqdm(range (first_num,last_num)):

        ImA_num = num
        ImB_num = num+1

        ImA_name=str(ImA_num)
        ImB_name=str(ImB_num)

        fileA_name=ImA_name.zfill(6)+".jpg"
        fileB_name=ImB_name.zfill(6)+".jpg"
        diff_name=ImA_name.zfill(6)+"_diff.jpg"

        imA=cv2.imread(foldar_name+"/"+fileA_name,0)
        imB=cv2.imread(foldar_name+"/"+fileB_name,0)

        fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()#マスク画像の作成

        fgmask = fgbg.apply(imA)
        fgmask = fgbg.apply(imB)

        fgmask_op = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

        cv2.imwrite(p_sub_name+'/th_imgs/'+basename+'_'+time+"/"+diff_name,fgmask_op)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def mkdiffimgfiles_1_1(foldar_name,first_num,last_num,time):

    basename = os.path.basename(foldar_name)
    p_sub = pathlib.Path(foldar_name)
    p_sub_name= str(p_sub.parent)
    os.mkdir(p_sub_name+'/th_imgs/'+basename+"_"+time)

    for num in tqdm(range (first_num,last_num)):

        ImA_num = num
        ImB_num = num+1

        ImA_name=str(ImA_num)
        ImB_name=str(ImB_num)

        fileA_name=ImA_name.zfill(6)+".jpg"
        fileB_name=ImB_name.zfill(6)+".jpg"
        diff_name=ImA_name.zfill(6)+"_diff.jpg"

        imA=cv2.imread(foldar_name+"/"+fileA_name,0)
        imB=cv2.imread(foldar_name+"/"+fileB_name,0)

        fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()#マスク画像の作成

        fgmask = fgbg.apply(imA)
        fgmask = fgbg.apply(imB)

        cv2.imwrite(p_sub_name+'/th_imgs/'+basename+'_'+time+"/"+diff_name,fgmask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
