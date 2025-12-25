from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd


# Load data
data = pd.read_csv('Day_2/data.csv')
texts = data['text']
labels = data['label']

# TF-IDF vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)

# LogisticRegression fit
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy eval
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')