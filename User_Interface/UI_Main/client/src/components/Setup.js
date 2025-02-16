import React from 'react';

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
    <div>

        <h2>Enter IP adressses</h2>
       
        <div className = "dust">
          <label>DUST IP: </label>
          <input name="dustInput" defaultValue="00.0.0.000:0000" />

        </div>

        <div className = "tss">
          <label>TSS IP: </label>
          <input name="tssInput" defaultValue="00.0.0.000:0000" />
          
        </div>
        
        <div className = "dust">
          <label>DUST IP: </label>
          <input name="dustInput" defaultValue="00.0.0.000:0000" />
          
        </div>

        <div className = "eva">
          <label>EVA 1: </label>
          <input name="evaInput" defaultValue="00.0.0.000:0000" />
        </div>

        <div className = "eva2">
          <label>EVA 2: </label>
          <input name="eva2Input" defaultValue="00.0.0.000:0000" />
        </div>

        <div className = "ltv">
          <label>LTV : </label>
          <input name="ltvInput" defaultValue="00.0.0.000:0000" />
        </div>


    </div>
  )
}

export default Setup;