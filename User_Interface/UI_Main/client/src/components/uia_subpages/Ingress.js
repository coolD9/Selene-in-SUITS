import React from 'react';
import DCU_Front from './../images/DCU_Front.jpg'
import UIA_Panel from './../images/SUITS_UIA_PANEL.jpg'
import './../css/MasterCSS.css'
import './../css/UIACSS.css'

/*
* Egress() - **PAGE**
*
* Description:
*      Page component where specifically ingress operations will
*      be displayed 
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/
function Ingress() {
  return(
    <div className=''>
      <div>
        <img src={DCU_Front}></img>
      </div>
      <div>
        <img src={UIA_Panel}></img>
      </div>
    </div>
  )
}

export default Ingress;