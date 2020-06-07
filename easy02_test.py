import os,random,io
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import initializers

inputs = keras.Input(shape=(30,15,3))
x = layers.Conv2D(64,(3,3),input_shape=(30,15,3),activation='relu')(inputs)
x = layers.MaxPool2D()(x)
x = layers.Conv2D(128,(3,3),input_shape=(30,15,3),activation='relu')(x)
x = layers.Conv2D(64,(3,3),input_shape=(30,15,3),activation='relu')(x)
#x = layers.Conv2D(32,(3,3),input_shape=(30,15,3),activation='relu')(x)
#x = layers.Conv2D(64,(3,3),input_shape=(30,15,3),activation='relu')(x)
x = layers.Flatten()(x)
x = layers.Dense(128, activation='relu')(x)
x = layers.Dropout(0.5)(x)
outputs = layers.Dense(43,activation='softmax')(x)
model = keras.Model(inputs,outputs,name = 'model')
model.load_weights('.\\best_model.h5')
def read_img(path,resize=(30,15)):
    img_st = tf.io.read_file(path)
    img_decode = tf.image.decode_image(img_st)
    img_decode = tf.image.resize(img_decode,resize)
    #img_decode = tf.cast(img_decode,tf.float32)/255.
    img_decode = tf.image.convert_image_dtype(img_decode, tf.float32)
    img_decode = tf.expand_dims(img_decode,axis=0)
    return img_decode

#先定義data位置
data_dir = './data'
train_path = data_dir+'/train/'
valid_path = data_dir+'/valid/'

#獲取標籤名稱
label = next(os.walk(train_path))[1]
print(label)
img=read_img('./test0.jpg')
b = list(np.array(model.predict(img))[0])
print(b)
#    try:
#        print(a,label[b.index(1)])
#    except:
#       print(a,b)
print(label[b.index(max(b))])
input(':')
