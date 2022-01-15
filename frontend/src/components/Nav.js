import { Link } from "react-router-dom";

const Nav = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/candlestick">Candlestick</Link>
        </li>
        <li>
          <Link to="/eps">Earnings Per Share</Link>
        </li>
        <li>
          <Link to="/sma">Simple Moving Average</Link>
        </li>
        <li>
          <Link to="/recommendations">Analyst Recommendations</Link>
        </li>
        <li>
          <Link to="/news">News</Link>
        </li>
      </ul>
    </nav>
  )
}

export default Nav;