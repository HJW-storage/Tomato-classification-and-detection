import os

foldername = "label_txt"  # txt 파일이 있는 폴더 경로
search_number = "0"  # 찾으려는 숫자

count = 0  # 숫자가 등장한 횟수

for i in range(0, 3):
    for filename in os.listdir(foldername):
        if filename.endswith(".txt"):
            with open(os.path.join(foldername, filename), "r") as f:
                for line in f:
                    count += line.count(search_number)
    print("숫자 {}의 개수: {}".format(search_number, count))
    count = 0  # 숫자가 등장한 횟수
    search_number = int(search_number) + 1
    search_number = str(search_number)
