import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from './SignalForm.module.css';

const SignalForm = () => {
  const [dominios, setDominios] = useState([]);
  const [categorias, setCategorias] = useState([]);
  const [subcategorias, setSubcategorias] = useState([]);
  const [termo, setTermo] = useState('');
  const [dominio, setDominio] = useState('');
  const [categoria, setCategoria] = useState('');
  const [subcategoria, setSubcategoria] = useState('');
  const [descricao, setDescricao] = useState('');
  const [video, setVideo] = useState(null);

  // Requisição para carregar os domínios
  useEffect(() => {
    axios.get('http://localhost:8000/api/dominio/')
      .then(response => {
        if (Array.isArray(response.data)) {
          setDominios(response.data);  // Garantir que a resposta seja um array
        } else {
          console.error('Dados de domínios não são um array:', response.data);
        }
      })
      .catch(error => console.error('Erro ao carregar domínios', error));
  }, []);

  // Requisição para carregar as categorias
  useEffect(() => {
    axios.get('http://localhost:8000/api/categoria/')
      .then(response => {
        if (Array.isArray(response.data)) {
          setCategorias(response.data);
        } else {
          console.error('Dados de categorias não são um array:', response.data);
        }
      })
      .catch(error => console.error('Erro ao carregar categorias', error));
  }, []);

  // Requisição para carregar as subcategorias
  useEffect(() => {
    if (categoria) {
      axios.get('http://localhost:8000/api/subcategoria/?categoria=${categoria}')
        .then(response => {
          if (Array.isArray(response.data)) {
            setSubcategorias(response.data);
          } else {
            console.error('Dados de subcategorias não são um array:', response.data);
          }
        })
        .catch(error => console.error('Erro ao carregar subcategorias', error));
    }
  }, [categoria]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('termo', termo);
    formData.append('dominio', dominio);
    formData.append('categoria', categoria);
    formData.append('subcategoria', subcategoria);
    formData.append('descricao', descricao);
    formData.append('video', video);

    axios.post('http://localhost:8000/api/video/', formData)
      .then(response => {
        console.log('Sinal cadastrado com sucesso:', response.data);
      })
      .catch(error => {
        console.error('Erro ao cadastrar sinal:', error);
      });
  };

  return (
    <form onSubmit={handleSubmit} className="signal-form">
      <div className="form-group">
        <label htmlFor="termo">Termo</label>
        <input
          type="text"
          id="termo"
          value={termo}
          onChange={(e) => setTermo(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="dominio">Domínio</label>
        <select
          id="dominio"
          value={dominio}
          onChange={(e) => setDominio(e.target.value)}
          required
        >
          <option value="">Escolha um domínio</option>
          {Array.isArray(dominios) && dominios.map((dominioItem) => (
            <option key={dominioItem.id} value={dominioItem.id}>
              {dominioItem.nome}
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="categoria">Categoria</label>
        <select
          id="categoria"
          value={categoria}
          onChange={(e) => setCategoria(e.target.value)}
          required
        >
          <option value="">Escolha uma categoria</option>
          {Array.isArray(categorias) && categorias.map((categoriaItem) => (
            <option key={categoriaItem.id} value={categoriaItem.id}>
              {categoriaItem.nome}
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="subcategoria">Subcategoria</label>
        <select
          id="subcategoria"
          value={subcategoria}
          onChange={(e) => setSubcategoria(e.target.value)}
          required
        >
          <option value="">Escolha uma subcategoria</option>
          {Array.isArray(subcategorias) && subcategorias.map((subcategoriaItem) => (
            <option key={subcategoriaItem.id} value={subcategoriaItem.id}>
              {subcategoriaItem.nome}
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label htmlFor="descricao">Descrição</label>
        <textarea
          id="descricao"
          value={descricao}
          onChange={(e) => setDescricao(e.target.value)}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="video">Vídeo do Sinal</label>
        <input
          type="file"
          id="video"
          onChange={(e) => setVideo(e.target.files[0])}
          required
        />
      </div>

      <button type="submit">Cadastrar Sinal</button>
    </form>
  );
};

export default SignalForm;