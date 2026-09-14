import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("1")
from src.feature_engineering.feature_extraction import extract_features
print("✓ feature_extraction")

from src.random_forest.predict import predict_chromosome
print("✓ predict")

from src.random_forest.region_predictor import predict_region
print("✓ region_predictor")

from src.alignment.smith_waterman import smith_waterman_alignment
print("✓ smith_waterman")

from src.alignment.search_pipeline import search_query
print("✓ search_pipeline")