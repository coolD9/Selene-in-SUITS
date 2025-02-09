import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <ul>
        <li><Link to="/map">Map</Link></li>
        <li><Link to="/eva">EVA</Link></li>
        <li><Link to="/uia">UIA</Link></li>
        <li><Link to="/setup">Setup</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
