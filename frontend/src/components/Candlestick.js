// This is the high-level page component that contains the candlestick chart
// import CandlestickChart from "./api/CandlestickChart.js";
import { PlotlyChart } from "./api/PlotlyChart.js";

const Candlestick = ({ apiURL }) => {
  console.log("Candlestick called");
  return (
    <>
      <h1>You're visiting the Candlestick page</h1>
      <PlotlyChart apiURL={apiURL} />
    </>
  )
}

export default Candlestick;