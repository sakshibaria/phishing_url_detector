# phishing_detector.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
from Utils import extract_features

# Load dataset (10,000 sampled entries from earlier step)
df = pd.read_csv('phishing_site_urls.csv')  # We'll save this CSV shortly

# Encode label: 'bad' → 1 (phishing), 'good' → 0 (legit)
df['Label'] = df['Label'].map({'good': 0, 'bad': 1})

# Feature extraction
features_df = df['URL'].apply(lambda x: pd.Series(extract_features(x)))
X = features_df
y = df['Label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("\n=== Classification Report ===\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(clf, 'model.pkl')

# CLI Test
test_url = "http://paypal-account-verification.com"
test_features = pd.DataFrame([extract_features(test_url)])
pred = clf.predict(test_features)[0]
print(f"\nPrediction for '{test_url}':", "Phishing" if pred else "Legit")
