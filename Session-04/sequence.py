from pathlib import Path

filename = input("File's name: ")

try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    total = 0
    for line in body:
        total += len(line)
    print(f"Total number of basis {total}")
except FileNotFoundError:
    print(f"[Error]: file '{filename}' not found ")
except IndexError:
    print(f"file '{filename}' is empty")