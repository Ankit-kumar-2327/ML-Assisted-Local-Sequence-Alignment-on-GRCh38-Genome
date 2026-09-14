import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing.genome_loader import genome_load
from src.preprocessing.dataset_generator import generate_samples
from src.preprocessing.visualization import (
    plot_chromosome_lengths,
    plot_training_samples,
)

genome = genome_load(
    "C:/ML_Genome_Project/genome/GCF_000001405.26_GRCh38_genomic.fna"
)

plot_chromosome_lengths(genome)

dataset = generate_samples(genome)

plot_training_samples(dataset)