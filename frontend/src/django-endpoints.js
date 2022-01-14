// defines the django REST url endpoints for retrieving data from finnhub

const endpoints = {
  charts: {
    candlestick: "http://localhost:8000/api/candlestick",
    eps: "http://localhost:8000/api/eps",
    sma: "http://localhost:8000/api/sma",
    recommendations: "http://localhost:8000/api/recommendations",

    // still testing
    news: "http://localhost:8000/api/news",
  }
}

export default endpoints;