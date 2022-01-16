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

      <h2>{props.staticContent.title}</h2>

      {props.staticContent.descriptions.map((description, index) => (
        <p key={`${description.slice(0, 20).toString()}:${index}`}>
          {description}
        </p>
      ))}

      <a>{props.staticContent.link}</a>
      <div style={{ backgroundColor: "red", height: "1000px" }}></div>
    </>
  )
}

export default SMA;