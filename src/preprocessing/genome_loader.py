def genome_load(path):
    genome = {}
    curr_chr = None
    seq = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith(">"):

                if curr_chr and seq:
                    genome[curr_chr] = "".join(seq)

                seq = []

                if "chromosome" in line:
                    chr_name = line.split("chromosome")[1].split(",")[0].strip()

                    if chr_name.isdigit():
                        curr_chr = "chr" + chr_name
                        print("Loading", curr_chr)
                    else:
                        curr_chr = None

                else:
                    curr_chr = None

            else:
                if curr_chr:
                    # Remove unknown bases
                    seq.append(line.replace("N", ""))

        if curr_chr and seq:
            genome[curr_chr] = "".join(seq)

    print(f"\nLoaded {len(genome)} chromosomes successfully.")

    return genome