from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split

# Load the data
Target_Labels = pd.read_csv("Shifted_price_data.csv") #Target Labels for the future price
Noise_eliminated_price = pd.read_csv("filtered_prices.csv") #Noise processed historical data


Price_data = Noise_eliminated_price['Sign'].to_numpy()

#Scale Value
Denom = .5 * 3 * (3 - 1)
#Scaling
for i in range(2999):
    Price_data[i] = Price_data[i] / Denom

labels = Target_Labels['Sign']
labels_temp = np.where(labels == -1, 0, labels)
# Convert data to NumPy arrays
Price_data_numpy = np.array(Price_data)
labels_numpy = np.array(labels_temp)

#Normalization of price data
mean = np.mean(Price_data_numpy)
std = np.std(Price_data_numpy)
Price_data_normalized = (Price_data_numpy - mean) / std


# Reshape input data for XGBoost
Price_data_reshaped = Price_data.reshape(-1, 1)  # Reshape to (num_samples, num_features)


# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(Price_data_reshaped, labels_numpy, test_size=0.1, random_state=42)
#Training the model
model = xgb.XGBClassifier()
model.fit(X_train,y_train)
# Evaluate the model
predictions = model.predict(X_test)
predicted_labels = np.round(predictions)

accuracy = accuracy_score(y_test, predicted_labels)


accuracy = accuracy_score(y_test, predicted_labels)
precision = precision_score(y_test, predicted_labels)
recall = recall_score(y_test, predicted_labels)
f1 = f1_score(y_test, predicted_labels)
roc_auc = roc_auc_score(y_test, predictions)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("ROC AUC Score:", roc_auc)