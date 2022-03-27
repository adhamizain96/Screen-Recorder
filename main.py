#!/usr/bin/env python
# coding: utf-8

# In[1]:


#note - PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other application
#note - https://pyautogui.readthedocs.io/en/latest/
#note - pip install pyautogui
import pyautogui
#note - https://pypi.org/project/opencv-python/   
#note - pip install opencv-python
import cv2
import numpy    

#---recording parameters---
#note - cv2.VideoWriter() - https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html#ac3478f6257454209fa99249cc03a5c59
#note - cv2.VideoWriter(filename, codec, fps, resolution)
filename  = 'Screen_Recording.mp4'    
#note - codec - https://www.fourcc.org/codecs.php
codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')   
#note - resolution & fps - current gen Mackbook Air specifications
resolution = (2560, 1600)
fps = 120.0 

recording = cv2.VideoWriter(filename, codec, fps, resolution)

while True:
    #note - screenshot functions - https://pyautogui.readthedocs.io/en/latest/quickstart.html#screenshot-functions
    video_frame = numpy.array(pyautogui.screenshot())
    recording.write(video_frame)
    cv2.imshow('Screen_Recording', video_frame)
    #note - how do we stop the screen recording???
    #note - https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
    if cv2.waitKey(1) == ord('s'):
        break
    
recording.release()
cv2.destroyAllWindows()      


# In[ ]:




