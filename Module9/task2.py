# Дзен Пайтона
f = open("zen.txt", "r")
lines = f.readlines()
f.close()
lines.reverse()
for line in lines:
    print(line, end="")