import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";
import SignalForm from "../components/SignalForm";
import styles from './SugerirSinal.module.css'; // Corrigido

const SugerirSinal = () => {
  return (
    <main className={styles.container}>
      <Header />

      <section>
        <h2 className={styles.title}>Adicionar Sinal</h2>
        <SignalForm />
      </section>

      <Footer />
    </main>
  );
};

export default SugerirSinal;