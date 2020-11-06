#!/usr/bin/env python
import os
from PIL import Image
from tqdm import tqdm
import os.path
import pathlib

def cropimage_files(foldar_name,first_num,last_num,Acrop,time):

    basename = os.path.basename(foldar_name)
    p_sub = pathlib.Path(foldar_name)
    p_sub_name= str(p_sub.parent)

    for x in ["A"]:
        os.mkdir(p_sub_name+'/crop_imgs/'+basename+"_"+x+'_'+time)

    for num in tqdm(range (first_num,last_num)):
        file_num= str(num)
        file_name= file_num.zfill(6)+"_diff.jpg"

        im = Image.open(p_sub_name+'/th_imgs/'+basename+'_'+time+'/'+file_name)
        im_1=im.crop((Acrop))
        im_1.save(p_sub_name+'/crop_imgs/'+basename+'_A_'+time+'/'+file_name)
