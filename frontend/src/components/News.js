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

      {/* new method schema, don't remove above until sure all working */}
      {props.newsData ? (
        props.newsData.map((news) => (
          <div key={news.time_posted.toString()} className={styles['news']}>
            {news.image ? <img src={news.image}/> : <img src={tesla_default_image} /> }
            <h4>{news.headline}</h4>
            <h5>{news.time_posted}</h5>
            <h6>{news.summary}</h6>
          </div>
        ))
      ) : null}
    </div>
  )
}

export default News;