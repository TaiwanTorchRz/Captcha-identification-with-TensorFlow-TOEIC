import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import time,os

def inputs_event(event):
    global last_img,last_label,path,upath,img_index,mode2
    label = inputs.get()
    if mode2:
        if label.isupper():
            label+='_upper'
    if label!='':
        img_index+=1
        inputs.delete(0,'end')
        if img_index<len(file_name):
            if not last_label=='':
                save_image(upath+file_name[img_index-2],path+'\\'+last_label+'\\'+file_name[img_index-2])
            last_label=label
            button["state"] = "normal"
            set_image()
        elif img_index==len(file_name):
            button["state"] = "disabled"
            if not last_label=='':
                save_image(upath+file_name[img_index-2],path+'\\'+last_label+'\\'+file_name[img_index-2])
            save_image(upath+file_name[img_index-1],path+'\\'+label+'\\'+file_name[img_index-1])
        else:
            pass
        set_tip_text()
        

def last_picture():
    global img_index,last_label
    img_index-=1
    button["state"] = "disabled"
    last_label=''
    set_image()

def save_image(origin,target):
    try:
        os.mkdir('\\'.join(target.split('\\')[0:-1]))
    except:
        pass
    os.rename(origin,target)
    f=open('./last_save.txt','w')
    f.write(origin)
    f.close()

def set_image():
    global img_index,upath,last_img,img
    print(file_name[img_index])
    last_img=img
    img = Image.open(upath+file_name[img_index]).resize((51,90),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    imLabel.configure(image=img)
    imLabel.image = img

def set_tip_text():
    global path
    labels = next(os.walk(path))[1]
    st='Label\n\n'
    st2='num\n\n'
    for label in labels:
        num = len(next(os.walk(path+'\\'+label))[2])
        st+=label+'\n'
        st2+=str(num)+'\n'
    var.set(st)
    var2.set(st2)


if __name__ == '__main__':
    
    path=input('path:')#r'C:\Users\cliffsu\Desktop\Tensorflow\verification_code\sample'
    support = ['bmp','tiff','tif','png','gif','jpeg','jpg','webp']
    mode=1 if input('\nAuto remove the files are not Supported image? Supported formate: '+str(support)+'\n(this can be dangerous! n for default) (y/n):').lower()=='y' else 0
    mode2=1 if input('\nupper lower auto detect?(y/n):').lower()=='y' else 0
    path = path.replace('/','\\')
    upath = path+'\\'+'unlabeled\\'
    file_name=next(os.walk(upath))[2]

    n_support=0
    for a in file_name:
        if not a.split('.')[-1].lower() in support:
            n_support+=1
            file_name.remove(a)
            if mode:
                os.remove(upath+a)

    print('not support file num:',n_support)
    img_index=0
    last_img = ''
    last_label = ''
    window=tk.Tk()
    window.title('labeler.py')
    window.geometry('400x700')
    window.resizable(0,0)

    inputs=tk.Entry(window)
    inputs.bind("<Return>",inputs_event)
    inputs.place(x=70,y=150)
    
    button=tk.Button(
    window,
    padx=10,
    pady=10,
    text='上一張',
    command=last_picture)
    button.place(x=5,y=50)
    button["state"] = "disabled"

    img = Image.open(upath+file_name[0]).resize((51,90),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    imLabel=tk.Label(window,image=img)
    imLabel.place(x=120,y=30)
    
    
    var = tk.StringVar()
    var2 = tk.StringVar()
    set_tip_text()
    label_tips = tk.Label(window,textvariable=var)
    label_tips.place(x=240,y=10)
    label_num = tk.Label(window,textvariable=var2)
    label_num.place(x=310,y=10)

    #im=Image.open(r'C:\Users\cliffsu\Desktop\Tensorflow\verification_code\sample.jpg')
    #img=ImageTk.PhotoImage(im)
    #imLabel=tk.Label(window,image=img).pack()
    #root.mainloop()
    window.mainloop()
