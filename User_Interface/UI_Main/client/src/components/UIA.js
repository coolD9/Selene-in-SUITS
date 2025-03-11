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

              {/* EMU1 Power Value */}
              <div className='uia_pair lm_drop'>
                <div className='value_title'>
                <p>EMU1 Power:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>
              
              {/* EV1 Supply Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Supply:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* EV1 Waste Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Waste:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* EV1 Oxygen Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Oxygen:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* O2 Vent Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>O2 Vent:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>
            </div>
            
            {/* Middle status block */}
            <div className='status_block'>

              {/* EMU2 Power Value */}
              <div className='uia_pair lm_drop'>
                <div className='value_title'>
                <p>EMU2 Power:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>
              
              {/* EV2 Supply Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Supply:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* EV2 Waste Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Waste:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* EV2 Oxygen Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Oxygen:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* Depress Pump Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>Depress Pump:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>
            </div>
            
            {/* Right status block */}
            <div className='status_block'>

              {/* Battery Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                <p>Battery:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>
              
              {/* Oxygen Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>Oxygen:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* Comms Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>Comms:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* Fan Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>Fan:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* Pump Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>Pump:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>

              {/* CO2 Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>CO2:</p>
                </div>
                <div className='uia_value'>
                  <p>Value</p>
                </div>
              </div>
            </div>
          </div>{/* End status block spanning div */}
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