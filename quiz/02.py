import json
import cv2

file_name = input()
image = cv2.imread('../data/images/' + file_name)

f = open('../data/labels/labels.json')
labels = json.load(f)

for label in labels:
    if label['name'] == file_name:
        for l in label['labels']:
            if 'box2d' in l:
                cv2.rectangle(image, (int(l['box2d']['x1']), int(l['box2d']['y1'])),
                              (int(l['box2d']['x2']), int(l['box2d']['y2'])), (0, 0, 255), 3)
                # 이미지 변수, 이름, 위치(왼쪽 아래점 기준), 폰트, 폰트 크기, 컬러(B,G,R)
                cv2.putText(image, l['category'], (int(l['box2d']['x1']), int(l['box2d']['y1'])),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('image', image)
cv2.waitKey(0)
