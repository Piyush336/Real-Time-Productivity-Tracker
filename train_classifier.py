import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from prepare_dataset import load_and_split_data

# Load and split data
X_train, X_test, y_train, y_test = load_and_split_data("activity_dataset.csv")

# Convert text to numerical features
vectorizer = TfidfVectorizer(stop_words="english")
X_train_transformed = vectorizer.fit_transform(X_train)
X_test_transformed = vectorizer.transform(X_test)

# Train a classifier
model = MultinomialNB()
model.fit(X_train_transformed, y_train)

# Evaluate the model
accuracy = model.score(X_test_transformed, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model and vectorizer
joblib.dump(model, "activity_classifier_model.pkl")
joblib.dump(vectorizer, "activity_vectorizer.pkl")
print("Model and vectorizer saved.")
