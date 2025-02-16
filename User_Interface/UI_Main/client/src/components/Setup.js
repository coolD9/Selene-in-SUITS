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
        <h2>Setup Page</h2>
        <p>This is the Setup Page!</p>

        <h2>Enter IP adressses</h2>
       
        <label>
        DUST IP: <input name="myInput" defaultValue="00.0.0.000:0000" />
        </label>

        <p>DUST IP:</p>
        <p>TSS IP:</p>

        <p>EVA 1:</p>
        <p>EVA 2:</p>
        <p>LTV:</p>

    </div>
  )
}

export default Setup;