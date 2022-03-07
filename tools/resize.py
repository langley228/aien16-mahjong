import os
import cv2
import numpy as np

def main():
    data_dir_path = r"C:\Users\Student\Desktop\mahjong\dataset"
    file_list = os.listdir(data_dir_path)
    count = 0
    for file_name in file_list:
        root, ext = os.path.splitext(file_name)
        if ext == u'.png' or u'.jpeg' or u'.jpg':
            abs_name = data_dir_path + '/' + file_name
            image = cv2.imread(abs_name)
            #cut
            shape = np.shape(image)
            image = image[(shape[0]-shape[1])//2:shape[1]+((shape[0]-shape[1])//2), 0:shape[1]]
            #在下面寫要做的處理 在這邊是做修改圖片大小的處理
            img = cv2.resize(image, (300, 300)) #把圖片的大小改成300*300
            cv2.imwrite(abs_name, img)          
if __name__ == '__main__':
    main()