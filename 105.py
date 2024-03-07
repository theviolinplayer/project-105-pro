import os
import cv2

path = "Images"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.png', '.jpg', '.jpeg', '.gif']:
        file_name = os.path.join(path, file)
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
    img = cv2.imread(Images[i])
    out.write(img)

out.release()

print("Done")
