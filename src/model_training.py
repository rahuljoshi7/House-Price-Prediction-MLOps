import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def train_model():
    np.random.seed(42)

    area = np.random.randint(500, 3000, 200)
    bedrooms = np.random.randint(1, 6, 200)

    price = 50000 + (area * 150) + (bedrooms * 10000)
    price = price + np.random.normal(0, 15000, 200)

    X = np.column_stack((area, bedrooms))

    X_train, X_test, y_train, y_test = train_test_split(
        X, price, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    return model, mae, rmse, r2


if __name__ == "__main__":
    model, mae, rmse, r2 = train_model()

    print("Linear Regression Model Results")
    print("MAE:", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R2 Score:", round(r2, 4))