function App() {

  const testAPI = async () => {
    const url = 'http://localhost:8000/api/hello-world';
    try {
      const res = await fetch(url);
      const data = await res.json();
      console.log(data);
    }
    catch (error) {
      // console.warn(xhr.responseText)
      console.log(error);
    }
  }
  testAPI();

  return (
    <div>
      <h1>Hello from react-integration branch :)</h1>
    </div>
  );
}

export default App;
