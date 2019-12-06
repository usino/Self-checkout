# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:19:41 2019

@author: USER
"""
import cv2
from darkflow.net.build import TFNet
import numpy as np
#%%
options = {
    'model': 'D:/DIGI+/fristtech/darkflow-master/cfg/tiny_20191016.cfg',
    'load': 277600,
    'threshold': 0.3,
    'gpu':1.0 }

tfnet = TFNet(options)

colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

img = cv2.imread(r'D:\DIGI+\test\test_1.jpg')
label_save = []
results = tfnet.return_predict(img) #results = 將預測的權重套用於img(圖片)
for color, result in zip(colors, results):
    tl = (result['topleft']['x'], result['topleft']['y'])  #左x/左y
    br = (result['bottomright']['x'], result['bottomright']['y']) #右x/右y
    label = result['label'] 
    confidence = result['confidence'] #可信度
    text = '{}: {:.0f}%'.format(label, confidence * 100) #可信度的呈現
    
    img = cv2.rectangle(img, tl, br, color, 5) #(影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)
    img = cv2.putText(img, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)#(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)

    label_save.append(label)#label顯示list中
print(label_save)
cv2.imshow('img', img)
cv2.waitKey(0)
#cv2.destroyAllWindows()
