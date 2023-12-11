import os

# 현재 디렉토리에서 .txt 파일들을 찾습니다
for filename in os.listdir(os.getcwd()):
    if filename.endswith('.txt'):
        # 파일을 읽어들입니다
        with open(filename, 'r') as f:
            lines = f.readlines()

        # 각 줄에서 숫자들을 추출합니다
        numbers = []
        for line in lines:
            nums = line.split()
            # 15를 0으로, 16을 1로, 17을 2로 바꿉니다
            nums = [0 if num == '2' else 1 if num == '0' else 2 if num == '17' else format(float(num), '.6f') for num
                    in nums]
            numbers.append(nums)

        # 수정된 리스트를 파일에 씁니다
        with open(filename, 'w') as f:
            for nums in numbers:
                f.write(' '.join(map(str, nums)) + '\n')
