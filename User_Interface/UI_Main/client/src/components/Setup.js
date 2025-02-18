
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

          {/* The label shows the text "DUST IP:" next to the input box*/}
          <label>DUST IP:</label>

          
            {/* This creates an input box where users can type.
            name="dustInput" gives the input box a name to identify it.
            placeholder="00.0.0.000:0000" shows grayed-out example text*/}
          <input name="dustInput" placeholder="00.0.0.000:0000" />
        </div>

        <div className="form-row">
          <label>TSS IP:</label>
          <input name="tssInput" placeholder="00.0.0.000:0000" />
        </div>
        
        <div className="form-row">
          <label>DUST IP:</label>
          <input name="dustInput" placeholder="00.0.0.000:0000" />
        </div>

        <div className="form-row">
          <label>EVA 1:</label>
          <input name="evaInput" placeholder="00.0.0.000:0000" />
        </div>

        <div className="form-row">
          <label>EVA 2:</label>
          <input name="eva2Input" placeholder="00.0.0.000:0000" />
        </div>

        <div className="form-row">
          <label>LTV:</label>
          <input name="ltvInput" placeholder="00.0.0.000:0000" />
        </div>
      </form>
    </div>
  );
}

export default Setup;