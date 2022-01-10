// This is the high-level page component that contains the candlestick chart
import CandlestickChart from "./api/CandlestickChart.js";

const Candlestick = () => {
  return (
    <>
      <h1>You're visiting the Candlestick Page</h1>
      <CandlestickChart />
    </>
  )
}

export default Candlestick;