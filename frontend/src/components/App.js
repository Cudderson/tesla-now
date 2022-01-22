import { useState } from "react";

import { Routes, Route } from "react-router-dom";

// components
import Nav from "./Nav.js";
import Landing from "./Landing.js";
import Candlestick from "./Candlestick.js";
import EPS from "./EPS.js";
import SMA from "./SMA.js";
import Recommendations from "./Recommendations.js";
import News from "./News.js";
import Footer from "./Footer.js";

// static page text
import pageStaticContent from "../constants/page-content.js";

// urls for django REST api
import endpoints from "./../constants/django-endpoints.js";

// custom hook
import { useFetchFinnhubData } from "../hooks/useFetchFinnhubData.js";

// styles
import styles from "./../styles/App.module.css";

function App() {
  const [userHasLanded, setUserHasLanded] = useState(false);
  const [djangoAPIData, setDjangoAPIData] = useState({});

  // this custom hook has a useEffect() that only runs on the first render
  // i.e this hook will only update <App/>'s state once
  // On <App/> re-render, this hook is called again, but the useEffect will prevent logic from executing!
  const response = useFetchFinnhubData(endpoints.django, setDjangoAPIData);

  return (
    <>
      {userHasLanded ? <Nav /> : null}
      <div className={styles["app-container"]}>

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
                  <Candlestick
                    staticContent={pageStaticContent["candlestick"]}
                    currentPrice={djangoAPIData["current_price"]}
                    chartDataHTML={djangoAPIData["candlestick_chart"]}
                  />
                }
              />
              <Route
                path="/eps"
                element={
                  <EPS
                    staticContent={pageStaticContent["eps"]}
                    chartDataHTML={djangoAPIData["eps_chart"]}
                  />
                }
              />
              <Route
                path="/sma"
                element={
                  <SMA
                    staticContent={pageStaticContent["sma"]}
                    chartDataHTML={djangoAPIData["sma_chart"]}
                  />
                }
              />
              <Route
                path="/recommendations"
                element={
                  <Recommendations
                    staticContent={pageStaticContent["recommendations"]}
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
      {userHasLanded ? <Footer /> : null}
    </>
  );
}

export default App;
