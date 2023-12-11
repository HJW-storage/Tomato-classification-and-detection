# pip install keras
# pip install tensorflow

from tensorflow.keras.utils import array_to_img
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.utils import load_img
from keras.preprocessing.image import ImageDataGenerator
import os

# 현재 경로
path = os.getcwd()
print(path)

num_augmet = int(input("이미지당 증식시킬 이미지 개수 입력 : "))

# 원본 이미지 경로와 증식된 이미지를 저장할 경로 설정
# 현재 폴더 위치에서 original_image 와 augmented_image 폴더를 만들어 주고 가자.
img_path = path + "/original_image_Medium"
output_dir = path + "/augmented_image_Medium"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(img_path)
print(output_dir)

# 이미지 증식
# ImageDataGenerator 내 속성이 랜덤으로 적용됌.
augGen = ImageDataGenerator(rescale=1./255,
                            rotation_range=15,  # rotation_range: 회전, 90(0-90)사이 랜덤
                            width_shift_range=0.1,  # width_shift_range : 이동, (0~1) 이미지 사이의 비율 랜덤하게 이동 , 10% 좌/우 이동
                            height_shift_range=0.1,  # height_shift_range : 상하 이동
                            shear_range=0.5,    # shear_range : 변형, (0.5)(반시계 방향 )
                            zoom_range=[0.8, 2.0],  # zoom_range : 확대,축소 0.3(0.7~1.3 사이의 크기로 랜덤하게... )
                            horizontal_flip=True,   # horizontal_flip : 수평 방향 뒤집기
                            vertical_flip=True,  # vertical_flip : 수직 방향 뒤집기
                            fill_mode='nearest'  # 이미지를 회전, 이동하거나 축소할 때 생기는 공간을 채우는 방식
                            )

# listdir(원본 사진 폴더 경로) -> 폴더 내 이미지를 한장씩 불러옴
for i in os.listdir(img_path):
    # 절대 경로 + 원본 사진 파일 경로
    img = load_img("C:/Users/Administrator/Desktop/KPU/2022 3학년 2학기/영상신호처리/주교재_예제소스(PY)/imgCrolling/original_image_Medium/"+i)
    x = img_to_array(img)  # 이미지를 array로 변경
    print(x.shape)

    x = x.reshape((1,)+x.shape)  # 이후에 사용하는 augGen.flow() 함수를 사용하기 위에 reshape을 통해 차원을 맞춰주자.
    print(x.shape)

    i = 0
    # 아래 .flow()함수는 임의 변환된 이미지를 배치 단위로 생성해서 지정된 augmented_image폴더에 저장
    # bathch size는 고정, save to dir 는 저장될 폴더 이름, save prefix는 저장될 파일 이름, save format은 파일 형식
    for batch in augGen.flow(x, batch_size=1, save_to_dir='augmented_image_Medium', save_prefix="test", save_format="jpg"):
        i += 1
        if i >= num_augmet: # 사진들이 각 맨 위에서 입력한 수 만큼씩 생성됨
            break