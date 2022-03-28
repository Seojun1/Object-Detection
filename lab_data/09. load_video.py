import cv2

path = '../data/videos/cabc30fc-e7726578.mov'
cap = cv2.VideoCapture(path)
while cap.isOpened():   # 파일이 정상적으로 열렸을 때
    ret, image = cap.read()    # ret --> 지금 내가 읽어올 frame이 있는가 없는가를 판별하는 값 (True, False 반환)
    if not ret:   # 끝장 까지 모두 봤다면
        break   # 프로그램 종료

    cv2.imshow('video', image)
    if cv2.waitKey(1) == ord('q'):  # 비디오가 켜지고 0.001초 안에 입력을 했으면 (심지어 입력키가 q라면) / q가 아닌 다른키는 안먹힘
        break   # 프로그램 종료

cap.release()   # release() --> 프로그램 닫는 함수