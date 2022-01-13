import { PlotlyChart } from "./PlotlyChart";
import LoadingChart from "./LoadingChart.js";

const EPS = (props) => {
  console.log("EPS called");

  return (
    <>
      <h1>This is the EPS page</h1>
      {props.chartDataHTML ? (
        <PlotlyChart chartDataHTML={props.chartDataHTML} />
      ) : (
        <LoadingChart />
      )}
    </>
  )
}

export default EPS;