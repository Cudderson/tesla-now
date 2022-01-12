// custom hook for fetching tesla chart/news data from finnhub

import { useState, useEffect } from "react";

const useFetchFinnhubData = (urls, setChartAPIData) => {
  // const [finnhubData, setFinnhubData] = useState(null);

  console.log('useFetch called');

  useEffect(() => {
    console.log("useFetch useEffect called");

    // async IIFE defined here, because useEffect() doesn't expect a Promise to be returned
    (async () => {
      const charts = {};
      for (const url in urls) {
        console.log(url);
        try {
          const res = await fetch(urls[url]);
          const data = await res.json();
          // charts.push(data.chart);
          charts[url] = data.chart;
        }
        catch (err) {
          console.log(err);
        }  
      }
      console.log('useFetch useEffect setting state')
      // setFinnhubData(charts);
      console.log(charts);
      setChartAPIData(charts);
    })();
  }, []);

  // currently, this Hook doesn't return anything, but
  // rather updates <App/>'s state via the passed updater function
  // [] Next: determine how this will work in the big picture
}

export { useFetchFinnhubData };