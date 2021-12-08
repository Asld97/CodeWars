# Exercise 4: Complementary DNA
# Return translated DNA where A is complementary with T, and C -> G

def DNA_strand(dna):
    dna_list = ''
    for letter in dna:
        if letter == "A":
            dna_list += "T"
        elif letter == "T":
            dna_list += "A"
        elif letter == "G":
            dna_list += "C"
        else:
            dna_list += "G"
    return dna_list


example_dna = 'TTTTT'
print(DNA_strand(example_dna))
