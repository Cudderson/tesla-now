import CandlestickChart from "./api/CandlestickChart.js";
import EPSChart from "./api/EPSChart.js";
import RecommendationChart from "./api/RecommendationChart.js";
import SMAChart from "./api/SMAChart.js";

function App() {

  return (
    <div>
      <h1>Hello from react-integration branch :)</h1>
      {/* <div><CandlestickChart/></div> */}
      {/* <div><EPSChart /></div> */}
      {/* <SMAChart /> */}
      <RecommendationChart />
    </div>
  );
}

export default App;