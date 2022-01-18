import styles from './../styles/News.module.css';
import tesla_default_image from './../tesla-logo.png';

const News = (props) => {
  console.log(props.newsData);

  return (
    <div className={styles['news-outer']}>
      {/* let's make sure all the data was serialized properly */}
      {/* <img src={props.newsData.images[0]} alt='missing photo' style={{width: '200px'}}></img>
      <h4>{props.newsData.times_posted[0]}</h4>
      <h4>{props.newsData.urls[0]}</h4>
      <h4>{props.newsData.sources[0]}</h4>
      <h3>{props.newsData.headlines[0]}</h3>
      <h5>{props.newsData.summaries[0]}</h5> */}
      <div className={styles['news-inner']}>
        {/* new method schema, don't remove above until sure all working */}
        {props.newsData ? (
          props.newsData.map((news) => (
            <div key={news.time_posted.toString()} className={styles['news']}>
              <div className={styles['image-container']}>
                {news.image ? <img src={news.image}/> : <img src={tesla_default_image} /> }
              </div>
              <h6>{news.time_posted}</h6>
              <h5>{news.source}</h5>
              <h2>{news.headline}</h2>
              <h3>{news.summary}</h3>
              <a href={news.url} target="_blank">Go To Article</a>
            </div>
          ))
        ) : null}
      </div>
    </div>
  )
}

export default News;