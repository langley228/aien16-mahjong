import os
import cv2

# replace file path with your path, idiot.
labelDictPath = r"C:\Users\Student\Desktop\aien16-mahjong\imagesV3/label.txt"

labelSrcPath = r"C:\Users\Student\Desktop\test123"
labelOutPath = r"C:\Users\Student\Desktop\aien16-mahjong\imagesV3\label"

imgSrcPath = r"C:\Users\Student\Desktop\test123"
imgOutPath = r"C:\Users\Student\Desktop\aien16-mahjong\imagesV3\img"

def getDict(srcPath) :
    # initial dictionary
    dict = {}

    with open(srcPath, 'r') as f:
        for idx, line in enumerate(f):
            dict[idx] = line.replace('\n','')

    return dict


def newImage(LabelSrcPath, ImgSrcPath, outputPath, dict) :
    files = os.listdir(LabelSrcPath)

    # direct to img folder to save image
    os.chdir(outputPath)

    for file in files:
        # verify the file we read is .txt file
        labelfileName = os.path.splitext(file)

        # if not go to next for loop
        if labelfileName[1] != r'.txt' :
            continue

        # read label file
        labFilePath = os.path.join(LabelSrcPath, file)
        
        with open(labFilePath, 'r') as f:
            # get the keyword from label file
            keyword = int(f.readline().split(' ')[0])

        # get corresponding name from dictionary
        mahjName = dict[keyword]

        # read the corresponding image
        jpgName = labelfileName[0]+r'.JPG'
        imgPath = os.path.join(ImgSrcPath, jpgName)
        #img  = cv2.imread(imgPath, cv2.IMREAD_COLOR)
        img  = cv2.imread(imgPath)

        # save the image with corresponding name
        newImgName = mahjName+'_'+labelfileName[0].split('_')[1]+r'.JPG'

        cv2.imwrite(newImgName, img)

def newLabel(srcPath, outputPath, dict) :
    files = os.listdir(srcPath)

    # direct to label folder to save label file
    os.chdir(outputPath)

    for file in files:
        # verify the file we read is .txt file
        labelfileName = os.path.splitext(file)

        # if not go to next for loop
        if labelfileName[1] != r'.txt' :
            continue

        # read label file
        labFilePath = os.path.join(srcPath, file)

        with open(labFilePath, 'r') as f:
            # get content from label file
            content = f.read()

            # get the keyword from label file
            keyword = int(content.split(' ')[0])

        # get corresponding name from dictionary, then generate new name
        mahjName = dict[keyword]
        newLabelName = mahjName+'_'+labelfileName[0].split('_')[1]+r'.txt'

        # save new label txt file
        with open(newLabelName, 'w') as f:
            f.write(content)


if __name__ == '__main__' :
    # generate dictionary
    dict = getDict(srcPath = labelDictPath)

    # generate label file with new name
    newLabel(srcPath = labelSrcPath,
            outputPath = labelOutPath,
            dict = dict)

    # generate image with new name
    newImage(LabelSrcPath = labelSrcPath, 
            ImgSrcPath = imgSrcPath, 
            outputPath = imgOutPath,
            dict = dict)