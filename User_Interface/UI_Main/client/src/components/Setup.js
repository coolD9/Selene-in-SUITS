import React from 'react';

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

      {/* Sets how the page should be formated. 
          If try to place this in css, the inpt boxes will not be
          aligned properly.*/}
      <style>{`

        .setup-container {
          
          padding: 20px;
          max-width: 500px;
        }

        .ip-form {
          display: flex;
          flex-direction: column;
          gap: 15px;
        }

        .form-row {
          display: grid;
          grid-template-columns: 80px 1fr;
          align-items: center;
          gap: 10px;
        }

        label {
          color: black;
          font-size: 16px;
          font-family: Arial, Helvetica, sans-serif;
          font-weight: normal;
        }

        input {
          padding: 8px;
          border: 1px solid #ccc;
          border-radius: 4px;
          font-size: 16px;
          width: 100%;
        }
      `}</style>
    </div>
  );
}

export default Setup;