import random
import pandas as pd

def generate_samples(genome, num_samples=20000, seq_length=500):
    data = [] # List to store the generated samples
    chromosomes = list(genome.keys())
    for i in range(num_samples):

        chrom = random.choice(chromosomes) # to randomly select a chromosome from the genome
        sequence = genome[chrom]

        start = random.randint(0, len(sequence) - seq_length)
        sample_seq = sequence[start:start + seq_length]

        data.append({
            "sequence": sample_seq,
            "chromosome": chrom,
            "position": start
        })

    df = pd.DataFrame(data) # Convert the list of samples to a DataFrame using pandas

    return df