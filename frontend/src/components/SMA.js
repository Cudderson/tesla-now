import { PlotlyChart } from "./PlotlyChart";
import LoadingChart from "./LoadingChart.js";

const SMA = (props) => {
  console.log("SMA called");
  return (
    <>
      <h1>This is the SMA page</h1>
      {props.chartDataHTML ? (
        <PlotlyChart chartDataHTML={props.chartDataHTML} />
      ) : (
        <LoadingChart />
      )}
    </>
  )
}

export default SMA;