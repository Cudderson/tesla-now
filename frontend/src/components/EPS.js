import { PlotlyChart } from "./PlotlyChart";

const EPS = (props) => {
  console.log("EPS called");

  return (
    <>
      <h1>This is the EPS page</h1>
      <PlotlyChart chartDataHTML={props.chartDataHTML} />
    </>
  )
}

export default EPS;