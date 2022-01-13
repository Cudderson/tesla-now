// consider passing this component as props from higher component
import InnerHTML from "dangerously-set-html-content";

// this component no longer needs to fetch anything, should simply return the chart
const PlotlyChart = ({ chartDataHTML }) => {
  console.log("PlotlyChart called");
  
  return (
    <InnerHTML html={chartDataHTML} />
  )
}

export { PlotlyChart };
