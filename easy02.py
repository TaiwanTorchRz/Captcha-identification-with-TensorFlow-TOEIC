

###################     USEFUL　TOOL     ########################
import os,random,io
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds

###################     USEFUL　TOOL     ########################

def color(x):
    x = tf.image.random_hue(x,0.08)
    x = tf.image.random_saturation(x,0.6,1.6)
    x = tf.image.random_brightness(x,0.05)
    x = tf.image.random_contrast(x,0.7,1.3)
    return x

def get_label(file_path):
  #分割path
  #ex : c://test//abc.jpg --→ ['c:','test','abc.jpg']
  parts = tf.strings.split(file_path, os.path.sep)
  #class name 為 前面定義之標籤
  #parts[-2]為我們標命名 data//(label)//*.jpg 中(label)資料夾的名稱
  #a = parts[-2] == CLASS_NAMES的用意為取的熱鍵編碼
  #此為numpy之特殊用法
  #ex: b='123' a=np.array(['123','456','789']) a==b --→ [True,False,False]
  a = parts[-2] == CLASS_NAMES
  return a

def decode_img(img,IMG_WIDTH=15,IMG_HEIGHT=30):
  # convert the compressed string to a 3D uint8 tensor
  img = tf.image.decode_jpeg(img, channels=3)
  return tf.image.resize(img, [IMG_HEIGHT,IMG_WIDTH])
def process_path(file_path):
  #取得label的熱鍵編碼
  label = get_label(file_path)
  # load the raw data from the file as a string
  img = tf.io.read_file(file_path)
  # decode raw data to image
  img = decode_img(img)
  #回傳為(image(輸入),label(輸出))
  return img, label
def hand_pic(x,y):
    x = tf.cast(x,tf.float32)/255.
    return x,y
def rnd_pic(x,y):
    x = tf.cast(x,tf.float32)/255.
    x = tf.cond(tf.random.uniform([],0,1)>0.0,lambda:color(x),lambda:x)#0.5
    return x,y


#先定義data位置
data_dir = './data'
train_path = data_dir+'/train/'
valid_path = data_dir+'/valid/'

#獲取標籤名稱
label = next(os.walk(train_path))[1]
#將標籤名稱轉為np array
CLASS_NAMES = np.array(label)
print(CLASS_NAMES)

#取得train、val的樣本數量，以利在後面處理圖片時可以使用
total_train = 0
total_val = 0
for a in label:
    for b in next(os.walk(train_path+a))[2]:
        if b.lower().count('.jpg')>0:
            total_train+=1
for a in label:
    for b in next(os.walk(valid_path+a))[2]:
        if b.lower().count('.jpg')>0:
            total_val+=1
print(total_train,total_val)

#定義batchsize數量
batch_size=20#64
#定義自動調整
AUTOTUNE = tf.data.experimental.AUTOTUNE

#利用tensorflow dataset的方便功能讀入 train_path 中所有jpg檔案 , 且先不要打亂
list_ds = tf.data.Dataset.list_files(str(train_path+'*.jpg'),shuffle=False)


####     注意 labeled_ds_train、labeled_ds_valid 只是先定義，真正執行是在訓練時     ####

#讀入正式的要訓練的圖片，tfds的用法
#將list_ds中所有資料(所有圖片之路徑) map(用多核心) 帶入到process_path函式
#使用核心數量自動調整
#請依定要參考上方process_path函式
labeled_ds_train = list_ds.map(process_path, num_parallel_calls=AUTOTUNE)

#設定快取、打亂、將圖片隨機化(顏色)、設定batch、預取等
labeled_ds_train = labeled_ds_train.cache().shuffle(total_train).map(hand_pic,num_parallel_calls=AUTOTUNE).batch(batch_size).prefetch(buffer_size=AUTOTUNE)
#rnd_pic為標準化圖片且隨機化，process_path只標準化圖片
#注意 在訓練時train data可隨機化以提升模型準確率，valid data可不用以節省效能


#將動作重複於valid
list_ds = tf.data.Dataset.list_files(str(valid_path+'*.jpg'),shuffle=False)
labeled_ds_valid = list_ds.map(process_path, num_parallel_calls=AUTOTUNE)
labeled_ds_valid = labeled_ds_valid.cache().map(hand_pic,num_parallel_calls=AUTOTUNE).batch(batch_size).prefetch(buffer_size=AUTOTUNE)



#搭建模型，這裡要靠經驗，無準確答案
#Conv2D , MaxPool2D , Flatten , Dense 等可以上網意思
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

#定義模型儲存路徑
model_dir='lab10-logs/models'
try:
    os.makedirs(model_dir)
except:
    pass
log_dir = 'lab10-logs\\model-1' 

#定義tensorboard callback log 以追蹤模型訓練進度
model_cbk = keras.callbacks.TensorBoard(log_dir=log_dir)

#定義checkpoint callback以記錄最佳模型
# monitor為以此種數值類定義為最佳，這裡以辨識準確度當monitor
# mode 為此數值越大越好還是越小越好，因為monitor為準確度，所以mode是max
mckpt = keras.callbacks.ModelCheckpoint(model_dir+'\\best_model.h5',monitor='val_categorical_accuracy',mode='max',save_best_only=True)

#定義模型之優化器、損失函數、指標函數
#CategoricalCrossentropy 為多分類問題
#CategoricalAccuracy 為分類準確率
model.compile(keras.optimizers.Adam(),loss=keras.losses.CategoricalCrossentropy(),metrics=[keras.metrics.CategoricalAccuracy()])



#最後model.fit開始訓練，前面輸入為train資料 
# epochs為訓練總次數 
# validation_data為驗證資料
# callbacks表示在訓練模型時要呼叫的函示
history = model.fit(labeled_ds_train,epochs=100,validation_data=labeled_ds_valid,callbacks=[model_cbk,mckpt])

