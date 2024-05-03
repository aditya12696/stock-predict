import streamlit as st
from datetime import date
import yfinance as yf 
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

# Set constants
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Define the main function
def main():
    # Set page title and background color
    st.title("Stock Prediction")
    st.markdown(
        """
        <style>
        .main {
        background-color: #DCDBDB;
        }
        </style>
    """,
    unsafe_allow_html=True)

    # Create an input field for the user to enter text
    stocks = st.text_input('Stock To Predict', key='stock_input')
    
    # Create a submit button
    if st.button("Submit"):
        return stocks

# Load selected stock data and display prediction
selected_stocks = main()

if selected_stocks:
    # Check if the entered stock symbol is valid
    stock_info = yf.Ticker(selected_stocks)

    if len(stock_info.info) > 1:  # Checking if any information is fetched
        # Function to load and cache stock data
        @st.cache_data
        def load_data(ticker):
            data = yf.download(ticker, START, TODAY)
            data.reset_index(inplace=True)
            return data

        # Display loading message while data is being loaded
        data_load_state = st.text("Loading data...")
        data = load_data(selected_stocks)
        data_load_state.text("Loading data...done!")
         
        # Display raw data
        st.header('Raw Data')
        st.write(data.tail())

        # Plot raw data
        st.subheader('Time Series Data')
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Stock_Open', marker=dict(color='Green')))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock_Close', marker=dict(color='Red')))
        fig.update_layout(title_text="Time Series Data", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

        # Prepare data for forecasting
        df_train = data[['Date', 'Close']]
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
        
        # Text indicating data processing
        st.text("Model is processing the data. Please wait for the results...")

        # Instantiate Prophet model and make predictions
        m = Prophet()
        m.fit(df_train)
        future = m.make_future_dataframe(periods=365)  # Forecasting for the next year (365 days)
        forecast = m.predict(future)

        # Display forecast data
        st.subheader('Forecast Data')
        st.write(forecast.tail())

        # Plot forecast data
        st.write('Forecast Data')
        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)

        # Plot forecast components
        st.write('Forecast Components')
        fig2 = m.plot_components(forecast)
        st.write(fig2)

        # Calculate last close price and predicted price
        last_close_price = df_train.iloc[-1]['y']
        predicted_price = forecast.iloc[-1]['yhat']

        # Determine recommended action based on predicted price
        if predicted_price > last_close_price:
            action = "Buy"
        elif predicted_price < last_close_price:
            action = "Sell"
        else:
            action = "Hold"

        # Display recommended action
        st.subheader("Recommended Action")
        st.write(f"For the selected stock, the recommended action based on the forecasted price is: **{action}**")

    else:
        st.warning("Please enter a valid stock symbol.")
