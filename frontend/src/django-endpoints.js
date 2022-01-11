// defines the django REST url endpoints for retrieving data from finnhub

const endpoints = {
  charts: {
    candlestick: "http://localhost:8000/api/candlestick"
  }
}

export default endpoints;