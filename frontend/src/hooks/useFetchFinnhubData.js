// custom hook for fetching tesla chart/news data from finnhub

import { useState, useEffect } from "react";

const useFetchFinnhubData = (url) => {
  const [finnhubData, setFinnhubData] = useState(null);

  console.log('useFetch called');

  useEffect(() => {
    console.log("useFetch useEffect called");

    // async IIFE defined here, because useEffect() doesn't expect a Promise to be returned
    (async () => {
      try {
        const res = await fetch(url);
        const data = await res.json();
        console.log('useFetch useEffect setting state')
        setFinnhubData(data);
      }
      catch (err) {
        console.log(err);
      }      
    })();
  }, []);

  console.log("useFetch returning: " + finnhubData);
  return !finnhubData ? null : finnhubData;
}

export { useFetchFinnhubData };