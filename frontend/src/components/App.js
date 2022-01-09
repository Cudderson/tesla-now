import { Routes, Route } from 'react-router-dom';

import CandlestickChart from "./api/CandlestickChart.js";
import EPSChart from "./api/EPSChart.js";
import RecommendationChart from "./api/RecommendationChart.js";
import SMAChart from "./api/SMAChart.js";

// top-level page components
import Landing from "./Landing.js";
import Candlestick from "./Candlestick.js";

function App() {

  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/candlestick" element={<Candlestick />} />
    </Routes>
  );
}

export default App;