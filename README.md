# Stock Prediction App

This is a Streamlit-based web application that allows users to predict stock prices using historical data. The app utilizes the **YFinance API** to fetch stock data and **Facebook's Prophet** library for time series forecasting.

## Features

- **User Input**: Users can input a stock symbol to retrieve historical data.
- **Data Visualization**: Time series data (Open and Close prices) are displayed with interactive graphs using Plotly.
- **Stock Price Prediction**: The app uses Prophet to forecast stock prices for the next 365 days.
- **Confidence Intervals**: Predictions come with upper and lower confidence intervals.
- **Recommended Action**: Based on the forecast, the app provides a suggested action (Buy, Sell, or Hold).

## Technologies Used

- **Python**
- **Streamlit**: For building the web interface.
- **YFinance**: To fetch historical stock data.
- **Prophet**: For time series forecasting.
- **Plotly**: For interactive data visualization.

## How to Run the App Locally

1. Clone this repository:
    ```bash
    git clone https://github.com/aditya12696/stock-predict.git
    ```
   
2. Navigate into the project directory:
    ```bash
    cd stock-prediction-app
    ```

3. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. Open your browser and go to `http://localhost:8501` to interact with the app.

## Prerequisites

- **Python 3.8+**
- **Pip** for managing dependencies

## Installation

1. Clone the repository and install dependencies:
    ```bash
    git clone https://github.com/yourusername/stock-prediction-app.git
    cd stock-prediction-app
    pip install -r requirements.txt
    ```

2. Run the app using Streamlit:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Input the stock ticker symbol of the company you'd like to predict.
2. Click on **Submit** to fetch and display historical stock data.
3. View the **Raw Data** and interactive charts to understand past performance.
4. Check the **Prediction** section for the next year's forecast with confidence intervals.
5. Use the **Recommended Action** feature to decide whether to buy, sell, or hold the stock.

## Example

If you enter **AAPL** (Apple Inc.) as the stock symbol, the app will display the historical data for Apple stock and provide a forecast for the next 365 days, including a recommendation.


## Roadmap

- [ ] Add support for cryptocurrency price predictions.
- [ ] Add more advanced machine learning models for improved prediction accuracy.
- [ ] Allow users to customize forecast horizons.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the MIT License.
