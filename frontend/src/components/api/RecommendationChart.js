import { useState, useEffect } from "react";
import InnerHTML from "dangerously-set-html-content";

const RecommendationChart = () => {
  const [RecommendationChartData, setRecommendationChartData] = useState(null);

  useEffect(() => {
    (async () => {
      const url = "http://localhost:8000/api/recommendations";
      const res = await fetch(url);
      const data = await res.json();
      setRecommendationChartData(data);
    })();
  }, []);

  return (
    <div>
      {RecommendationChartData ? (
        <InnerHTML html={RecommendationChartData.chart} />
      ) : (
        <h1>waiting on recommendation chart...</h1>
      )}
    </div>
  );
};

export default RecommendationChart;