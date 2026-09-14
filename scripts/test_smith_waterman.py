import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.alignment import smith_waterman_alignment

query = "ATCGATCG"

genome = "GGGATCGATCGTTT"

result = smith_waterman_alignment(query, genome)

print("Score :", result["score"])
print("Identity :", result["identity"])
print(result["align_q"])
print(result["match_line"])
print(result["align_g"])