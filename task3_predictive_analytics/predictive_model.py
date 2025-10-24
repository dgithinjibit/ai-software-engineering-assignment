
# task3_predictive_analytics/predictive_model.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Load dataset
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

# Create DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# For our resource allocation simulation, let's create priority levels
# based on feature values (simulating issue severity)
feature_sums = df.iloc[:, :-1].sum(axis=1)
thresholds = np.percentile(feature_sums, [33, 67])

def classify_priority(val):
    if val < thresholds[0]:
        return "Low"
    elif val < thresholds[1]:
        return "Medium"
    else:
        return "High"

# Create priority labels
y_priority = np.array([classify_priority(val) for val in feature_sums])

# Select relevant features for prediction
selected_features = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area',
    'mean smoothness', 'mean compactness', 'mean concavity'
]
X = df[selected_features]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_priority, test_size=0.2, random_state=42, stratify=y_priority
)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')

# Save metrics
metrics = {
    "accuracy": float(accuracy),
    "f1_score": float(f1),
    "classification_report": classification_report(y_test, y_pred, output_dict=True)
}

# Save results
with open('outputs/model_metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)

# Generate visualizations
plt.figure(figsize=(8, 6))
cm = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.savefig('outputs/confusion_matrix.png')
plt.close()

# Feature importance
feat_importance = pd.Series(model.feature_importances_, index=selected_features)
feat_importance.sort_values().plot(kind='barh')
plt.tight_layout()
plt.savefig('outputs/feature_importance.png')
plt.close()

print(f"Model trained successfully!")
print(f"Accuracy: {accuracy:.3f}")
print(f"F1-Score: {f1:.3f}")
