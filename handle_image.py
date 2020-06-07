import cv2,os
import numpy as np
import tensorflow as tf
import multiprocessing as mp
from functools import partial
print(0)
def read_image(file):
    r = tf.io.read_file(file)
    image_decode = tf.image.decode_jpeg(r, channels=3)
    #image_decode = tf.expand_dims(image_decode,axis=0)
    return image_decode

def handle(path,name2):
    try:
        name = name2.split('.jpg')[0]
        path2 = path+'\\unlabeled\\'
        file = path+'\\'+name2
        img = read_image(file)
        cropped = tf.image.crop_to_bounding_box(img, 0,8,30,17)
        cropped2 = tf.image.crop_to_bounding_box(img, 0,24,30,17)
        cropped3 = tf.image.crop_to_bounding_box(img, 0,40,30,17)
        cropped4 = tf.image.crop_to_bounding_box(img, 0,56,30,17)
        enc = tf.image.encode_jpeg(cropped)
        enc2 = tf.image.encode_jpeg(cropped2)
        enc3 = tf.image.encode_jpeg(cropped3)
        enc4 = tf.image.encode_jpeg(cropped4)
        tf.io.write_file(path2+name+'_1.jpg',enc)
        tf.io.write_file(path2+name+'_2.jpg',enc2)
        tf.io.write_file(path2+name+'_3.jpg',enc3)
        tf.io.write_file(path2+name+'_4.jpg',enc4)
    except:
        f=open('error.txt','a+')
        f.write(path+'\\'+name2+'\n')
        f.close()
        
handle('C:\\Users\\a0922\\Desktop\\test\\pic','219.jpg')
##if __name__=='__main__':
##    path = input('path:')
##    path = path.replace('/','\\')
##    try:
##        os.mkdir(path2)
##    except:
##        pass
##    func = partial(handle,path)
##    names = next(os.walk(path))[2]
##    pool = mp.Pool()
##    pool.map(func,names)
