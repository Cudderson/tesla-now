import styles from "./../styles/News.module.css";
import tesla_default_image from "./../tesla-logo.png";

const News = (props) => {
  console.log(props.newsData);

  return (
    <div className={styles["news-outer"]}>
      <h1 className={styles["title"]}>Tesla Now News</h1>
      <p>The latest stories, articles, and news related to Tesla Inc.</p>
      <div className={styles["news-inner"]}>
        {props.newsData
          ? props.newsData.map((news, index) => (
              <div key={`${news.time_posted.toString()}:${index}`} className={styles["news"]}>
                <div className={styles["image-container"]}>
                  {news.image ? (
                    <img src={news.image} />
                  ) : (
                    <img src={tesla_default_image} />
                  )}
                </div>
                <h2 className={styles["headline"]}>
                  <a href={news.url} target="_blank">
                    {news.headline}
                  </a>
                </h2>
                <div className={styles["source"]}>
                  <span>{news.source}</span>
                  <span className={styles["time-posted"]}>
                    {news.time_posted}
                  </span>
                </div>
                <p className={styles["summary"]}>{news.summary}</p>
                <span>
                  <a className={styles["link"]} href={news.url} target="_blank">
                    Go To Article
                  </a>
                </span>
              </div>
            ))
          : null}
      </div>
    </div>
  );
};

export default News;
