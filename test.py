import cv2
import numpy as np
for c in range(1):
    img = cv2.imread('.\\pic\\'+str(2)+'.jpg')
    img2=[[] for a in range(len(img[0]))]
    for a in range(0,len(img)):
        for b in range(len(img[a])):
            img2[b].append([0,0,0] if sum(img[a][b])<400 else [255,255,255])
    count=0
    start=0
    for a in range(len(img2[0])):
        if img2[0][a]==[0,0,0]:
            count+=1
        else:
            if count>2:
                start=a-count-1
                break
            else:
                count=0
    print(start)
    for a in range(int(len(img2)/2)):
        for b in range(start-int(a*(0.25 if a<len(img2)/4 else 0.2)),start-int(a*(0.25 if a<len(img2)/4 else 0.2))+5):
            #print(img2[a][b])
            if img2[a][b]==[255,255,255]:
                img2[a][b]=[0,0,0]
            else:
                img2[a][b]=[255,255,255]
    for c in range(len(img2)-a):
        for b in range(start-int(a*(0.25 if a<len(img2)/4 else 0.2)),start-int(a*(0.25 if a<len(img2)/4 else 0.2))+5):
            #print(img2[a][b])
            if img2[a+c][b]==[255,255,255]:
                img2[a+c][b]=[0,0,0]
            else:
                img2[a+c][b]=[255,255,255]
    print('end')
            
    cv2.imwrite('./tesetesteset.jpg',np.array(img2))
    n=0
    for b in range(len(img2)):
        count=0
        for c in range(len(img2[b])):
            #print(sum(img2[b][c]))
            if sum(img2[b][c])<40:
                count+=1
        if count>8:
            if n==0:
                print(b)
            n+=1
        else:
            if n>3:
                print(b)
                n=0
        #print('\n\n'+str(count)+' '+str(b)+'\n\n')
        #print(count)
