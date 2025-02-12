import React from 'react';
import './css/UIACSS.css'

/*
* UIA() - **PAGE**
*
* Description:
*      Page component where UIA tasks and procedures will be
*      displayed.
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/
function UIA() {
  return(
    <div className='UIA_container'>
      <div className='egress_container'>
        <div className='egress_button'>
          <button>Egress</button>
        </div>
      </div>
      <div className='ingress_container'>
        <div classname='ingress_button'>
          <button>Ingress</button>
        </div>
      </div>
    </div>
  )
}

export default UIA;