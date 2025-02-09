import React from 'react';
import { Link } from 'react-router-dom';

/*
* Navbar() - **Navbar Component**
*
* Description:
*      A navigation bar component that will be displayed at the
*      top of every page, facilitating traversal between pages.
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/
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
