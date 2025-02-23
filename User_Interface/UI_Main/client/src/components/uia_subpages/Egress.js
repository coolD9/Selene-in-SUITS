import React from 'react';
import DCU_Front from "./../images/DCU_Front.jpg";

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
    <div>
     <p> Hello World </p>
     <img src={DCU_Front}> 
     </img>
    </div>
  )
}

export default Egress;