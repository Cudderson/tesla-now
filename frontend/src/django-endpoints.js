// defines the django REST url endpoints for retrieving data from finnhub

const endpoints = {
  django: {
    candlestick_chart: "http://localhost:8000/api/candlestick",
    eps_chart: "http://localhost:8000/api/eps",
    sma_chart: "http://localhost:8000/api/sma",
    recommendations_chart: "http://localhost:8000/api/recommendations",

    // still testing
    news: "http://localhost:8000/api/news",
  }
}

export default endpoints;