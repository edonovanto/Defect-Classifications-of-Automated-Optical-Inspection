# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 08:49:37 2019

@author: novanto
"""

import os
import cv
import cv2

PATH = "C:/Users/novanto/Downloads/AI AU Materials/FINAL PROJECT 4"
data_path = PATH + "/test_images"
data_dir_list = os.dirlist(data_path)

for i in data_dir_list:
  img1 = cv.imread(data_path + "/" + i)
  img2 = cv2.resize(img1,(224,224),interpolation=cv2.INTER.CUBIC)
  cv2.imwrite(data_path+"/"+i,img2)
  print(data_path+"/"+i)
