import React from "react";
import styles from "./Footer.module.css";

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <p className={styles.text}>
        Desenvolvido pelos alunos do Instituto Federal Catarinense (IFC) - Balneário Camboriú / SC
      </p>
    </footer>
  );
};

export default Footer;