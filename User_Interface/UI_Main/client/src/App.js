import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Map from './components/Map'; // No curly braces
import EVA from './components/EVA';  
import UIA from './components/UIA';
import Setup from './components/Setup';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Setup />} />
          <Route path="/map" element={<Map />} />
          <Route path="/eva" element={<EVA />} />
          <Route path="/uia" element={<UIA />} />
          <Route path="/setup" element={<Setup />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
