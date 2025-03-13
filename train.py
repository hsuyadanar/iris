import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


# Load dataset
data = pd.read_csv("data/iris.csv")

# Define features and labels
X = data.drop('variety', axis=1)
y = data['variety']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Predict the model
y_pred = model.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# Save model
joblib.dump(model, 'model/iris.pkl')


