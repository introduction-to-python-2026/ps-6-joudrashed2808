def create_codon_dict(file_path):
    codon_table = []
    with open(file_path, "r") as fobj:
        all_rows = fobj.readlines()
    for entry in all_rows:
        fields = entry.strip().split('\t')
        if len(fields) >= 3:
            key = fields[0]
            value = fields[2]
            codon_table[key] = value
    return codon_table
