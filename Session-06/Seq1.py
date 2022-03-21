class Seq:
    #a class for representing sequences

    BASES_ALLOWED = ["A", "C", "G", "T"] #atributo de clase, es una cte que le pertenece a Seq

    def are_bases_valid(self, bases):
        valid = len(bases) != 0
        i = 0
        while valid and i < len(bases):
            if bases[i] not in Seq.BASES_ALLOWED:
                valid = False
            i += 1
        return valid
    
    def __init__(self, bases):
        self.bases = bases
        print("New sequence created!")
    def __str__(self):
        return self.bases
    def len(self):
        return len(self.bases)

class Gen(Seq):
    def __init__(self, bases, name =""):
        super().__init__(bases)
        self.name = name #propiedad o atributo de objeto
        print("New gene created!")

s = Seq("AGTACACTGGT")
g = Gene("CGTAAC")
print("Testing...")

print(f"Sequence 1: {s}")
print(f"    Lenght: {s.len()}")
print(f"Sequence 2: {g}")
print(f"    Lenght: {g.len()}")