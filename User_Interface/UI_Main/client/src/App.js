import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// Components for different pages
import Navbar from './components/Navbar';
import Map from './components/Map'; 
import EVA from './components/EVA';  
import UIA from './components/UIA';
import Setup from './components/Setup';
//import Begin from './components/Begin'
import'./components/css/NavbarCSS.css';
import Egress  from './components/uia_subpages/Egress'
import Ingress  from './components/uia_subpages/Ingress'


/*
* App()
*
* Description:
*      Main driving function for React application. Currently
*      manages the routes between different pages.
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
          <Route path="/uia/egress" element={<Egress />} />
          <Route path="/uia/ingress" element={<Ingress />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
