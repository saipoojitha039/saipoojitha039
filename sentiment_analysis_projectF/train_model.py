import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Sample data
data = {
    "text": [
        "I love this product!",
        "This is the worst experience I've ever had.",
        "It's okay, not great but not terrible.",
        "Absolutely fantastic!",
        "I hate this so much.",
        "Meh, it was fine.",
        "I am very happy with the service.",
        "Not satisfied with the product.",
        "I'm indifferent about this.",
        "Totally worth it!"
    ],
    "label": [
        "positive", "negative", "neutral", "positive", "negative",
        "neutral", "positive", "negative", "neutral", "positive"
    ]
}

df = pd.DataFrame(data)

X = df["text"]
y = df["label"]

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
