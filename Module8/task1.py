# Challenge-2
def print_num(num):
    if num > 1:
        print_num(num - 1)
    print(num)
print_num(int(input("Введите num: ")))