import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import MapRequest from './components/MapRequest';
import MechanicsList from './components/MechanicsList';
import Dashboard from './components/Dashboard';

function App(){
  return (
    <BrowserRouter>
      <nav style={{padding:10}}>
        <Link to="/">Map</Link> | <Link to="/mechanics">Mechanics</Link> | <Link to="/dashboard">Dashboard</Link> | <Link to="/login">Login</Link> | <Link to="/register">Register</Link>
      </nav>
      <Routes>
        <Route path="/" element={<MapRequest/>} />
        <Route path="/mechanics" element={<MechanicsList/>} />
        <Route path="/dashboard" element={<Dashboard/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/register" element={<Register/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
