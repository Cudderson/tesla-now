// defines the django REST url endpoints for retrieving data from finnhub

const endpoints = {
  django: {
    // endpoints same for dev/prod 
    // BASE_URL (dev/prod) is controlled by hooks/useFetchFinnhubData.js
    current_price: `/current-price`,
    candlestick_chart: `/candlestick`,
    eps_chart: `/eps`,
    sma_chart: `/sma`,
    recommendations_chart: `/recommendations`,
    news: `/news`,
  }
}

export default endpoints;