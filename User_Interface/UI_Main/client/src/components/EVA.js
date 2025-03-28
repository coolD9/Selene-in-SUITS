import React from 'react';
import "./css/EVA.css";
/*
* EVA() - **PAGE**
*
* Description:
*      Page component where EVA-specific items will be built
*      and displayed, such as EVA telemetry, tasks, XRF, etc.
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/
function EVA() {
  return (
   
    <div className = "Adam">
      <div className = "lilin">
        <h1>Lilin</h1>
        <p>This is where the vitals of both plug suits will be displayed.</p>
      </div>

      <div className = "task_tracker">
        <h1>Task Tracker</h1>
        <p>This is where mission tasks will be displayed.</p>
        
        <div>
          <h1>Warnings</h1>
        </div>        
      </div>

      <div className = "xray_tracker">
        <h1>X-Ray Data</h1>
        <p>This is where Xray Spectrometry data will be displayed.</p>
      </div>
    </div>

  );
}

export default EVA;

/*
   <div className = "EVAngelion_container" >
      <div className = "panel EV_tracker">
        <p>Here is where the EV tracker info will be</p>
      </div>
      <div className = "panel task_tracker">
        <p>Here is where the tasks will be tracked</p>
      <button onClick={alert('Shinji get in the robot')}>Click Me!</button>
      </div>
      <div className = "panel xray_tracker">
        <p>Here is where the Xray Spectrometry will be</p>
      </div>
    </div>

*/
