import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.combine import SMOTETomek  # Replaces SMOTE
from xgboost import XGBClassifier  # Gradient Boosting

# Load the CSV dataset
data = pd.read_csv(r"C:\Users\Alex\OneDrive\Desktop\Py_AI+ML_Proj\archive\ai4i2020.csv")

# Drop unnecessary columns
data = data.drop(columns=['UDI', 'Product ID', 'RNF', 'OSF', 'PWF', 'HDF', 'TWF', 'Machine failure'])

# Add interaction features
data['Torque_RotationalSpeed'] = data['Torque [Nm]'] * data['Rotational speed [rpm]']

# Encode the target variable ('Type')
label_encoder = LabelEncoder()
data['Type'] = label_encoder.fit_transform(data['Type'])

# Separate features (X) and target (y)
X = data.drop(columns=['Type'])
y = data['Type']

# Normalize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply SMOTETomek to balance the dataset
smotetomek = SMOTETomek(random_state=42)
X_balanced, y_balanced = smotetomek.fit_resample(X_scaled, y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_balanced, y_balanced, test_size=0.2, random_state=42)

# Train a Random Forest Classifier with adjusted hyperparameters
rf_model = RandomForestClassifier(
    n_estimators=300,      # Increased trees
    max_depth=15,          # Deeper trees
    min_samples_split=4,   # Slightly stricter split
    class_weight="balanced",  # Handle imbalance
    random_state=42
)
rf_model.fit(X_train, y_train)

# Make predictions with Random Forest
y_pred_rf = rf_model.predict(X_test)

# Evaluate Random Forest
print("\nRandom Forest Classification Report:")
print(classification_report(y_test, y_pred_rf))

print("\nRandom Forest Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_rf))

# Optional: Train an XGBoost Classifier for comparison
xgb_model = XGBClassifier(
    n_estimators=300,      # Number of boosting rounds
    max_depth=10,          # Tree depth
    learning_rate=0.05,    # Learning rate
    subsample=0.8,         # Feature sampling
    colsample_bytree=0.8,  # Feature sampling
    random_state=42
)
xgb_model.fit(X_train, y_train)

# Make predictions with XGBoost
y_pred_xgb = xgb_model.predict(X_test)

# Evaluate XGBoost
print("\nXGBoost Classification Report:")
print(classification_report(y_test, y_pred_xgb))

print("\nXGBoost Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_xgb))

# Plot feature importance for the Random Forest model
plt.figure(figsize=(10, 6))
plt.barh(data.drop(columns=['Type']).columns, rf_model.feature_importances_)
plt.xlabel("Feature Importance")
plt.title("Random Forest Feature Importance (With SMOTETomek and Tuning)")
plt.show()

# Optional: Plot feature importance for XGBoost
plt.figure(figsize=(10, 6))
plt.barh(data.drop(columns=['Type']).columns, xgb_model.feature_importances_)
plt.xlabel("Feature Importance")
plt.title("XGBoost Feature Importance")
plt.show()

# --- Add Heatmap for Feature Correlation ---
plt.figure(figsize=(12, 8))
corr_matrix = data.drop(columns=['Type']).corr()  # Correlation matrix for features
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.show()

# --- Add Heatmap for Confusion Matrix ---
# Random Forest Confusion Matrix Heatmap
rf_cm = confusion_matrix(y_test, y_pred_rf)
plt.figure(figsize=(10, 6))
sns.heatmap(rf_cm, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title("Random Forest Confusion Matrix Heatmap")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# XGBoost Confusion Matrix Heatmap
xgb_cm = confusion_matrix(y_test, y_pred_xgb)
plt.figure(figsize=(10, 6))
sns.heatmap(xgb_cm, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title("XGBoost Confusion Matrix Heatmap")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
