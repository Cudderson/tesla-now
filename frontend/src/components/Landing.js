import { Link } from "react-router-dom";

const LandingPage = () => {
  return (
    <>
      <h1>This is the landing page.</h1>
      <Link to="/candlestick">Enter Tesla Now</Link>
    </>
  );
};

export default LandingPage;
