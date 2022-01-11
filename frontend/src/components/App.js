import { useState } from "react";

import { Routes, Route, Link, Redirect } from "react-router-dom";
// hook to obtain the current url
import { useLocation } from "react-router-dom";

// import CandlestickChart from "./api/CandlestickChart.js";
// import EPSChart from "./api/EPSChart.js";
// import SMAChart from "./api/SMAChart.js";
// import RecommendationChart from "./api/RecommendationChart.js";

// top-level page components
import Landing from "./Landing.js";
import Candlestick from "./Candlestick.js";
import EPS from "./EPS.js";
import SMA from "./SMA.js";
import Recommendations from "./Recommendations.js";

function App() {
  const [userHasLanded, setUserHasLanded] = useState(false);

  console.log('App rendered');
  console.log('user landed? ' + userHasLanded);

  return (
    <>
      {!userHasLanded ? (
        <h1>on landing page, no nav</h1>
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
            </ul>
          </nav>
        </>
      )}
      
      {/* routes only available once user has visited the landing page (and click Enter button) */}
      {/* this is to ensure the api data is always gathered the same way (user must visit defined entrypoint) */}
      <Routes>
        {userHasLanded ? (
          <>
            <Route path="/" element={<Landing setUserHasLanded={setUserHasLanded} />} />
            <Route path="/candlestick" element={<Candlestick />} />
            <Route path="/eps" element={<EPS />} />
            <Route path="/sma" element={<SMA />} />
            <Route path="/recommendations" element={<Recommendations />} />
          </>
        ) : (
          <Route path="/*" element={<Landing setUserHasLanded={setUserHasLanded} />} />
        )}
      </Routes>
    </>
  );
}

export default App;
