def predict_chromosome(model, X_query, le):

    prediction = model.predict(X_query)

    chromosome = le.inverse_transform(prediction)

    return chromosome[0]