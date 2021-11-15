data = open("D:\Project\MongoDB_proj\\requirements.txt", "r", encoding="UTF-8")

f = open("D:\Project\MongoDB_proj\\new.txt", "w", encoding="UTF-8")

data.readlines()

for line in data:
    label, txt = line.decode().split(" ", 1)

    f.write(txt)

f.close()
