from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_chromosome_model(X, y, tune=True):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    if tune:

        model = RandomForestClassifier(
            n_estimators=500,
            max_depth=None,
            min_samples_leaf=2,
            max_features="sqrt",
            class_weight="balanced",
            bootstrap=True,
            oob_score=True,
            random_state=42,
            n_jobs=-1,
        )

    else:

        model = RandomForestClassifier(
            n_estimators=1000,
            random_state=42,
            n_jobs=-1,
        )

    print("Training Random Forest...")

    model.fit(X_train, y_train)

    if hasattr(model, "oob_score_"):
        print(
            f"OOB Score : {model.oob_score_:.4f}"
        )

    return model, X_test, y_test