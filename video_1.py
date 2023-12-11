import cv2

# 웹캠 캡쳐 객체 생성
cap = cv2.VideoCapture(0)

# 동영상 파일 저장을 위한 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    # 프레임을 읽어옴
    ret, frame = cap.read()

    if ret:
        # 프레임을 화면에 보여줌
        cv2.imshow('frame', frame)

        # 녹화를 위해 프레임 저장
        out.write(frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 객체 해제
cap.release()
out.release()

# 화면에 나타난 윈도우들을 종료
cv2.destroyAllWindows()
