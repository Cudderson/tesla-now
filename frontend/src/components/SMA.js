import { PlotlyChart } from "./PlotlyChart";

const SMA = (props) => {
  console.log("SMA called");
  return (
    <>
      <h1>This is the SMA page</h1>
      <PlotlyChart chartDataHTML={props.chartDataHTML} />
    </>
  )
}

export default SMA;