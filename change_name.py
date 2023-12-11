import os

# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
# file_path = 'C:/Python_Lang/green_tomato/croll_green_img'  # 이미지 파일이 담겨있는 파일 경로 지정
# file_path = 'C:/Users/Administrator/Desktop/KPU/졸업작품/최종_이미지_상'
# file_path = 'C:/Users/Administrator/Desktop/KPU/2022 3학년 2학기/영상신호처리/주교재_예제소스(PY)/imgCrolling'
file_path = 'C:/Users/Administrator/Desktop/KPU/2022 3학년 2학기/영상신호처리/주교재_예제소스(PY)/imgCrolling/augmented_image_Medium'
file_names = os.listdir(file_path)

i = 2060
for name in file_names:
    src = os.path.join(file_path, name)
    # dst = 'ftomato' + str(i) + '.jpg'
    dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1