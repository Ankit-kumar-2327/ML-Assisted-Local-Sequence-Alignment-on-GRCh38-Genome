import itertools
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import hstack, csr_matrix

def kmer(sequence, k = 4):
    return [sequence[i : i + k] for i in range(len(sequence) - k + 1)]

def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / max(len(seq), 1)

def extract_features(sequences, k = 4):
    vocab = [
        "".join(p)
        for p in itertools.product("ATCG", repeat = k) # as k = 4 ATCG * ATCG * ATCG * ATCG = 4^4 = 256 possible combinations
    ]

    vectorizer = CountVectorizer(
        analyzer = lambda x: kmer(x, k),
        vocabulary = vocab,
        lowercase = False
    )

    X_kmer = vectorizer.fit_transform(sequences).astype(float)

    row_sums = np.array(X_kmer.sum(axis = 1)).flatten()
    row_sums[row_sums == 0] = 1

    X_kmer = X_kmer.multiply(
        1.0 / row_sums[:, np.newaxis]
    )

    bio_feats = []

    for seq in sequences:

        n = len(seq)

        a = seq.count("A") / n
        t = seq.count("T") / n
        g = seq.count("G") / n
        c = seq.count("C") / n

        gc = g + c

        at_skew = (a - t) / (a + t + 1e-9)
        gc_skew = (g - c) / (g + c + 1e-9)

        cpg = seq.count("CG") / max(n - 1, 1)
        ta_dinuc = seq.count("TA") / max(n - 1, 1)

        bio_feats.append([
            a,
            t,
            g,
            c,
            gc,
            at_skew,
            gc_skew,
            cpg,
            ta_dinuc
        ])

    X_bio = csr_matrix(np.array(bio_feats))

    X = hstack([X_kmer, X_bio])

    print(
        f"Feature Matrix : {X.shape[0]} samples × {X.shape[1]} features"
    )

    return X, vectorizer