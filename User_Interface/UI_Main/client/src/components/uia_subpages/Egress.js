import React from 'react';
import DCU_Front from "./../images/DCU_Front.jpg";
import SUITS_UIA_PANEL from "./../images/SUITS_UIA_PANEL.jpg";
import './../css/UIASubpageCSS.css'

/*  
* Egress() - **PAGE**
*
* Description:
*      Page component where specifically egress operations will
*      be displayed 
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/
function Egress() {
  return(
    <div className="container">
    <div className="image-container">
      <img className="DCUFront_image" src={DCU_Front} alt="DCU Front" />
    </div>
  
    <div className="image-container">
      <img className="SUITS_UIA_PANEL_image" src={SUITS_UIA_PANEL} alt="Panel" />
    </div>
  </div>
    
  );
}

export default Egress;