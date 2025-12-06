def create_codon_dict(file_path):
    codon_dictionary = {}
    with open(file_path) as files:
        row_of_codon = files.readlines()
    for index in row_of_codon:
        slices = index.strip().split('\t')
        if len(slices) >= 3:
            codon = slices[0]
            x = slices[2]
            codon_dictionary[codon] = x
    return codon_dictionary
