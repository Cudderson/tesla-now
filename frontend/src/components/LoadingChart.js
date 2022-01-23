// this component will be rendered when data is not yet available for a given chart

import { WaveSpinner } from "react-spinners-kit";
import styles from "./../styles/LoadingChart.module.css";

const LoadingChart = () => {
  return (
    <div className={styles['chart-container']}>
      <WaveSpinner size={80} color="#53d876" loading={true} />
      <h4>Gathering data...</h4>
    </div>
  );
};

export default LoadingChart;
