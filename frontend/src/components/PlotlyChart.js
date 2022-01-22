// consider passing this component as props from higher component
import InnerHTML from "dangerously-set-html-content";
import styles from './../styles/PlotlyChart.module.css';

// this component no longer needs to fetch anything, should simply return the chart
const PlotlyChart = ({ chartDataHTML }) => {
  
  return (
    <InnerHTML className={styles['chart']} html={chartDataHTML} />
  )
}

export { PlotlyChart };
