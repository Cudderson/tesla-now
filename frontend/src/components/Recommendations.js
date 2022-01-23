// import RecommendationChart from './api/RecommendationChart.js';
import { PlotlyChart } from "./PlotlyChart.js";
import LoadingChart from "./LoadingChart.js";
import styles from './../styles/Recommendations.module.css';

const Recommendations = (props) => {
  
  return (
    <>
      {props.chartDataHTML ? (
        <PlotlyChart chartDataHTML={props.chartDataHTML} />
      ) : (
        <LoadingChart />
      )}
      {props.staticContent ? (
        <div className={styles['static-content']}>
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