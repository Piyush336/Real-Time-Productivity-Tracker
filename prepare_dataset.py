import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split_data(filepath):
    """
    Load the dataset from a CSV file and split into train and test sets.
    """
    # Load the dataset
    data = pd.read_csv("activity_dataset.csv")

    # Split into features (X) and labels (y)
    X = data['text']
    y = data['category']

    # Split into train and test sets (80-20 split)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Example usage
    X_train, X_test, y_train, y_test = load_and_split_data("activity_dataset.csv")
    print("Training Examples:", len(X_train))
    print("Testing Examples:", len(X_test))
