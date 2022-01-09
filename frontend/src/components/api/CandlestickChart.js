import { useState, useEffect } from "react";

// dangerouslySetInnerHTML() will not let script tags execute in Plotly chart html string
// to solve this, I'm using npm package 'dangerously-set-html-content'
import InnerHTML from "dangerously-set-html-content";

// might rename later, during modularization
const CandlestickChart = () => {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    // async IIFE
    (async () => {
      const url = "http://localhost:8000/api/test-get-candlestick";
      const res = await fetch(url);
      const data = await res.json();
      setChartData(data);
    })();
  }, []);

  return (
    <div>
      {chartData ? (
        <InnerHTML html={chartData.chart} />
      ) : (
        <div>no chart yet</div>
      )}
    </div>
  );
};

export default CandlestickChart;
