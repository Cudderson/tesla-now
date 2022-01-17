// import RecommendationChart from './api/RecommendationChart.js';
import { PlotlyChart } from "./PlotlyChart.js";
import LoadingChart from "./LoadingChart.js";

const Recommendations = (props) => {
  console.log("Recommendations called");
  return (
    <>
      {props.chartDataHTML ? (
        <PlotlyChart chartDataHTML={props.chartDataHTML} />
      ) : (
        <LoadingChart />
      )}
    </>
  )
}

export default Recommendations;