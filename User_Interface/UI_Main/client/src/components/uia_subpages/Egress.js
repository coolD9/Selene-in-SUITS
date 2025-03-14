import React from 'react';
import Collapsible from "./../Collapsible";
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
       <div className="text-container">
        <h2>Egress Operations</h2>
        <p>
          This section showcases the egress operations involved in our system. 
        </p>
        <Collapsible title="Section 1">Content for section 1</Collapsible>
        <Collapsible title="Section 2">Content for section 2</Collapsible>
        <Collapsible title="Section 3">Content for section 3</Collapsible>
        <Collapsible title="Section 4">Content for section 4</Collapsible>
      </div>
      <div className="image-column">
        <div className="image-container">
          <img className="DCUFront_image" src={DCU_Front} alt="DCU Front" />
        </div>

        <div className="image-container">
          <img className="SUITS_UIA_PANEL_image" src={SUITS_UIA_PANEL} alt="Panel" />
        </div>
      </div>
    </div>
    
  );
}

export default Egress;