import os
import cv2
import numpy as np

#dataset path and output path
dataSetPath = r'E:\dataset\dataset(3rd)'
outputPath = r'C:\Users\Student\Desktop\aien16-mahjong\imagesV3'

def resize3(dataSetPath, outputPath):

    #border type :cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, cv2.BORDER_DEFAULT, cv2.BORDER_REPLICATE, cv2.BORDER_WRAP
    borderType = cv2.BORDER_DEFAULT

    #bordercolor(only use in constant type)  0,0,0 = black
    value = (0,0,0)

    #load files in dir
    fileList = os.listdir(dataSetPath)
    for fileName in fileList:
        
        #get Images
        _, ext = os.path.splitext(fileName)        
        if ext != u'.png' and ext !=  u'.jpeg' and ext != u'.jpg' and ext !=u'.JPG':
            continue
        
        #load Image
        abs_name = os.path.join(dataSetPath, fileName)
        image = cv2.imread(abs_name)  


        shape = np.shape(image)
        top = 0
        bottom = 0
        left = 0
        right = 0

        #set border size
        if shape[0] > shape[1]:
            left = (shape[0] - shape[1]) // 2
            right = (shape[0] - shape[1]) // 2
        else:
            top = (shape[1] - shape[0]) // 2
            bottom = (shape[1] - shape[0]) // 2
        
        #set border
        img = cv2.copyMakeBorder(image, top, bottom, left, right, borderType, value=value)

        #resize Image with 300,300
        img = cv2.resize(img, (300, 300)) 

        #save the new Image
        newImgPath = os.path.join(outputPath, fileName)
        cv2.imwrite(newImgPath, img) 
        

if __name__ == '__main__':
    resize3(dataSetPath, outputPath)