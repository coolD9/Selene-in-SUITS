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
    <div className = "EVAngelion_container" >
      <div className = "panel EV_tracker">
        <p>Here is where the EV tracker info will be</p>
      </div>
      <div className = "panel task_tracker">
        <p>Here is where the tasks will be tracked</p>
        {/* Note that this is where the Modals will be. Currently utilizing scroll bar */}
        <button onClick={alert('Shinji get in the robot')}>Click Me!</button>
      </div>
      <div className = "panel xray_tracker">
        <p>Here is where the Xray Spectrometry will be</p>
      </div>
    </div>
  );
}

export default EVA;
