import warnings
import random
import numpy as np

# Ignore warnings
warnings.filterwarnings("ignore")
RANDOM_STATE = 42 # Global random seed
random.seed(RANDOM_STATE)
np.random.seed(RANDOM_STATE)