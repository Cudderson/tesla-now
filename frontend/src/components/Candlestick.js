// This is the high-level page component that contains the candlestick chart
// import CandlestickChart from "./api/CandlestickChart.js";
import { PlotlyChart } from "./PlotlyChart.js";
import LoadingChart from "./LoadingChart.js";

const Candlestick = (props) => {
  console.log("Candlestick called");
  if (props.chartDataHTML) {
    console.log("hello");
  }
  return (
    <>
      <h1>You're visiting the Candlestick page</h1>
      {props.chartDataHTML ? (
        <PlotlyChart chartDataHTML={props.chartDataHTML} />
      ) : (
        <LoadingChart />
      )}
      <div style={{backgroundColor: 'red', height: '1000px'}}></div>
    </>
  );
};

export default Candlestick;
