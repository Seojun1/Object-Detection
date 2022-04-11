import yolov3
import cv2

model = yolov3.YOLO_V3()
model.build()
model.load()

image = cv2.imread('../data/images/b001a7ce-5cbc6e0b.jpg')
image_copy = image.copy()
result_image = model.predict(image_copy)

cv2.imshow('image', image)
cv2.imshow('result_image', result_image)
cv2.waitKey(0)
