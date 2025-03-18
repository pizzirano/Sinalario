import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from './SignalForm.module.css';

const SignalForm = () => {
  const [dominios, setDominios] = useState([]);
  const [categorias, setCategorias] = useState([]);
  const [subcategorias, setSubcategorias] = useState([]);
  const [termoNome, setTermoNome] = useState('');
  const [termo, setTermo] = useState(''); 
  const [dominio, setDominio] = useState('');
  const [categoria, setCategoria] = useState('');
  const [subcategoria, setSubcategoria] = useState('');
  const [descricao, setDescricao] = useState('');
  const [video, setVideo] = useState(null);

  // Carregar domínios
  useEffect(() => {
    axios.get('http://localhost:8000/api/dominio/dominios/')
      .then(response => {
        if (Array.isArray(response.data)) setDominios(response.data);
      })
      .catch(error => console.error('Erro ao carregar domínios', error));
  }, []);

  // Carregar categorias
  useEffect(() => {
    axios.get('http://localhost:8000/api/categoria/categorias/')
      .then(response => {
        if (Array.isArray(response.data)) setCategorias(response.data);
      })
      .catch(error => console.error('Erro ao carregar categorias', error));
  }, []);

  // Carregar subcategorias
  useEffect(() => {
    if (categoria) {
      axios.get('http://localhost:8000/api/subcategoria/')
        .then(response => {
          if (Array.isArray(response.data)) setSubcategorias(response.data);
        })
        .catch(error => console.error('Erro ao carregar subcategorias', error));
    }
  }, [categoria]);

  // Função de envio do formulário
  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('termo', termoNome);  // Passa o nome do termo
    formData.append('descricao', descricao);  // Passa a descrição
    formData.append('dominio', dominio);  // Passa o ID do domínio
    formData.append('categoria', categoria);
    formData.append('subcategoria', subcategoria);
    formData.append('video', video);

    axios.post('http://localhost:8000/api/video/', formData)
      .then(response => console.log('Sinal cadastrado com sucesso:', response.data))
      .catch(error => {
        if (error.response) {
          console.error('Erro ao cadastrar sinal:', error.response.data);
        } else {
          console.error('Erro desconhecido:', error);
        }
      });
  };

  return (
    <form onSubmit={handleSubmit} className={styles.signalForm}>
      <div className={styles.formGroup}>
        <label htmlFor="termo">Termo</label>
        <input
          type="text"
          id="termo"
          value={termoNome}
          onChange={(e) => setTermoNome(e.target.value)}
          required
          placeholder="Digite o nome do termo"
        />
      </div>

      <div className={styles.formGroup}>
        <label htmlFor="dominio">Domínio</label>
        <select
          id="dominio"
          value={dominio}
          onChange={(e) => setDominio(e.target.value)}
          required
        >
          <option value="">Escolha um domínio</option>
          {dominios.map((dominioItem) => (
            <option key={dominioItem.id} value={dominioItem.id}>
              {dominioItem.nome}
            </option>
          ))}
        </select>
      </div>

      <div className={styles.formGroup}>
        <label htmlFor="categoria">Categoria</label>
        <select
          id="categoria"
          value={categoria}
          onChange={(e) => setCategoria(e.target.value)}
          required
        >
          <option value="">Escolha uma categoria</option>
          {categorias.map((categoriaItem) => (
            <option key={categoriaItem.id} value={categoriaItem.id}>
              {categoriaItem.nome}
            </option>
          ))}
        </select>
      </div>

      <div className={styles.formGroup}>
        <label htmlFor="subcategoria">Subcategoria</label>
        <select
          id="subcategoria"
          value={subcategoria}
          onChange={(e) => setSubcategoria(e.target.value)}
          required
        >
          <option value="">Escolha uma subcategoria</option>
          {subcategorias.map((subcategoriaItem) => (
            <option key={subcategoriaItem.id} value={subcategoriaItem.id}>
              {subcategoriaItem.nome}
            </option>
          ))}
        </select>
      </div>

      <div className={styles.formGroup}>
        <label htmlFor="descricao">Descrição</label>
        <textarea
          id="descricao"
          value={descricao}
          onChange={(e) => setDescricao(e.target.value)}
          required
        />
      </div>

      <div className={styles.formGroup}>
        <label htmlFor="video">Vídeo do Sinal</label>
        <input
          type="file"
          id="video"
          onChange={(e) => setVideo(e.target.files[0])}
          required
        />
      </div>

      <button type="submit" className={styles.submitButton}>Cadastrar Sinal</button>
    </form>
  );
};

export default SignalForm;