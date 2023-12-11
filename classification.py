import cv2
import os
import shutil

# Set the path to the directory containing the tomato photos
path = os.getcwd()
print(path)

# Create the high, medium, and low folders if they don't exist
if not os.path.exists(path+"/상"):
    os.makedirs(path+"/상")
if not os.path.exists(path+"/중"):
    os.makedirs(path+"/중")
if not os.path.exists(path+"/하"):
    os.makedirs(path+"/하")

# 자신이 분류하고자 하는 파일의 시작과 끝 설정. 본인은 tomato1.jpg ~ tomato500.jpg에 해당하는 이미지 분류를 하고자함.
start = 1
end = 500
path1 = path + '/images' # 본인은 기존 경로 path 하위 폴더에 images 폴더를 만들어 이미지를 넣어두었기에 추가로 경로지정.
print(path1)
# a = os.listdir(path1)
# print(len(a))

# Loop through each tomato photo in the directory
for file_name in sorted(os.listdir(path1)):
    # Check if the file is a tomato photo
    if file_name.endswith(".jpg") and file_name.startswith("tomato"):
        # print(file_name)

        temp = file_name.replace("tomato", "")
        temp = int(temp.replace(".jpg", ""))

        # print(temp)

        if start <= temp <= end:
            # Read the tomato photo using OpenCV
            img = cv2.imread("images"+"/"+file_name)
            # Show the tomato photo
            cv2.imshow(file_name, img)
            # Wait for the user to classify the tomato photo
            while True:
                key = cv2.waitKey(1) & 0xFF
                if key == ord('3'):
                    folder = "상"
                    break
                elif key == ord('2'):
                    folder = "중"
                    break
                elif key == ord('1'):
                    folder = "하"
                    break
            # Copy the tomato photo to the selected folder
            # shutil.move(기존 폴더 경로, 이동할 폴더 경로)
            shutil.move(path1+"/"+file_name, path+"/"+folder+"/"+file_name)
            # Destroy the window showing the tomato photo
            cv2.destroyAllWindows()
