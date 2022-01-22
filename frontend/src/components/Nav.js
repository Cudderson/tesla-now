import { Link } from "react-router-dom";
import styles from "./../styles/Nav.module.css";
import { useEffect, useState } from "react";

const Nav = () => {
  const [showDropdown, setShowDropdown] = useState(false);
  const [activeTab, setActiveTab] = useState("Go To ");

  useEffect(() => {
    // scroll to top whenever activeTab changes
    window.scrollTo(0, 0);
  }, [activeTab]);

  return (
    <nav>
      <div className={styles['nav-inner']}>
        <h3>Tesla Now</h3>
        <div className={styles["nav-links"]}>
          <button
            className={styles["dropdown-btn"]}
            onClick={() => {
              setShowDropdown(!showDropdown);
            }}
          >
            {activeTab} &#9660;
          </button>
          {/* (mobile) <ul> is positioned according to nav-links (which wraps dropdown-btn for correct effect) */}
          <ul className={showDropdown ? "" : styles["hide"]}>
            <li>
              <Link
                onClick={() => {
                  setShowDropdown(false);
                  setActiveTab("Candlestick");
                }}
                className={styles["link"]}
                to="/candlestick"
              >
                Candlestick
              </Link>
            </li>
            <li>
              <Link
                onClick={() => {
                  setShowDropdown(false);
                  setActiveTab("EPS");
                }}
                className={styles["link"]}
                to="/eps"
              >
                Earnings Per Share
              </Link>
            </li>
            <li>
              <Link
                onClick={() => {
                  setShowDropdown(false);
                  setActiveTab("SMA");
                }}
                className={styles["link"]}
                to="/sma"
              >
                Simple Moving Average
              </Link>
            </li>
            <li>
              <Link
                onClick={() => {
                  setShowDropdown(false);
                  setActiveTab("Recommendations");
                }}
                className={styles["link"]}
                to="/recommendations"
              >
                Analyst Recommendations
              </Link>
            </li>
            <li>
              <Link
                onClick={() => {
                  setShowDropdown(false);
                  setActiveTab("News");
                }}
                className={styles["link"]}
                to="/news"
              >
                News
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Nav;
