# Количество строк
import os

def gen_lines_count(directory: str) -> int:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    count = 0
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            count += 1
                    yield count