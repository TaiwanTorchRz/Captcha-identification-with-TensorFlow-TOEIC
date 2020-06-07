import os,shutil
a=next(os.walk('./data_'))[1]
for b in a:
    try:
        os.mkdir('./data/train/'+b)
    except:
        pass
    try:
        os.mkdir('./data/valid/'+b)
    except:
        pass
for b in range(len(a)):
    count=0
    c=next(os.walk('./data_/'+a[b]))[2]
    total=len(c)
    train=int(total*0.7)
    valid=total-train
    for d in c:
        count+=1
        if count<=train:
            shutil.copy('./data_/'+a[b]+'/'+d,'./data/train/'+a[b]+'/'+d)
        else:
            shutil.copy('./data_/'+a[b]+'/'+d,'./data/valid/'+a[b]+'/'+d)
        print(count)
