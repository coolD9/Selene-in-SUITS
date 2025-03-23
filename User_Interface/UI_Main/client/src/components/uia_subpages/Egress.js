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
        <Collapsible title="Connect UIA to DCU and Start Depress">
          <div className="checkbox-container">
            <span>UIA and DCU 1. EV1 and EV2 connect UIA and DCU umbilical</span>
            <input type="checkbox" />
          </div>

          <div className="checkbox-container">
            <span>UIA 2. EV-1, EV-2 PWR – ON</span>
            <input type="checkbox" />
          </div>

          <div className="checkbox-container">
            <span>BOTH DCU 3. BATT – UMB</span>
            <input type="checkbox" />
          </div>

          <div className="checkbox-container">
            <span>UIA 4. DEPRESS PUMP PWR – ON</span>
            <input type="checkbox" />
          </div>
        </Collapsible>


        <Collapsible title="Prep O2 Tanks">Content for section 2</Collapsible>

        <Collapsible title="Prep Water Tanks">Content for section 3</Collapsible>

        <Collapsible title="END Depress, Check Switches and Disconnect">Content for section 4</Collapsible>

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