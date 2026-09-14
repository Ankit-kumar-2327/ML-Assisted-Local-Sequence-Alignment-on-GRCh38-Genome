import sys
import os
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing.genome_loader import genome_load
from src.preprocessing.dataset_generator import generate_samples
from src.feature_engineering.feature_extraction import (
    kmer,
    extract_features,
)

genome = genome_load(
    "C:/ML_Genome_Project/genome/GCF_000001405.26_GRCh38_genomic.fna"
)

dataset = generate_samples(genome)

X, vectorizer = extract_features(dataset["sequence"])

sequence = dataset["sequence"][0]

# Visualize 3-mer frequency for a sample sequence
kmers = kmer(sequence, 3)

pd.Series(kmers).value_counts().plot(kind="bar")

plt.title("k-mer Frequency")

plt.show()

print("Total features:", len(vectorizer.vocabulary_))
print(list(vectorizer.vocabulary_.keys())[:100])