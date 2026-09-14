import itertools
import numpy as np
import matplotlib.pyplot as plt


def plot_feature_importance(model):

    feature_importance = model.feature_importances_

    top_idx = np.argsort(feature_importance)[-20:][::-1]

    vocab = [
        "".join(p)
        for p in itertools.product(
            "ATCG",
            repeat=4,
        )
    ]

    bio_names = [
        "A%",
        "T%",
        "G%",
        "C%",
        "GC%",
        "AT_skew",
        "GC_skew",
        "CpG",
        "TA_dinuc",
    ]

    feature_names = vocab + bio_names

    top_names = [
        feature_names[i]
        for i in top_idx
    ]

    plt.figure(figsize=(10,5))

    plt.bar(
        range(20),
        feature_importance[top_idx],
    )

    plt.xticks(
        range(20),
        top_names,
        rotation=90,
    )

    plt.title("Top 20 Feature Importances")

    plt.tight_layout()

    plt.show()