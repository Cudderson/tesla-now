import { useState, useEffect } from "react";

// consider passing this component as props from higher component (for all)
import InnerHTML from "dangerously-set-html-content";

const EPSChart = () => {
  const [EPSChartData, setEPSChartData] = useState(null);

  useEffect(() => {
    // async IIFE
    (async () => {
      // consume api
      const url = "http://localhost:8000/api/eps";
      const res = await fetch(url);
      const data = await res.json();
      // save data to state
      setEPSChartData(data);
    })();
  }, []);

  return (
    <div>
      {EPSChartData ? (
        <InnerHTML html={EPSChartData.chart} />
      ) : (
        <h1>Waiting on EPS Chart</h1>
      )}
    </div>
  );
};

export default EPSChart;