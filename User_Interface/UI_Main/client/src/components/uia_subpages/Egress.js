import React from 'react';
import Collapsible from "./../Collapsible";
import DCU_Front from "./../images/DCU_Front.jpg";
import SUITS_UIA_PANEL from "./../images/SUITS_UIA_PANEL.jpg";
import './../css/UIASubpageCSS.css'

/*  
* Egress() - **PAGE**
*
* Description:
*      Page component where specifically egress operations will
*      be displayed 
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/
function Egress() {
  return(
    <div className="container">
       <div className="text-container">
        <h2>Egress Operations</h2>
        <p>
          This section showcases the egress operations involved in our system. 
        </p>


        <Collapsible title="Connect UIA to DCU and Start Depress">
          <label className="checkbox-container">
            <span>UIA and DCU 1. EV1 and EV2 connect UIA and DCU umbilical</span>
            <input type="checkbox"/>
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>UIA 2. EV-1, EV-2 PWR – ON</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>BOTH DCU 3. BATT – UMB</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>UIA 4. DEPRESS PUMP PWR – ON</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>
        </Collapsible> 


        <Collapsible title="Prep O2 Tanks">
          <label className="checkbox-container">
            <span>UIA 1. OXYGEN O2 VENT – OPEN </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span> HMD 2. Wait until both Primary and Secondary OXY tanks are less than 10psi</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>UIA 3. OXYGEN O2 VENT – CLOSE </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>BOTH DCU 4. OXY – PRI</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>UIA 5. OXYGEN EMU-1, EMU-2 – OPEN</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>HMD 6. Wait until EV1 and EV2 Primary O2 tanks greate than 3000 psi </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>UIA 7. OXYGEN EMU-1, EMU-2 – CLOSE </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>BOTH DCU 8. OXY – SEC</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>UIA 9. OXYGEN EMU-1, EMU-2 – OPEN</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>HMD 10. Wait until EV1 and EV2 Secondary O2 tanks greate than 3000 psi</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>UIA 11. OXYGEN EMU-1, EMU-2 – CLOSE </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

          <label className="checkbox-container">
            <span>BOTH DCU 12. OXY – PRI</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
          </label>

        </Collapsible>

        <Collapsible title="Prep Water Tanks">
         <label className="checkbox-container">
            <span>BOTH DCU 1. PUMP – OPEN</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>UIA 2. EV-1, EV-2 WASTE WATER – OPEN</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>HMD 3. Wait until water EV1 and EV2 Coolant tank is less than 5%</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>UIA 4. EV-1, EV-2 WASTE WATER – CLOSE</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>UIA 5. EV-1, EV-2 SUPPLY WATER – OPEN</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>HMD 6. Wait until water EV1 and EV2 Coolant tank is greater than 95%</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>UIA 7. EV-1, EV-2 SUPPLY WATER – CLOSE </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>BOTH DCU 8. PUMP – CLOSE</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>
        
        </Collapsible>

        <Collapsible title="END Depress, Check Switches and Disconnect">

        <label className="checkbox-container">
            <span>HMD 1. Wait until SUIT P, O2 P = 4 </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>UIA 2. DEPRESS PUMP PWR – OFF </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>BOTH DCU 3. BATT – LOCAL </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>UIA 4. EV-1, EV-2 PWR - OFF </span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>BOTH DCU 5. Verify OXY – PRI</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>BOTH DCU 6. Verify COMMS – A</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>BOTH DCU 7. Verify FAN – PRI</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>BOTH DCU 8. Verify PUMP – CLOSE</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>BOTH DCU 9. Verify CO2 – A</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>

         <label className="checkbox-container">
            <span>UIA and DCU 10. EV1 and EV2 disconnect UIA and DCU umbilical</span>
            <input type="checkbox" />
            <span class="checkmark"></span>
         </label>
        
        </Collapsible>

      </div>
      
      <div className="image-column">
        <div className="image-container">
          <img className="DCUFront_image" src={DCU_Front} alt="DCU Front" />
        </div>

        <div className="image-container">
          <img className="SUITS_UIA_PANEL_image" src={SUITS_UIA_PANEL} alt="Panel" />
        </div>
      </div>
    </div>
    
  );
}

export default Egress;