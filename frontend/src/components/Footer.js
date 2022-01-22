import styles from "./../styles/Footer.module.css";

const Footer = () => {
  return (
    <div className={styles["footer-outer"]}>
      <div className={styles["footer-inner"]}>
        <ul>
          <li className={styles["copyright"]}>
            <span>&copy; 2021-2022</span>
            <span>Tesla Now</span>
          </li>
          <li>
            <span>Links</span>
            {/* both will go to github for now */}
            <span>
              <a href="https://github.com/Cudderson/tesla-now">Github</a> /{" "}
              <a href="https://github.com/Cudderson/tesla-now">Portfolio</a>
            </span>
          </li>
          <li>
            <span>Made By</span>
            <span>Cody Weller</span>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Footer;
