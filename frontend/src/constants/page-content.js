console.log("page-content imported");

const pageContent = {
  candlestick: {
    title: `What is a Candlestick Chart?`,
    descriptions: [
      `Candlestick Charts use 'OHLC' prices (open, high, low, close) to create 'candles' for a certain time interval,
    typically 1 day per candle.`,
      `Candlestick charts are a staple for investors, as they provide detailed insight to how the market is trending
    for a particular company, many companies, or the entire stock market.`,
    ],
    link: `https://en.wikipedia.org/wiki/Candlestick_chart`,
  },

  eps: {
    title: `What is EPS?`,
    descriptions: [
      `Investors use EPS as a measure a company's real value, as EPS indicates how much money a company makes
      for each share of its stock.`,
    ],
    link: `https://en.wikipedia.org/wiki/Earnings_per_share`,
  },

  sma: {
    title: `What is SMA?`,
    descriptions: [
      `SMA, or simple moving average, is a statistic used by investors to find trends in the short-term
      fluctuations of a company's stock.`,
      `I have chosen to use the 4-day and 20-day moving averages in this figure, but experts tend to use many variations
      of the SMA, (7-day, 50-day, 200-day, etc.) as well as more complicated versions, such as EMA, or Exponential
      Moving Average.`,
    ],
    link: `https://en.wikipedia.org/wiki/Moving_average`,
  },
};

export default pageContent;
