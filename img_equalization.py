import os
import cv2

def histogram_equalization(bgr_img):
    # convert from RGB color-space to YCrCb
    ycrcb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2YCrCb)

    # equalize the histogram of the Y channel
    ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])

    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)

    return equalized_img


input_folder = 'C:/Users/Administrator/Desktop/KPU/2022 3학년 2학기/영상신호처리/주교재_예제소스(PY)/imgCrolling/total_image'
# 이퀄리제이션 이미지를 저장할 폴더 경로
output_folder = 'C:/Users/Administrator/Desktop/KPU/2022 3학년 2학기/영상신호처리/주교재_예제소스(PY)/imgCrolling/equalization_image'

# 컬러 이미지 폴더에서 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    print("폴더가 이미 있습니다.")

i = 0
for name in image_files:
    try:
        img_color = cv2.imread(os.path.join(input_folder, name))
        cv2.imshow(name, img_color)

        img_equ = histogram_equalization(img_color)
        # cv2.imshow(name + "_equ", img_equ)

        # equ_image_path = os.path.join(output_folder, name)
        # cv2.imwrite(equ_image_path, img_equ)
        i += 1
        print(i)
        # cv2.waitKey(0)
    except Exception as e:
        print(f'{name}: {str(e)}')

# print("이퀄리제이션 이미지 저장 완료.")