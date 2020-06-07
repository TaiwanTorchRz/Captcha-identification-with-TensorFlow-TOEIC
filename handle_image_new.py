import cv2,os
count=0
try:
    os.mkdir('./data_/unlabeled')
except:
    pass
for b in range(250):
    img = cv2.imread('.\\pic\\'+str(b)+'.jpg')
    height=img.shape[0]
    weidth=img.shape[1]
    weidth_w=17
    early=9999
    end=0
    early2=9999
    end2=0
    early3=9999
    end3=0
    early4=9999
    end4=0
    early5=9999
    end5=0
    #if 1:
    #    a=15
    for a in range(len(img)):
        for c in range(len(img[a])):
            #print(c)
            if img[a][c][0]>150 and img[a][c][1]<40 and img[a][c][2]<40:
                #print(img[a][c],c)
                if c<early:
                    early=c
                break
    out_w=0
    for c in range(early+5,len(img[0])):
        check_in=False
        for a in range(len(img)):
            if img[a][c][0]>130 and img[a][c][1]<40 and img[a][c][2]<45:
                check_in=True
        if not check_in:
            out_w+=1
        else:
            out_w=0
        if out_w>=3:
            end=c-3
            break
    #print(early,end)
    for a in range(len(img)):
        for c in range(end+5,len(img[a])):
            #print(c)
            if 200>img[a][c][0]>100 and img[a][c][1]<50 and img[a][c][2]<60:
                #print(img[a][c],c)
                if c<early2:
                    early2=c
                break
    out_w=0
    for c in range(early2+5,len(img[0])):
        check_in=False
        for a in range(len(img)):
            if 200>img[a][c][0]>100 and img[a][c][1]<50 and img[a][c][2]<60:
                check_in=True
        if not check_in:
            out_w+=1
        else:
            out_w=0
        if out_w>=3:
            end2=c-3
            break
    #print(early2,end2)
    for a in range(len(img)):
        for c in range(end2+5,len(img[a])):
            #print(c)
            if 150>img[a][c][0]>90 and img[a][c][1]<40 and 20<img[a][c][2]<80:
                #print(img[a][c],c)
                if c<early3:
                    early3=c
                break
    out_w=0
    for c in range(early3+5,len(img[0])):
        check_in=False
        for a in range(len(img)):
            if 150>img[a][c][0]>90 and img[a][c][1]<40 and 20<img[a][c][2]<80:
                check_in=True
        if not check_in:
            out_w+=1
        else:
            out_w=0
        if out_w>=3:
            end3=c-3
            break
    #print(early3,end3)
    for a in range(len(img)):
        for c in range(end3+5,len(img[a])):
            #print(c)
            if 150>img[a][c][0]>50 and img[a][c][1]<40 and 20<img[a][c][2]<120:
                #print(img[a][c],c)
                if c<early4:
                    early4=c
                break
    out_w=0
    for c in range(early4+5,len(img[0])):
        check_in=False
        for a in range(len(img)):
            if 150>img[a][c][0]>50 and img[a][c][1]<40 and 20<img[a][c][2]<120:
                check_in=True
        if not check_in:
            out_w+=1
        else:
            out_w=0
        if out_w>=3:
            end4=c-3
            break
    #print(early4,end4)
    for a in range(len(img)):
        for c in range(end4+5,len(img[a])):
            #print(c)
            if 100>img[a][c][0]>=0 and img[a][c][1]<35 and 40<img[a][c][2]<150:
                #print(img[a][c],c)
                if c<early5:
                    early5=c
                break
    out_w=0
    for c in range(early5+5,len(img[0])):
        check_in=False
        for a in range(len(img)):
            if 100>img[a][c][0]>=0 and img[a][c][1]<35 and 40<img[a][c][2]<150:
                check_in=True
        if not check_in:
            out_w+=1
        else:
            out_w=0
        if out_w>=3:
            end5=c-3
            break
    #print(early5,end5)
    #exit()
    crop_img = img[0:-1, early-3:end+3]
    cv2.imwrite('.\\data_\\unlabeled\\'+str(count)+'.jpg',crop_img)
    count+=1
    crop_img = img[0:-1, early2-3:end2+3]
    cv2.imwrite('.\\data_\\unlabeled\\'+str(count)+'.jpg',crop_img)
    count+=1
    crop_img = img[0:-1, early3-3:end3+3]
    cv2.imwrite('.\\data_\\unlabeled\\'+str(count)+'.jpg',crop_img)
    count+=1
    crop_img = img[0:-1, early4-3:end4+3]
    cv2.imwrite('.\\data_\\unlabeled\\'+str(count)+'.jpg',crop_img)
    count+=1
    crop_img = img[0:-1, early5-3:end5+3]
    cv2.imwrite('.\\data_\\unlabeled\\'+str(count)+'.jpg',crop_img)
    count+=1
    print(b)
    #exit()
