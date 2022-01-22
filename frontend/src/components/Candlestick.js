// This is the high-level page component that contains the candlestick chart
// import CandlestickChart from "./api/CandlestickChart.js";
import { PlotlyChart } from "./PlotlyChart.js";
import LoadingChart from "./LoadingChart.js";
import styles from "./../styles/Candlestick.module.css";

const Candlestick = (props) => {
  console.log("Candlestick called");
  console.log(props);
  if (props.chartDataHTML) {
    console.log("hello");
  }
  return (
    <>
      <h1 className={styles["price-header"]}>
        Current Share Price for Tesla (TSLA):
        {props.currentPrice ? (
          <span> ${props.currentPrice.toFixed(2)}</span>
        ) : (
          <span> Loading...</span>
        )}
      </h1>
      {/* <h1>You're visiting the Candlestick page</h1> */}
      {props.chartDataHTML ? (
        <PlotlyChart chartDataHTML={props.chartDataHTML} />
      ) : (
        <LoadingChart />
      )}
      {props.staticContent ? (
        <>
          <h2 className={styles["title"]}>{props.staticContent.title}</h2>
          <div className={styles["static-content"]}>
            <div className={styles["descriptions"]}>
              {props.staticContent.descriptions.map((description, index) => (
                <p
                  key={`${description.slice(0, 20).toString()}:${index}`}
                  className={styles["description"]}
                >
                  {description}
                </p>
              ))}
              <a className={styles["link"]} href={props.staticContent.link}>
                Learn More
              </a>
            </div>
            <p className={styles["fact"]}>
              {props.staticContent.fact} -{" "}
              <a href={props.staticContent.link}>Investopedia</a>
            </p>
          </div>
        </>
      ) : null}
    </>
  );
};

export default Candlestick;
