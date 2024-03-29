const pageContent = {
  candlestick: {
    title: `What is a Candlestick Chart?`,
    descriptions: [
      `Candlestick Charts use 'OHLC' (open, high, low, close) price data to create 'candles' that represent a given time interval,
    usually 1 trading day.`,
      `Candlestick charts are a common tool for investors, as they provide a deeper insight to how the market is trending
    for a particular company, many companies, or entire sectors.`
    ],
    fact: `" In the 1700s, a Japanese man named Homma discovered that, while there was a link between price and the supply and demand of rice,
    the markets were strongly influenced by the emotions of traders. Candlesticks show that emotion by visually representing the size of price moves with
    different colors. Traders use the candlesticks to make trading decisions based on regularly occurring patterns that help forecast the short-term direction of the price. "`, 
    link: `https://www.investopedia.com/trading/candlestick-charting-what-is-it/`,
  },

  eps: {
    title: `What is EPS?`,
    descriptions: [
      `"EPS is calculated as a company's profit divided by the outstanding shares of its common stock.
      The resulting number serves as an indicator of a company's profitability. 
      The higher a company's EPS, the more profitable it is considered to be."`
    ],
    fact: `The chart above compares analyst estimates vs actual reported EPS for the previous 4 quarters.`,
    link: `https://www.investopedia.com/terms/e/eps.asp`,
  },

  sma: {
    title: `What is SMA?`,
    descriptions: [
      `Simple Moving Averages, or SMA, are statistics used by investors to find trends in the short-term
      fluctuations of a company's stock.
      The price value at any given point on one of the lines represents the average share price for the previous (n) days.`,
      `The chart above calculates the 4-day and 20-day moving averages for Tesla, but there exists many variations
      of the SMA, (7-day, 50-day, 200-day, etc.) as well as more complicated versions, such as EMA, or Exponential
      Moving Average.`,
    ],
    link: `https://en.wikipedia.org/wiki/Moving_average`,
  },
  recommendations: {
    title: `Recommendation Trends`,
    description: `The chart above displays analyst buy/sell recommendations for the previous 4 quarters.`
  }
};

export default pageContent;
