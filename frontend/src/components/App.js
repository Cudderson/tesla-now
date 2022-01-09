import testGetCurrentPrice from "./api/TestGetCurrentPrice.js";
import CandlestickChart from "./api/CandlestickChart.js";

function App() {

  // const testAPI = async () => {
  //   const url = 'http://localhost:8000/api/hello-world';
  //   try {
  //     const res = await fetch(url);
  //     const data = await res.json();
  //     console.log(data);
  //   }
  //   catch (error) {
  //     console.log(error);
  //   }
  // }
  // testAPI();


  // testGetCurrentPrice();

  // CandlestickChart();

  return (
    <div>
      <h1>Hello from react-integration branch :)</h1>
      <div><CandlestickChart /></div>
    </div>
  );
}

export default App;