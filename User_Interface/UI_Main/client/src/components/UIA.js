import React from 'react';
import './css/MasterCSS.css';
import './css/UIACSS.css';
import { useNavigate } from 'react-router-dom';

/*
* UIA() - **PAGE**
*
* Description:
*      Page component where UIA statuses can be viewed as
*      well as begin egress or ingress operations
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed which shows two sections
*     for egress/ingress with relevant buttons as well as
*     a section for monitoring UIA status
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
      {/* Status monitor div */}
      <div className='monitor_container theme_light_border'>
          {/* Monitor title */}
          <p className='theme_text theme_light_border monitor_title'>Status Monitor</p>
          
          {/* Div for status blocks */}
          <div className='monitor_statuses'>

            {/* Left status block  */}
            <div className='status_block'>
              <p>EMU1 Power: Value</p>
              <p>EV1 Supply: Value</p>
              <p>EV1 Waste: Value</p>
              <p>EV1 Oxygen: Value</p>
              <p>O2 Vent: Value</p>
            </div>
            
            {/* Middle status block */}
            <div className='status_block'>
              <p>EMU2 Power: Value</p>
              <p>EV2 Supply: Value</p>
              <p>EV2 Waste: Value</p>
              <p>EV2 Oxygen: Value</p>
              <p>Depress Pump: Value</p>
            </div>
            
            {/* Right status block */}
            <div className='status_block'>
              <p>Battery: Value</p>
              <p>Oxygen: Value</p>
              <p>Comms: Value</p>
              <p>Fan: Value</p>
              <p>Pump: Value</p>
              <p>CO2: Value</p>
            </div>
          </div>{/* End status block div */}
      </div> {/* End monitor div */}

      {/* UIA Operations div */}
      <div className='UIA_container theme_text'>
        
        {/* Egress div */}
        <div className='egress_container theme_light_border'>
          <div>
            <button className="egress_button theme_light_border" onClick={navEgress}>Egress</button>
          </div>
        </div> {/* End egress div */}

        {/* Ingress div */}
        <div className='ingress_container theme_light_border'>
          <div>
            <button className='ingress_button theme_light_border' onClick={navIngress}>Ingress</button>
          </div>
        </div> {/* End ingress div */}

      </div> {/* End UIA Operations div */}

    </div>
  )
}

export default UIA;