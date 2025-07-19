# ✅ All imports at the top (fixes E402 and F811)
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import joblib

# ✅ Load dataset
df = pd.read_csv('data/emails.csv')
df.dropna(inplace=True)

X = df['text']
y = df['spam']

# ✅ Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Define and train pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

model.fit(X_train, y_train)

# ✅ Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# ✅ Save model
joblib.dump(model, 'model/phishing_classifier.pkl')
print("✅ Model saved to model/phishing_classifier.pkl")

