import React from 'react';
import './css/Setup.css'

/*
* Setup() - **PAGE**
*
* Description:
*      Page component where connectivity information will be
*      input, such as TSS and interoperability IP addresses.
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/
function Setup() {
  return(
    <div className = "tss">
        <p>Tss IP</p>

        <div className = "dust">
          <p>Dust IP</p>
        </div>

        <div className = "Interoperability">
          <p>Interoperability IP</p>
        </div>

    </div>

    
  )
} 

export default Setup;