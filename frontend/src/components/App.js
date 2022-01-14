import { useState } from "react";

import { Routes, Route, Link } from "react-router-dom";

// top-level page components
import Landing from "./Landing.js";
import Candlestick from "./Candlestick.js";
import EPS from "./EPS.js";
import SMA from "./SMA.js";
import Recommendations from "./Recommendations.js";
import News from "./News.js";

// urls for django REST api
import endpoints from "../django-endpoints.js";

// custom hook
import { useFetchFinnhubData } from "../hooks/useFetchFinnhubData.js";

// styles
import styles from './../styles/App.module.css';

function App() {
  const [userHasLanded, setUserHasLanded] = useState(false);
  const [djangoAPIData, setDjangoAPIData] = useState({});

  console.log("App called");
  console.log("user landed? " + userHasLanded);

  // this custom hook has a useEffect() that only runs on the first render
  // i.e this hook will only update <App/>'s state once
  // On <App/> re-render, this hook is called again, but the useEffect will prevent logic from executing!
  const response = useFetchFinnhubData(endpoints.django, setDjangoAPIData);
  console.log("useFetch response: " + response);

  return (
    <div className={styles['app-container']}>
      {!userHasLanded ? (
        <div>
          <h1>on landing page, no nav</h1>
          <h1>Hello, world!</h1>
        </div>
      ) : (
        <>
          <nav>
            <h1>not on landing page, nav available</h1>
            <ul>
              <h3>nav element</h3>
              <li>
                <Link to="/candlestick">Candlestick</Link>
              </li>
              <li>
                <Link to="/eps">Earnings Per Share</Link>
              </li>
              <li>
                <Link to="/sma">Simple Moving Average</Link>
              </li>
              <li>
                <Link to="/recommendations">Analyst Recommendations</Link>
              </li>
              <li>
                <Link to="/news">News</Link>
              </li>
            </ul>
          </nav>
        </>
      )}

      {/* routes only available once user has visited the landing page (and click Enter button) */}
      {/* this is to ensure the api data is always gathered the same way (user must visit defined entrypoint) */}
      <Routes>
        {userHasLanded ? (
          <>
            <Route
              path="/"
              element={<Landing setUserHasLanded={setUserHasLanded} />}
            />
            <Route
              path="/candlestick"
              element={
                <Candlestick chartDataHTML={djangoAPIData["candlestick_chart"]} />
              }
            />
            <Route
              path="/eps"
              element={<EPS chartDataHTML={djangoAPIData["eps_chart"]} />}
            />
            <Route
              path="/sma"
              element={<SMA chartDataHTML={djangoAPIData["sma_chart"]} />}
            />
            <Route
              path="/recommendations"
              element={
                <Recommendations
                  chartDataHTML={djangoAPIData["recommendations_chart"]}
                />
              }
            />
            <Route
              path="/news"
              element={<News newsData={djangoAPIData["news"]} />}
            />
          </>
        ) : (
          <Route
            path="/*"
            element={<Landing setUserHasLanded={setUserHasLanded} />}
          />
        )}
      </Routes>
    </div>
  );
}

export default App;
