import { PlotlyChart } from "./PlotlyChart";
import LoadingChart from "./LoadingChart.js";
import styles from './../styles/SMA.module.css';

const SMA = (props) => {
  return (
    <>
      {props.chartDataHTML ? (
        <PlotlyChart chartDataHTML={props.chartDataHTML} />
      ) : (
        <LoadingChart />
      )}

      {props.staticContent ? (
        <div className={styles['static-content']}>
          <h2>{props.staticContent.title}</h2>  
          {props.staticContent.descriptions.map((description, index) => (
            <p key={`${description.slice(0, 20).toString()}:${index}`}>
              {description}
            </p>
          ))}

          <a className={styles['link']} href={props.staticContent.link}>Learn More</a>
        </div>
      ) : null}
    </>
  )
}

export default SMA;