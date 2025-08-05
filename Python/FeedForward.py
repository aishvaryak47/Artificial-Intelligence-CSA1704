import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Step 1: Generate a sample dataset
X, y = make_moons(n_samples=1000, noise=0.2, random_state=0)

# Step 2: Split and scale the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 3: Build the feedforward neural network
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))   # Hidden layer 1
model.add(Dense(4, activation='relu'))                # Hidden layer 2
model.add(Dense(1, activation='sigmoid'))             # Output layer (binary)

# Step 4: Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Step 5: Train the model
model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=0)

# Step 6: Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Predict on a new sample
sample = scaler.transform([[1, 0.5]])
prediction = model.predict(sample)
print("Prediction (1=Class A, 0=Class B):", int(prediction[0][0] > 0.5))
