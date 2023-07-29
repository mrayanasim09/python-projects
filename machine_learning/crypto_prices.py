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


# Download historical cryptocurrency price data from Yahoo Finance
def download_crypto_data(crypto_symbol, end_date):
    crypto_data = yf.download(
        crypto_symbol, start="2010-01-01", end=end_date, progress=False
    )
    return crypto_data


# Preprocess the data
def preprocess_data(data):
    data = data.reset_index()
    data.rename(columns={"Date": "ds", "Adj Close": "y"}, inplace=True)
    return data[["ds", "y"]]


# Train the forecasting model using Prophet
def train_prophet_model(data):
    if len(data) < 2:
        raise ValueError("Dataframe has less than 2 non-NaN rows.")

    model = Prophet(daily_seasonality=True)
    model.fit(data)
    return model


# Make predictions using the trained model
def make_predictions(model, num_days_ahead):
    future = model.make_future_dataframe(periods=num_days_ahead)
    forecast = model.predict(future)
    return forecast


def plot_predictions(data, forecast, crypto_name, num_days_ahead):
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
    ax.set_title(f"{crypto_name} Price Prediction ({num_days_ahead}-Day Ahead)")
    ax.set_xlabel("Date")
    ax.set_ylabel(f"{crypto_name} Price (USD)")
    plt.legend()
    plt.show()


def main():
    crypto_symbols = [
        "BTC-USD",
        "ETH-USD",
        "LTC-USD",
        "XRP-USD",
        "ADA-USD",
        "BNB-USD",
        "DOGE-USD",
    ]
    crypto_names = [
        "Bitcoin",
        "Ethereum",
        "Litecoin",
        "Ripple",
        "Cardano",
        "Binance Coin",
        "Dogecoin",
    ]

    end_date = datetime.datetime.now().strftime("%Y-%m-%d")

    try:
        # Get user input for the number of days ahead to predict
        num_days_ahead = int(input("Enter the number of days ahead for prediction: "))

        for i in range(len(crypto_symbols)):
            crypto_symbol = crypto_symbols[i]
            crypto_name = crypto_names[i]

            crypto_data = download_crypto_data(crypto_symbol, end_date)
            processed_data = preprocess_data(crypto_data)

            # Train the Prophet model using historical data
            model = train_prophet_model(processed_data)

            # Make predictions for the specified number of days ahead
            forecast = make_predictions(model, num_days_ahead)

            # Plot the predictions
            plot_predictions(processed_data, forecast, crypto_name, num_days_ahead)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
