from src.feature_engineering.feature_extraction import extract_features
from src.random_forest.predict import predict_chromosome
from src.random_forest.region_predictor import predict_region
from src.alignment.smith_waterman import smith_waterman_alignment


def search_query(query, model, genome, le):

    # Feature extraction
    query_features, _ = extract_features([query], k=4)

    # Predict chromosome
    predicted_chr = predict_chromosome(
        model,
        query_features,
        le,
    )

    print("Predicted Chromosome :", predicted_chr)

    # Generate candidate regions
    regions = predict_region(
        genome,
        predicted_chr,
        len(query),
    )

    best_score = -1
    best_result = None

    for start, end in regions:

        region_seq = genome[predicted_chr][start:end]

        result = smith_waterman_alignment(
            query,
            region_seq,
        )

        if result["score"] > best_score:

            best_score = result["score"]

            best_result = (
                start,
                end,
                result,
            )

    return predicted_chr, best_result