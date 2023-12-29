# IP-адрес 2
def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return "Адрес — это четыре числа, разделённые точками."
    for part in parts:
        if not part.isdigit():
            return f"{part} — это не целое число."
        if int(part) < 0 or int(part) > 255:
            return f"{part} превышает 255."
    else:
        return "IP-адрес корректен."

ip = input("Введите IP-адрес: ")
print(is_valid_ip(ip))