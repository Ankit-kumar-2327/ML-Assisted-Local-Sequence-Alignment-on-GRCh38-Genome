import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.preprocessing.genome_loader import genome_load
from src.preprocessing.dataset_generator import generate_samples

from src.feature_engineering.feature_extraction import extract_features
from src.feature_engineering.label_encoder import encode_labels

from src.random_forest.train import train_chromosome_model

from src.alignment.search_pipeline import search_query


# Load Genome
genome = genome_load(
    "C:/ML_Genome_Project/genome/GCF_000001405.26_GRCh38_genomic.fna"
)

# Generate Training Dataset
dataset = generate_samples(genome)

# Feature Extraction
X, vectorizer = extract_features(
    dataset["sequence"]
)

# Encode Labels
y, le = encode_labels(
    dataset["chromosome"]
)

# Train Random Forest
model, X_test, y_test = train_chromosome_model(
    X,
    y
)

print("\n===========================================")
print("ML-Assisted Genome Sequence Alignment")
print("===========================================\n")

query = input("Enter DNA Query Sequence : ").upper()

predicted_chr, best_result = search_query(
    query,
    model,
    genome,
    le
)

start, end, result = best_result

start_position = start + result["start_offset"]
end_position = start_position + result["alignment_length"]

print("\n=========== ALIGNMENT REPORT ===========")

print("\nPredicted Chromosome :", predicted_chr)

print(f"Genome Region : {start} - {end}")

print("\nAlignment Coordinates")

print("Start Position :", start_position)

print("End Position   :", end_position)

print("\nAlignment Statistics")

print("Alignment Score :", result["score"])

print("Alignment Length:", result["alignment_length"])

print("Matches         :", result["matches"])

print("Mismatches      :", result["mismatches"])

print("Gaps            :", result["gaps"])

print(f"Identity (%)    : {result['identity']:.2f}%")

print("\n------------- Alignment -------------\n")

print("Query  :", result["align_q"])

print("        ", result["match_line"])

print("Genome :", result["align_g"])

print("\n======================================")