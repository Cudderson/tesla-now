// import { useState, useEffect } from "react";
import { useFetchFinnhubData } from "../../hooks/useFetchFinnhubData.js";

// consider passing this component as props from higher component
import InnerHTML from "dangerously-set-html-content";

const PlotlyChart = ({ apiURL }) => {
  console.log('PlotlyChart called');
  // This will cause this component to rerender when this Hook's state changes
  const response = useFetchFinnhubData(apiURL);

  return (
    <>
      {response ? <InnerHTML html={response.chart} /> : <h1>loading candlestick chart...</h1>}
    </>
  );
};

export { PlotlyChart };
