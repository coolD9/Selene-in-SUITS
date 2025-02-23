import { display } from "@mui/system";
import React, { useState } from "react";
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
  const [size, setSize] = useState("");

  const resizeit = () => {
    setSize(size === "370" ? "740" : "370");
  };
  return (
    <div className="body">
      <div className="LeftContainer">
        <div className="ParentContainerEVA">
          <div className="EVA" id="container1">
            <h1>EVA1</h1>
            <div className="resize">
              <button onClick={resizeit} type="button">
                Resize
              </button>
            </div>
          </div>
          <div className="EVA" id="container2">
            <h1>EVA2</h1>
            <div className="resize">
              <button onClick={resizeit} type="button">
                Resize
              </button>
            </div>
          </div>
        </div>

        <div className="ParentContainerLTV">
          <div className="LTV" id="container3">
            <h1>LTV1</h1>
            <div className="resize">
              <button onClick={resizeit} type="button">
                Resize
              </button>
            </div>
          </div>
          <div className="LTV" id="container4">
            <h1>LTV2</h1>
            <div className="resize">
              <button onClick={resizeit} type="button">
                Resize
              </button>
            </div>
          </div>
        </div>

        <div className="WarningContainer">
          <h1>Control</h1>
        </div>
      </div>

      <div className="mapcontainer">
        <h1 id="map">Map</h1>
      </div>
    </div>
  );
}

export default Map;
