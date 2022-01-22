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
      {props.staticContent ? (
        // consider a global css file for static content
        <div>
          <h2>{props.staticContent.title}</h2>
          <p>
            {props.staticContent.description}
          </p>
        </div>
      ) : null}
    </>
  )
}

export default Recommendations;