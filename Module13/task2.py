# Пути файлов
import os

def gen_files_path(root_dir: str, target_dir: str) -> list[str]:
    paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        if dirpath.endswith(target_dir):
            for filename in filenames:
                paths.append(os.path.join(dirpath, filename))
    return paths