import { Link } from "react-router-dom";
import styles from './../styles/Landing.module.css';

const LandingPage = ({setUserHasLanded}) => {

  return (
    <div className={styles['landing-outer']}>
      <div className={styles['landing-inner']}>
        <h1>Tesla Now</h1>
        <p>Real-time charts, trends, and news related to Tesla Inc.</p>
        {/* give user access to app and bring user to candlestick page on click */}
        <Link to='/candlestick' onClick={() => setUserHasLanded(true)} className={styles['link']}>Enter Tesla Now</Link>
      </div>
    </div>
  );
};

export default LandingPage;