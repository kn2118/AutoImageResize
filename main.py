import os 
import cv2 

path = "./assets/"
directory = "./destination0/"
filelist = os.listdir(path)
resizedImages = []

width = input("Enter Desired Width or Enter ORIGINAL: ")
height = input("Enter Desired Width or Enter ORIGINAL: ")

for i in filelist:
    img = cv2.imread(path+i, cv2.IMREAD_UNCHANGED)

    print('Compressing Image :', i)
    # resize image
    try:
        if width.upper() == "ORIGINAL" or width == '':
            width = img.shape[1]
        if height.upper() == "ORIGINAL" or height == '':
            height = img.shape[0] 
        dim = (width, height)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        resizedImages.append((resized, i))
    except:
        print("Resizing Failed!")

print("Resizing Complete!", width, 'x', height)

print("Saving Images To: ", directory)
os.chdir(directory)
for image, name in resizedImages:
    cv2.imwrite(name,image)
    

    