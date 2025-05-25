import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression

def train_test():
    X_train = pd.read_csv('tema/X_train.csv')
    y_train = pd.read_csv('tema/y_train.csv')
    X_test = pd.read_csv('tema/X_test.csv')
    y_test = pd.read_csv('tema/y_test.csv')
    model = LinearRegression()
    model.fit(X_train, y_train)  
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae:.2f}")

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
    plt.title('Actual vs Predicted')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.grid()
    plt.show()

train_test()