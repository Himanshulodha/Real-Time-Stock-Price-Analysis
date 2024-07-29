import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go

# Function to fetch stock data
def fetch_stock_data(ticker, period='1d', interval='1m'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data

# Function to calculate moving average
def calculate_moving_average(data, window=5):
    data['MA'] = data['Close'].rolling(window=window).mean()
    return data


# Function to create interactive plot with Plotly
def plot_stock_data(data, ticker):
    fig = go.Figure()

    # Plot closing price
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['Close'],
        mode='lines',
        name='Close Price'
    ))

    # Plot moving average
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['MA'],
        mode='lines',
        name='Moving Average'
    ))

    # Update layout
    fig.update_layout(
        title=f'{ticker} Stock Price',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=True
    )

    st.plotly_chart(fig)


def main():
    st.title('Real-Time Stock Price Analysis')
    # List of ticker symbols
    tickers = ['ACN', 'AAPL', 'MSFT', 'TSLA', 'AMZN', 'GOOGL', 'META', 'NFLX', 'NVDA', 'BRK-B']
    # Dropdown menu for ticker selection
    ticker = st.selectbox('Select Stock Ticker', tickers)
    
    period = st.selectbox('Select Period', ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
    interval = st.selectbox('Select Interval', ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1d', '5d', '1wk', '1mo', '3mo'])

    if st.button('Fetch Data'):
        data = fetch_stock_data(ticker, period, interval)
        data = calculate_moving_average(data)
        plot_stock_data(data, ticker)
        
if __name__ == "__main__":
    main()
