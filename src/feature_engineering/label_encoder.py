from sklearn.preprocessing import LabelEncoder


def encode_labels(labels):

    le = LabelEncoder()

    y = le.fit_transform(labels)

    print("Classes :", list(le.classes_))

    return y, le