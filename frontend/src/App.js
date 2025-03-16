import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom'; // Importando o Router, Route e Link
import './App.css';
import SugerirSinal from './screens/SugerirSinal'; // Importando o componente SugerirSinal

function App() {
  return (
    <Router>
      <div className="App">
        {/* Links de Navegação */}
        <nav>
          <ul>
            <li>
              <Link to="/sugerir-sinal">Sugerir Sinal</Link>
            </li>
            {/* Você pode adicionar mais links para outras páginas */}
          </ul>
        </nav>

        {/* Configurando as Rotas */}
        <Switch>
          <Route path="/sugerir-sinal">
            <SugerirSinal />
          </Route>
          {/* Você pode adicionar outras rotas aqui */}
          <Route path="/">
            <h1>Home Page</h1>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;