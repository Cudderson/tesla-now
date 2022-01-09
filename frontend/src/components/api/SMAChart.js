import { useState, useEffect } from 'react';

// consider passing this component as props from higher component (for all)
import InnerHTML from "dangerously-set-html-content";

const SMAChart = () => {
  const [SMAChartData, setSMAChartData] = useState(null);

  useEffect(() => {
    (async () => {
      const url = 'http://localhost:8000/api/sma';
      const res = await fetch(url);
      const data = await res.json();
      setSMAChartData(data);
    })();
  }, []);

  return (
    <div>
      {SMAChartData ? <InnerHTML html={SMAChartData.chart} /> : <h1>Waiting for SMA chart...</h1>}
    </div>
  )
}

export default SMAChart;