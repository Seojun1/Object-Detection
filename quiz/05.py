# 미완성
import tensorflow as tf
import numpy as np
import cv2

# 모델 불러오기
model = tf.keras.models.load_model('../models/classification_model.h5')

class_names = ['bike', 'bus', 'car', 'images', 'labels', 'motor', 'person', 'rider', 'traffic light', 'traffic sign', 'truck']

a = input()
b = input()
image = cv2.imread('../classification_data/' + str(a) + '/' + str(b))
cv2.imshow('image', image)
cv2.waitKey(0)

resize_image = cv2.resize(image, (224, 224))
print(resize_image.shape)

data = np.array([resize_image])
print(data.shape)

predict = model.predict(data)
print(predict)

index = np.argmax(predict) # 최댓값
print(index)

print(class_names[index])










