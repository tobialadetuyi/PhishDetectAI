# ✅ Place these at the very top of the file
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Now define your functions/classes below
def train_model(X_train, y_train):
    # Example training pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, 'phish_model.pkl')
    return pipeline

import pandas as pd

# Load dataset
df = pd.read_csv('data/emails.csv')

# Check for missing values
df.dropna(inplace=True)

X = df['text']
y = df['spam']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load dataset
df = pd.read_csv('data/emails.csv')

# Check for missing values
df.dropna(inplace=True)

X = df['text']
y = df['spam']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train model
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, 'model/phishing_classifier.pkl')
print("✅ Model saved to model/phishing_classifier.pkl")

