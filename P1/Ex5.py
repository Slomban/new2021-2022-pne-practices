from Seq1 import Seq

print("-----| Exercise 5 |-----")
seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("Invalid sequence")
print(f"Sequence 1: (Lenght : {seq1.len()}) {seq1} \n A: {seq1.count_base()[0]}, C: {seq1.count_base()[2]}, T: {seq1.count_base()[1]}, G: {seq1.count_base()[3]}")
print(f"Sequence 2: (Lenght: {seq2.len()}) {seq2} \n A: {seq2.count_base()[0]}, C: {seq2.count_base()[2]}, T: {seq2.count_base()[1]}, G: {seq2.count_base()[3]}")
print(f"Sequence 3: (Lenght: {seq3.len()}) {seq3} \n A: {seq3.count_base()[0]}, C: {seq3.count_base()[2]}, T: {seq3.count_base()[1]}, G: {seq3.count_base()[3]}")
