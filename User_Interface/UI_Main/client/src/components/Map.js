import React from "react";
import "./css/MapCSS.css";

/*
 * Map() - **PAGE**
 *
 * Description:
 *      Page component where Map-specific items will be built
 *      and displayed, such as 2D map, LTV items, etc.
 *
 * Params:
 *     None
 *
 * Returns:
 *     A JSX object to be displayed.
 */
function Map() {
  return (
    <div>
      <div className="ParentContainerEVA">
        <div className="EVA" id="container3">
          <h1>EVA1</h1>
        </div>
        <div className="EVA" id="container4">
          <h1>EVA2</h1>
        </div>
      </div>

      <div className="ParentContainerLTV">
        <div className="LTV" id="container1">
          <h1>LTV1</h1>
        </div>
        <div className="LTV" id="container2">
          <h1>LTV2</h1>
        </div>
      </div>

      <div className="WarningContainer">
        <h1>Warning</h1>
      </div>
    </div>
  );
}

export default Map;
