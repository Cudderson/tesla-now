import styles from './../styles/News.module.css';
import tesla_default_image from './../tesla-logo.png';

const News = (props) => {
  console.log(props.newsData);

  return (
    <div className={styles['news-outer']}>
      <div className={styles['news-inner']}>
        {props.newsData ? (
          props.newsData.map((news) => (
            <div key={news.time_posted.toString()} className={styles['news']}>
              <div className={styles['image-container']}>
                {news.image ? <img src={news.image}/> : <img src={tesla_default_image} /> }
              </div>
              <h2 className={styles['headline']}>{news.headline}</h2>
              <h5 style={{color: 'gray', margin: 0, padding: 0}}>{news.source} {news.time_posted}</h5>
              <p className={styles['summary']}>{news.summary}</p>
              <a className={styles['link']} href={news.url} target="_blank">Go To Article</a>
            </div>
          ))
        ) : null}
      </div>
    </div>
  )
}

export default News;