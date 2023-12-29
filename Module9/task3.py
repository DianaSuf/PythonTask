# Файлы и папки
import os

def calculate_directory_stats(directory_path):
    total_size_bytes = 0
    total_files = 0
    total_subdirectories = 0

    for dirpath, dirnames, filenames in os.walk(directory_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size_bytes += os.path.getsize(fp)
            total_files += 1
            total_subdirectories += len(dirnames)
    total_size_kb = total_size_bytes / 1024
    return total_size_kb, total_files, total_subdirectories

directory_path = input("Введите путь до каталога: ")

size_kb, files, subdirs = calculate_directory_stats(directory_path)

print(f"Размер каталога (в Кбайтах): {size_kb}")
print(f"Количество файлов: {files}")
print(f"Количество подкаталогов: {subdirs}")