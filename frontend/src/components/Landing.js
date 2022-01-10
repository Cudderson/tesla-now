import { Link } from "react-router-dom";

const LandingPage = ({setUserHasLanded}) => {

  console.log('rendered landing page');

  return (
    <>
      <h1>This is the landing page.</h1>
      {/* give user access to app and bring user to candlestick page on click */}
      <Link to='/candlestick' onClick={() => setUserHasLanded(true)}>Enter Tesla Now</Link>
    </>
  );
};

export default LandingPage;