import os

folder_path = "label_txt"
counts = [0, 0, 0]

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "r") as file:
            for line in file:
                count = line.split()[0]
                if count == "0":
                    counts[0] += 1
                elif count == "1":
                    counts[1] += 1
                elif count == "2":
                    counts[2] += 1

print(f"Count of 0: {counts[0]}")
print(f"Count of 1: {counts[1]}")
print(f"Count of 2: {counts[2]}")