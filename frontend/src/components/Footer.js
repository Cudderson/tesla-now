import styles from './../styles/Footer.module.css';

const Footer = () => {
  return (
    <div className={styles['footer-outer']}>
      <div className={styles['footer-inner']}>
        <ul>
          <li className={styles['copyright']}>
            <span>&copy; 2021-2022</span>
            <span>Tesla Now</span>
          </li>
          <li>
            <span>Links</span>
            <span><a>Github</a> / <a>Portfolio</a></span>
          </li>
          <li>
            <span>Made By</span>
            <span>Cody Weller</span>
          </li>
        </ul>
        
      </div>
    </div>
  )
}

export default Footer;