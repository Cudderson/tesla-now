function App() {

  const testAPI = async () => {
    const url = 'http://localhost:8000/api/hello-world';
    try {
      const res = await fetch(url);
      const data = await res.json();
      console.log(data);
    }
    catch (error) {
      console.log(error);
    }
  }
  // testAPI();

  const testGetCurrentPrice = async () => {
    const url = 'http://localhost:8000/api/test-current-price';
    try {
      const res = await fetch(url);
      const data = await res.json();
      console.log(data); // successfully logs the current price of tesla :)
    }
    catch (error) {
      console.log(error);
    }
  }
  testGetCurrentPrice();

  return (
    <div>
      <h1>Hello from react-integration branch :)</h1>
    </div>
  );
}

export default App;
