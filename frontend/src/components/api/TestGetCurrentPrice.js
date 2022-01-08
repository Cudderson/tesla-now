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

export default testGetCurrentPrice;