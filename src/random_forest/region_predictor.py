def predict_region(genome, chromosome, query_length, window_size=10000):
    sequence = genome[chromosome]
    genome_length = len(sequence)

    regions = []

    for i in range(genome_length // window_size):
        start = i * window_size
        regions.append((start, start + window_size))

    return regions