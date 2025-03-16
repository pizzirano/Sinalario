import React from "react";
import styles from './Header.module.css'; // Importando o CSS Module

const Header = () => {
  return (
    <header className={styles.header}>
      <h1 className={styles.title}>Sinalário</h1>
    </header>
  );
};

export default Header;