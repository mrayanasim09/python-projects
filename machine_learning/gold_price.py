# This code is made by MRayan Asim
# Packages needed:
# pip install pandas
# pip install numpy
# pip install matplotlib
# pip install yfinance
# pip install seaborn
# pip install prophet
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
import datetime


# Download historical gold price data from Yahoo Finance
def download_gold_data(end_date):
    gold_data = yf.download("GC=F", start="2010-01-01", end=end_date, progress=False)
    return gold_data


# Preprocess the data
def preprocess_data(data):
    data = data.reset_index()
    data.rename(columns={"Date": "ds", "Adj Close": "y"}, inplace=True)
    return data[["ds", "y"]]


# Train the forecasting model using Prophet
def train_prophet_model(data):
    model = Prophet(daily_seasonality=True)
    model.fit(data)
    return model


# Make prediction using the trained model
def make_prediction(model, num_days_ahead):
    future = model.make_future_dataframe(
        periods=num_days_ahead
    )  # Predict 'num_days_ahead' days ahead
    forecast = model.predict(future)
    return forecast


# Plot the predictions
def plot_predictions(data, forecast, num_days_ahead):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=data, x="ds", y="y", label="Actual", ax=ax)
    sns.lineplot(data=forecast, x="ds", y="yhat", label="Predicted", ax=ax)
    sns.scatterplot(
        data=forecast.tail(1),
        x="ds",
        y="yhat",
        color="red",
        label=f"{num_days_ahead}-Day Ahead Prediction",
        ax=ax,
    )
    ax.set_title("Gold Price Prediction")
    ax.set_xlabel("Date")
    ax.set_ylabel("Gold Price (USD)")
    plt.legend()
    plt.show()


def main():
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    gold_data = download_gold_data(end_date)
    processed_data = preprocess_data(gold_data)

    # Train the Prophet model using historical data
    model = train_prophet_model(processed_data)

    # Get user input for the number of days ahead to predict
    num_days_ahead = int(input("Enter the number of days ahead for prediction: "))

    # Make prediction for the specified number of days ahead
    forecast = make_prediction(model, num_days_ahead)

    # Plot the predictions
    plot_predictions(processed_data, forecast, num_days_ahead)


if __name__ == "__main__":
    main()
