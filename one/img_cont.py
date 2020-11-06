import os
import PIL
from PIL import Image
from PIL import ImageEnhance
from tqdm import tqdm

first_num = 82
last_num = 84
folder_name = "201013-vib"

for th in tqdm((1,2,3,4,5,6,7,8,9,10)):
    TH=str(th)
    os.mkdir("enhance_test/"+folder_name+"_"+TH)

    for num in tqdm(range (first_num,last_num)):
        im_name=str(num)
        fileA_name=im_name.zfill(6)+".jpg"
        enhance_im_name=im_name.zfill(6)+".jpg"
        im = Image.open(folder_name+"/"+fileA_name)
        im = im.convert('L')
        im = ImageEnhance.Contrast(im)
        im = im.enhance(th)
        im = im.crop((410,977,1069,1378))
        im.save("enhance_test/"+folder_name+"_"+TH+"/"+fileA_name)
