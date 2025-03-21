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
    <div className="DCUFront_image">
     <img src={DCU_Front} alt='DCU'>     
     </img>

     <img src={SUITS_UIA_PANEL} alt='PANEL'>
     </img>

    </div>
  )
}

export default Egress;