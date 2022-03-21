from pathlib import Path

filename = input("File's name: ")

try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    print(f"First line of the {filename} file")
    print(lines[0])
except FileNotFoundError:
    print(f"[Error]: file '{filename}' not found ")
except IndexError:
    print(f"file '{filename}' is empty")