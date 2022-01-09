import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App.js';

// <React.StrictMode/> will cause our component to render twice (dev mode only, not prod) 

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);