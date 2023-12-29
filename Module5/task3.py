# Файлы
file_name = input("Название файла: ")
for special_simbol in ['@', '№', '$', '%', '^', '&', '*', '(']:
    if file_name.startswith(special_simbol):
        print("Ошибка: название начинается недопустимым символом.")
        break
    elif file_name.endswith(".txt") or file_name.endswith(".docx"):
        print("Файл назван верно.")
        break
    else:
        print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
        break
