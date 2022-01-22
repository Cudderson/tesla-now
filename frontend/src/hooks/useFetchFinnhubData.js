// custom hook for fetching tesla chart/news data from finnhub

import { useEffect } from "react";

const useFetchFinnhubData = (urls, setDjangoAPIData) => {

  console.log('useFetch called');

  useEffect(() => {
    console.log("useFetch useEffect called");

    // async IIFE defined here, because useEffect() doesn't expect a Promise to be returned
    (async () => {
      // base urls for dev and prod servers
      const DEV_BASE_URL = "http://localhost:8000/api";
      const BASE_URL = "https://tesla-now.herokuapp.com/api";
      const allData = {};

      for (const url in urls) {
        try {
          // change dev/prod here
          const res = await fetch(BASE_URL + urls[url]);
          const data = await res.json();

          console.log(url);

          // handle charts and news
          if (data.chart) {
            allData[url] = data.chart;
          }
          else if (data.news) {
            allData[url] = data.news;
          }
          else if (data.current_price) {
            allData[url] = data.current_price;
          }
        }
        catch (err) {
          console.log(err);
        }  
      }
      console.log('useFetch useEffect setting state');
      setDjangoAPIData(allData);
    })();
  }, []);

  // currently, this Hook doesn't return anything, but
  // rather updates <App/>'s state via the passed updater function
}

export { useFetchFinnhubData };