import React from 'react';
import "./css/SetupCSS.css";


/*
* Setup() - PAGE
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
  return (
    <div className="setup-container">
      <h2>Enter IP addresses</h2>
      
      {/* Form used for input fields.*/}
      <form className="ip-form">

        <div className="form-row">
          <label>DUST IP:</label>
          <input name="dustInput" defaultValue="00.0.0.000:0000" />
        </div>

        <div className="form-row">
          <label>TSS IP:</label>
          <input name="tssInput" defaultValue="00.0.0.000:0000" />
        </div>
        
        <div className="form-row">
          <label>DUST IP:</label>
          <input name="dustInput" defaultValue="00.0.0.000:0000" />
        </div>

        <div className="form-row">
          <label>EVA 1:</label>
          <input name="evaInput" defaultValue="00.0.0.000:0000" />
        </div>

        <div className="form-row">
          <label>EVA 2:</label>
          <input name="eva2Input" defaultValue="00.0.0.000:0000" />
        </div>

        <div className="form-row">
          <label>LTV:</label>
          <input name="ltvInput" defaultValue="00.0.0.000:0000" />
        </div>
      </form>

    </div>
  );
}

export default Setup;