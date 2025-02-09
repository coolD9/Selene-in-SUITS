import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// Components for different pages
import Navbar from './components/Navbar';
import Map from './components/Map'; 
import EVA from './components/EVA';  
import UIA from './components/UIA';
import Setup from './components/Setup';
import'./components/css/NavbarCSS.css';

/*
* App()
*
* Description:
*      Main driving function for React application. Currently
*      holds a Navbar to be displayed on every page of the app
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/
function App() {
  return (
    <Router>
      <div className="NavbarCSS">
        {/* Navbar routes */}
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
