filename = "47.txt"
search_number = "0"
count = 0

#
# with open(filename, "r") as f:
#     for line in f:
#         if " " in line:
#             continue
#         # 문자열에서 숫자 0의 개수를 세어서 더하기
#         count += line.count(search_number)
#
#
# print("숫자 {}의 개수: {}".format(search_number, count))
#
# import os
#
# foldername = "label_txt"  # txt 파일이 있는 폴더 경로
# search_number = "0"
# count = 0
#
# #
# # with open(filename, "r") as f:
# #     for line in f:
# #         if " " in line:
# #             continue
# #         # 문자열에서 숫자 0의 개수를 세어서 더하기
# #         count += line.count(search_number)
# #
# #
# # print("숫자 {}의 개수: {}".format(search_number, count))
# for filename in os.listdir(foldername):
#     if filename.endswith(".txt"):
#         with open(filename, 'r') as f:
#             # count = 0
#             for line in f:
#                 elements = line.strip().split()
#                 if len(elements) > 0 and int(elements[0]) == 0:
#                     count += 1
#
# print('첫 번째 열에서 0의 개수:', count)

# with open(filename, 'r') as f:
#     count = 0
#     for line in f:
#         elements = line.strip().split()
#         if len(elements) > 0 and int(elements[0]) == 0:
#             count += 1
#
# print('첫 번째 열에서 0의 개수:', count)

with open(filename, 'r') as f:
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for line in f:
        elements = line.strip().split()
        if len(elements) > 0:
            if int(elements[0]) == 0:
                count_0 += 1
            elif int(elements[0]) == 1:
                count_1 += 1
            elif int(elements[0]) == 2:
                count_2 += 1

print('첫 번째 열에서 0의 개수:', count_0)
print('첫 번째 열에서 1의 개수:', count_1)
print('첫 번째 열에서 2의 개수:', count_2)