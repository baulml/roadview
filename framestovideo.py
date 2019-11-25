import cv2
import os
from os.path import isfile,join

input = 'vid_debug/frames/'
output = 'vid_debug/frames/framestovideo.mp4'

fps = 25
frame_array = []
frames = [f for f in os.listdir(input) if isfile(join(input, f))]

for i in range(len(frames)):
    filename = input + frames[i]
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    frame_array.append(img)
    print("Reading frame: {}".format(i))

out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc('M','J','P','G'), fps, size)
for i in range(len(frame_array)):
    out.write(frame_array[i])
    print("Writing frame {} to video".format(i))
out.release()