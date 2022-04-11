import yolov3
import cv2
import os

model = yolov3.YOLO_V3()
model.build()
model.load()

video_file_name = 'cabc30fc-e7726578.mov'
path = '../data/videos/'
cap = cv2.VideoCapture(path + video_file_name) # cv2.VideoCapture(0) --> 웹캠 사용

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc('m', 'o', '4', 'v')   # 비디오를 저장하는 인코딩 방식

if not os.path.exists('../outputs'):
    os.mkdir('../outputs')

out = cv2.VideoWriter('../outputs/' + video_file_name, fourcc, (fps//2), (width, height))

while cap.isOpened():   # 파일이 정상적으로 열렸을 때
    ret, image = cap.read()    # ret --> 지금 내가 읽어올 frame이 있는가 없는가를 판별하는 값 (True, False 반환)
    if not ret:   # 끝장 까지 모두 봤다면
        break   # 프로그램 종료x

    result = model.predict(image)
    cv2.imshow('video', result)
    out.write(result)
    if cv2.waitKey(1) == ord('q'):  # 비디오가 켜지고 0.001초 안에 입력을 했으면 (심지어 입력키가 q라면) / q가 아닌 다른키는 안먹힘
        break   # 프로그램 종료

cap.release()   # release() --> 프로그램 닫는 함수
out.release()