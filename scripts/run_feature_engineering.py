import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing.genome_loader import genome_load
from src.preprocessing.dataset_generator import generate_samples

from src.feature_engineering.feature_extraction import extract_features
from src.feature_engineering.label_encoder import encode_labels

genome = genome_load(
    "C:/ML_Genome_Project/genome/GCF_000001405.26_GRCh38_genomic.fna"
)

dataset = generate_samples(genome)

X, vectorizer = extract_features(dataset["sequence"])

y, le = encode_labels(dataset["chromosome"])

print("\nFeature Matrix Shape :", X.shape)
print("Label Shape :", y.shape)

print("\nChromosome Classes:")
print(le.classes_)