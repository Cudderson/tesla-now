import { PlotlyChart } from "./PlotlyChart";
import LoadingChart from "./LoadingChart.js";
import styles from "./../styles/EPS.module.css";

const EPS = (props) => {
  console.log("EPS called");

  return (
    <>
      {props.chartDataHTML ? (
        <>
          <div className={styles['padding']}></div>
          <PlotlyChart chartDataHTML={props.chartDataHTML} />
        </>
      ) : (
        <LoadingChart />
      )}
      {props.staticContent ? (
        <div className={styles["static-content"]}>
          <h2>{props.staticContent.title}</h2>

          {props.staticContent.descriptions.map((description, index) => (
            <p
              key={`${description.slice(0, 20).toString()}:${index}`}
              className={styles["description"]}
            >
              {description} - {"  "}
              <a href={props.staticContent.link}>Investopedia</a>
            </p>
          ))}
          <p>{props.staticContent.fact}</p>
          <a href={props.staticContent.link}>Learn More</a>
        </div>
      ) : null}

      <div style={{ backgroundColor: "black", height: "1000px" }}></div>
    </>
  );
};

export default EPS;
