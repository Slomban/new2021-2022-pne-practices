rom Seq1 import Seq

print("-----| Exercise 9 |-----")
FILE_LIST = ["U5", "ADA", "FRAT1", "RNU6_269P"]
for file in FILE_LIST:
    file += ".txt"
    try:
        s = Seq()
        s.read_fasta(file)
        bases_app = s.count()
        most_frequent = None
        for base, count in bases_app.items():
            if most_frequent:
                if count > most_frequent[1]:
                    most_frequent = (base, count)
            else:
                most_frequent = (base, count)
        print(f"Gene {file}: Most frequent base: {base}")