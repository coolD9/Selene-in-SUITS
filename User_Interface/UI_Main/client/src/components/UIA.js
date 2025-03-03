import React from 'react';
import './css/MasterCSS.css';
import './css/UIACSS.css';
import { useNavigate } from 'react-router-dom';

/*
* UIA() - **PAGE**
*
* Description:
*      Page component where UIA tasks and procedures will be
*      displayed.
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed which shows two sections
*     for egress/ingress with relevant buttons
*/
function UIA() {
  const navigate = useNavigate();

  const navEgress = () =>
  {
    navigate('/uia/egress');
  }

  const navIngress = () =>
  {
    navigate('/uia/ingress');
  }

  return(
    <div className='theme_background'>
      <div className='monitor_container theme_light_border'>
          <p className='theme_text theme_light_border monitor_title'>Status Monitor</p>
          <div className='monitor_statuses'>
            <div className='status_block'>
              <p>EMU1 Power: Value</p>
              <p>EV1 Supply: Value</p>
              <p>EV1 Waste: Value</p>
              <p>EV1 Oxygen: Value</p>
              <p>O2 Vent: Value</p>
            </div>
            <div className='status_block'>
              <p>EMU2 Power: Value</p>
              <p>EV2 Supply: Value</p>
              <p>EV2 Waste: Value</p>
              <p>EV2 Oxygen: Value</p>
              <o>Depress Pump: Value</o>

            </div>
            <div className='status_block'>
              <p>Battery: Value</p>
              <p>Oxygen: Value</p>
              <p>Comms: Value</p>
              <p>Fan: Value</p>
              <p>Pump: Value</p>
              <p>CO2: Value</p>
            </div>
          </div>
          
         
        
      </div>
      <div className='UIA_container  theme_text'>
        
        <div className='egress_container theme_light_border'>
          <div>
            <button className="egress_button theme_light_border" onClick={navEgress}>Egress</button>
          </div>
        </div>
        <div className='ingress_container theme_light_border'>
          <div>
            <button className='ingress_button theme_light_border' onClick={navIngress}>Ingress</button>

          </div>
        </div>
      </div>
    </div>
  )
}

export default UIA;