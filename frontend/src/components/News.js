const News = (props) => {
  console.log(props.newsData);

  return (
    <>
      <h1>This is the News page</h1>
      {/* let's make sure all the data was serialized properly */}
      <img src={props.newsData.images[0]} alt='missing photo' style={{width: '200px'}}></img>
      <h4>{props.newsData.times_posted[0]}</h4>
      <h4>{props.newsData.urls[0]}</h4>
      <h4>{props.newsData.sources[0]}</h4>
      <h3>{props.newsData.headlines[0]}</h3>
      <h5>{props.newsData.summaries[0]}</h5>
    </>
  )
}

export default News;