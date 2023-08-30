from PIL import Image
from numpy import asarray
import random
import math

img = Image.open("C:\Users\Gollapalli/ Abhinav\Downloads\BW-T05.jpg")
grey_img = img.convert("L")
w, h = img.size
print(w, h)
num_arr = asarray(grey_img)
print(num_arr)


cd=[0,0]
l=[]
d={}
i=0
p=[]
check=0
f=0
while(f<20):
  while(num_arr[cd[0]!=0] and num_arr[cd[1]!=0 ]):
    cd[0]=random.randrange(0,w,1)
    cd[1]=random.randrange(0,h,1)
  l.append(cd)
  f+=1
print(l)
f=0
while(f<20):  
  i=0
  cd=l[f]
  for i in range(len(l)):
    if(i==f):
      i+=1
      continue
    slp=((l[i][1]-cd[1])/(l[i][0]-cd[0]))
    check=0
    if(abs(slp)>=1):
      if(slp>0):
          for j in range(cd[1],l[i][1]):
            pt=(j/slp)+cd[0]
            pt=math.floor(pt)
            if(num_arr[pt,cd[1]+j]!=0):
              check=5
              break
      else:
        for j in range(l[i][1],cd[1]):
            pt=(j/slp)+l[i][0]
            pt=math.floor(pt)
            if(num_arr[pt,l[i][1]+j]!=0):
              check=5
              break
    else:
      if(slp>0):
        for j in range(cd[0],l[i][0]):
            pt=(j*slp)+cd[1]
            pt=math.floor(pt)
            if(num_arr[cd[0]+j,pt]!=0):
              check=5
              break
      else:
        for j in range(l[i][0],cd[0]):
            pt=(j*slp)+l[i][1]
            pt=math.floor(pt)
            if(num_arr[cd[0]+j,pt]!=0):
              check=5
              break
    if(check!=5):
       map.append(l[i])
    i+=1
  d[cd]=map
  f+=1


print(d)
    


    

  
