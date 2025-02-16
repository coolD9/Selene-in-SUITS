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
       
        <label>
          DUST IP: <input name="dustInput" defaultValue="00.0.0.000:0000" />
        </label>
        

        <p>
          TSS IP: <input name="tssInput" defaultValue="00.0.0.000:0000" />
        </p>

        <p>
          EVA 1: <input name="eva1Input" defaultValue="00.0.0.000:0000" />
        </p>

        <p>
          EVA 2:<input name="eva2sInput" defaultValue="00.0.0.000:0000" /> 
        </p>

        <p>
          LTV: <input name="ltvInput" defaultValue="00.0.0.000:0000" />
        </p>

    </div>
  )
}

export default Setup;