import CandlestickChart from "./api/CandlestickChart.js";
import EPSChart from "./api/EPSChart.js";
import SMAChart from "./api/SMAChart.js";

function App() {

  return (
    <div>
      <h1>Hello from react-integration branch :)</h1>
      {/* <div><CandlestickChart/></div> */}
      {/* <div><EPSChart /></div> */}
      <SMAChart />
    </div>
  );
}

export default App;