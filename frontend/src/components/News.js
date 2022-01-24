import styles from "./../styles/News.module.css";
import tesla_default_image from "./../tesla-logo.png";
import LoadingChart from "./LoadingChart.js";

const News = (props) => {
  return (
    <div className={styles["news-outer"]}>
      <h1 className={styles["title"]}>Tesla Now News</h1>
      <p>The latest stories, articles, and news related to Tesla Inc.</p>
      <div className={styles["news-inner"]}>
        {props.newsData
          ? props.newsData.map((news, index) => (
              <div
                key={`${news.time_posted.toString()}:${index}`}
                className={styles["news"]}
              >
                <div className={styles["image-container"]}>
                  {news.image ? (
                    <img src={news.image} alt="" />
                  ) : (
                    <img src={tesla_default_image} alt="" />
                  )}
                </div>
                <h2 className={styles["headline"]}>
                  <a href={news.url} target="_blank" rel="noreferrer">
                    {news.headline}
                  </a>
                </h2>
                <div className={styles["source"]}>
                  <span>{news.source}</span>
                  <span className={styles["time-posted"]}>
                    {news.time_posted}
                  </span>
                </div>
                <p className={styles["summary"]}>
                  {news.summary.length < 350
                    ? news.summary
                    : news.summary.slice(0, 350) + "..."}
                </p>
                <span>
                  <a
                    className={styles["link"]}
                    href={news.url}
                    target="_blank"
                    rel="noreferrer"
                  >
                    Go To Article
                  </a>
                </span>
              </div>
            ))
          : <LoadingChart />}
      </div>
    </div>
  );
};

export default News;
