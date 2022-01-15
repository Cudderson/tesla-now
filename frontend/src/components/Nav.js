import { Link } from "react-router-dom";
import styles from "./../styles/Nav.module.css";

const Nav = () => {
  return (
    <nav>
      <h3>Tesla Now</h3>
      <ul>
        <li>
          <Link className={styles["link"]} to="/candlestick">
            Candlestick
          </Link>
        </li>
        <li>
          <Link className={styles["link"]} to="/eps">
            Earnings Per Share
          </Link>
        </li>
        <li>
          <Link className={styles["link"]} to="/sma">
            Simple Moving Average
          </Link>
        </li>
        <li>
          <Link className={styles["link"]} to="/recommendations">
            Analyst Recommendations
          </Link>
        </li>
        <li>
          <Link className={styles["link"]} to="/news">
            News
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
