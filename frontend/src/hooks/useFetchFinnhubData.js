// custom hook for fetching tesla chart/news data from finnhub

import { useEffect } from "react";
import ReactDOM from "react-dom";

const useFetchFinnhubData = (urls, setDjangoAPIData, setStaticApiData) => {
  // console.log("useFetchFinnhubData hook called!");

  useEffect(() => {
    // async defined here, because useEffect() doesn't expect a Promise to be returned
    const fetchData = async ({ isInitialFetch }) => {
      // console.log("fetchData called!");
      // console.log(`isInitialFetch?: ${isInitialFetch}`);

      // base urls for dev and prod servers
      // const DEV_BASE_URL = "http://localhost:8000/api";
      const BASE_URL = "https://tesla-now.herokuapp.com/api";
      const dyanamicData = {};
      const staticData = {};

      for (const url in urls) {
        // only GET eps_chart and recommendations on initial fetch
        if (
          isInitialFetch === true ||
          (url !== "eps_chart" && url !== "recommendations_chart")
        ) {
          try {
            // console.log("fetching " + url);
            // change dev/prod here
            const res = await fetch(BASE_URL + urls[url]);
            const data = await res.json();

            if (data.chart) {
              if (url === "eps_chart") {
                // reaching here only possible on first fetch
                staticData.eps_chart = data.chart;
              } else if (url === "recommendations_chart") {
                // reaching here only possible on first fetch
                staticData.recommendations_chart = data.chart;
              } else {
                dyanamicData[url] = data.chart;
              }
            } else if (data.news) {
              dyanamicData[url] = data.news;
            } else if (data.current_price) {
              dyanamicData[url] = data.current_price;
            }
          } catch (err) {
            console.log(err);
          }
        }
      }
      // this will batch the initial state updates together
      // only one state update is made in subsequent iterations, so this is okay
      ReactDOM.unstable_batchedUpdates(() => {
        // console.log("setting dynamic state");
        setDjangoAPIData(dyanamicData);

        if (isInitialFetch) {
          // console.log("setting static state");
          setStaticApiData(staticData);
        }
      });
    };

    // console.log("calling the initial fetchData()");
    fetchData({ isInitialFetch: true });

    // timer executes every 5 minutes
    const timer = setInterval(() => {
      // console.log("calling subsequent fetchData()");
      // something here maybe? a check?
      fetchData({ isInitialFetch: false });
    }, 300000);

    // cleanup
    return () => {
      // console.log("running cleanup function");
      clearInterval(timer);
    };
  }, [urls, setDjangoAPIData, setStaticApiData]);

  // currently, this Hook doesn't return anything, but
  // rather updates <App/>'s state via the passed updater function
};

export { useFetchFinnhubData };
