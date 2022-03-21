
class Seq:
    BASES_ALLOWED = ['A', 'C', 'T', 'G']
    BASES_COMPLEMENTS = {"A": "T", "T": "A", "G": "C", "C": "G"}
    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL sequence created")
            self.strbases = "NULL"
        elif not self.valid_sequence():
            print("INVALID Seq!")
            self.strbases = "ERROR"
        else:
            print("New sequence created!")
            self.strbases = strbases

    @staticmethod  # the function is expecting a normal argument
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence):
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases):
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        new_len = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            new_len = 0
            return new_len
        else:
            return len(self.strbases)

    def count_base(self):
        A = 0
        T = 0
        C = 0
        G = 0
        if self.strbases == "NULL" or self.strbases == "ERROR":
            pass
        else:
            for e in self.strbases:
                if e == "A":
                    A += 1
                elif e == "T":
                    T += 1
                elif e == "C":
                    C += 1
                else:
                    G += 1
        return A, T, C, G

    def count(self):
        result = {}
        for base in Seq.BASES_ALLOWED:
            result[base] = self.count_base(base)
            return result


    def reverse(self):
        reversed_seq = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            reversed_seq = self.strbases
        else:
            reversed_seq = self.strbases[::-1]
        return reversed_seq

    def complement(self):
        compl_seq = ""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            compl_seq = self.strbases
        else:
            for e in self.strbases:
                if e == "A":
                    compl_seq += "T"
                elif e == "T":
                    compl_seq += "A"
                elif e == "C":
                    compl_seq += "G"
                else:
                    compl_seq += "C"
        return compl_seq

    def read_fasta(self, filename):
        from pathlib import Path

        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for lines in body:
            self.strbases += lines

    def frequent_base(self):
        bases = ["A", "C", "G", "T"]
        count_A, count_C, count_G, count_T = self.count_base()
        counts = [count_A, count_C, count_G, count_T]
        zipped = zip(counts, bases)
        maximum = max(zipped)
        return