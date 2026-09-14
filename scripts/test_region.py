import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.random_forest.region_predictor import predict_region

print("Import Successful")