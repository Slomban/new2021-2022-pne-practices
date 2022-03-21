def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1
    return d

with open("SEQUENCESS", "r") as f:
    SEQUENCESS = f.readlines()
    for seq in SEQUENCESS:
        new_seq = seq.replace("\n", "")
        print("Total lenght:", len(new_seq))
        for k, v in count_bases(new_seq).items():
            print(k + ":", v)