from PIL import Image,ImageOps
import os
import tensorflow as tf
import numpy as np
import time
import json
np.set_printoptions(suppress=True)
path = "training_2"
s=os.path.dirname(os.path.abspath('TrainingModel1_saved'))+"\TrainingModel1_saved"

loaded_model=tf.keras.models.load_model(s)


def translate(img):
    origin=(13,13)
    img=img.tolist()
    new_img=[[0 for j in range(28)] for i in range(28)]
    coordX=[]
    coordY=[]
    max_X,max_Y=0,0
    min_X,min_Y=27,27
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j]>30:
                max_X=max(max_X,i)
                max_Y=max(max_Y,j)
                min_X=min(min_X,i)
                min_Y=min(min_Y,j)
                coordX.append(i)
                coordY.append(j)
    avg_X=int((min_X+max_X)/2)
    avg_Y=int((min_Y+max_Y)/2)
    dist_x=origin[0]-avg_X
    dist_y=origin[1]-avg_Y
    for i in range(len(coordX)):
        new_pos_x=coordX[i]+dist_x
        new_pos_y=coordY[i]+dist_y
        if 0<=new_pos_x and new_pos_x<=27:
            if 0<=new_pos_y and new_pos_y<=27:
                new_img[new_pos_x][new_pos_y]=img[coordX[i]][coordY[i]] 


    for i in range(1,27):
        for j in range(1,27):
            
            pix=new_img[i][j]
            up=new_img[i-1][j]
            down=new_img[i+1][j]
            left=new_img[i][j-1]
            right=new_img[i][j+1]
            if max(pix,up,down,left,right)<0:
                new_img[i][j]=0
    s=np.array(new_img,dtype='uint8')
    
   
    return s
def reflect(img):

    
    return (255-img) if img[0][0]>100 else img
   
    
    
   
def predict(img):
    

    img=json.loads(img)
    img=list(img.values())
    n=len(img)

    img=Image.fromarray(np.array(img,dtype='uint8').reshape(200,int(n/(200*4)),4)).resize((28,28)).convert('L')
    
    img=translate(np.array(img))
    
   
    Image.fromarray(img).save('final.jpg')
    img=img/255
    img=img.reshape(1,28,28,1)
    
    
    results = loaded_model.predict(img)

    
               
    return "The number is " + str(np.argmax(results))




