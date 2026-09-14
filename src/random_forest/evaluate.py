import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score,
)


def evaluate_model(model, X, y, X_test, y_test, le):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions,
    )

    print(
        f"Test Accuracy : {accuracy:.4f}"
    )

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42,
    )

    cv_scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy",
        n_jobs=-1,
    )

    print(
        f"CV Accuracy : {cv_scores.mean():.4f} ± {cv_scores.std():.4f}"
    )

    print()

    print(
        classification_report(
            y_test,
            predictions,
            target_names=le.classes_,
        )
    )

    cm = confusion_matrix(
        y_test,
        predictions,
    )

    plt.figure(figsize=(8,6))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=le.classes_,
        yticklabels=le.classes_,
    )

    plt.xlabel("Predicted")

    plt.ylabel("True")

    plt.title("Confusion Matrix")

    plt.tight_layout()

    plt.show()

    return accuracy, predictions