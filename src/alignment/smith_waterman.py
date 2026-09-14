"""
Smith-Waterman Local Sequence Alignment
"""

def smith_waterman_alignment(query, genome):

    match = 2
    mismatch = -1
    gap = -2

    m = len(query)
    n = len(genome)

    score_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    max_score = 0
    max_pos = (0, 0)

    # Fill Score Matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if query[i - 1] == genome[j - 1]:
                diag = score_matrix[i - 1][j - 1] + match
            else:
                diag = score_matrix[i - 1][j - 1] + mismatch

            up = score_matrix[i - 1][j] + gap
            left = score_matrix[i][j - 1] + gap

            score_matrix[i][j] = max(0, diag, up, left)

            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_pos = (i, j)

    # Traceback
    i, j = max_pos

    align_q = ""
    align_g = ""
    match_line = ""

    matches = 0
    mismatches = 0
    gaps = 0

    while i > 0 and j > 0 and score_matrix[i][j] != 0:

        if query[i - 1] == genome[j - 1]:

            align_q = query[i - 1] + align_q
            align_g = genome[j - 1] + align_g
            match_line = "|" + match_line

            matches += 1

            i -= 1
            j -= 1

        elif score_matrix[i][j] == score_matrix[i - 1][j] + gap:

            align_q = query[i - 1] + align_q
            align_g = "-" + align_g
            match_line = " " + match_line

            gaps += 1

            i -= 1

        else:

            align_q = "-" + align_q
            align_g = genome[j - 1] + align_g
            match_line = " " + match_line

            gaps += 1

            j -= 1

    alignment_length = len(align_q)

    identity = (
        (matches / alignment_length) * 100
        if alignment_length > 0
        else 0
    )

    return {
        "score": max_score,
        "align_q": align_q,
        "align_g": align_g,
        "match_line": match_line,
        "matches": matches,
        "mismatches": mismatches,
        "gaps": gaps,
        "alignment_length": alignment_length,
        "identity": identity,
        "start_offset": j,
    }