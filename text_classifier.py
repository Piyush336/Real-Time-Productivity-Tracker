import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    """Train the activity classifier."""
    # Sample dataset (replace with a real dataset)
    data = pd.DataFrame({
        "Application": [
            "Watching YouTube tutorial", "Scrolling Instagram feed",
            "Coding in Visual Studio", "Browsing Netflix",
            "Reading Research Paper", "Gaming on Steam"
        ],
        "Category": ["Productive", "Unproductive", "Productive", "Unproductive", "Productive", "Unproductive"]
    })

    X = data["Application"]
    y = data["Category"]

    vectorizer = CountVectorizer()
    X_transformed = vectorizer.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    
    # Save the model and vectorizer
    joblib.dump(model, "activity_classifier_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

# Call train_model() to generate the model
train_model()
