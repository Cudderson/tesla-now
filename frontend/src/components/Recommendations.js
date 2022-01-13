// import RecommendationChart from './api/RecommendationChart.js';
import { PlotlyChart } from "./PlotlyChart.js";

const Recommendations = (props) => {
  console.log("Recommendations called");
  return (
    <>
      <h1>This is the recommendations page.</h1>
      <PlotlyChart chartDataHTML={props.chartDataHTML} />
    </>
  )
}

export default Recommendations;