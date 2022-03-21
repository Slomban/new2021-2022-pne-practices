from Seq1 import Seq

print("-----| Exercise 6 |-----")
seqs_list = [Seq(), Seq("ACTGA"), Seq("Invalid Secuence")]
for index, item in enumerate(seqs_list):
    print(f"Sequence {index}: (Lenght: {len(item)}) {item}")
    print(f"\tBases: {item.count()}"