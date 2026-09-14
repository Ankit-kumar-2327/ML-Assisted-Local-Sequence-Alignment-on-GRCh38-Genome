import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing import genome_load, generate_samples
from src.feature_engineering import extract_features, encode_labels
from src.random_forest import (
    train_chromosome_model,
    evaluate_model,
    plot_feature_importance,
)

genome = genome_load(
    "C:/ML_Genome_Project/genome/GCF_000001405.26_GRCh38_genomic.fna"
)

dataset = generate_samples(genome)

X, vectorizer = extract_features(dataset["sequence"])

y, le = encode_labels(dataset["chromosome"])

model, X_test, y_test = train_chromosome_model(X, y)

accuracy, predictions = evaluate_model(
    model,
    X,
    y,
    X_test,
    y_test,
    le,
)

plot_feature_importance(model)