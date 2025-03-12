import React from 'react';
import './css/MasterCSS.css';
import './css/UIACSS.css';
import { useNavigate } from 'react-router-dom';
import UIA_JSON from './../TEST_JSON/UIA.json'
import DCU_JSON from './../TEST_JSON/DCU.json'

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

          <div className='device_titles'>
            <div className='uia_mon_title theme_light_border'>
              <p>UIA</p>
            </div>
            <div className='dcu_mon_title theme_light_border'>
              <p>DCU</p>
            </div>
          </div>
          
          {/* Div for status blocks */}
          <div className='monitor_statuses'>

            {/* Left status block (EV1 UIA Values) */}
            <div className='status_block'>

              {/* EMU1 Power Value */}
              <div className='uia_pair lm_drop'>
                <div className='value_title'>
                <p>EMU1 Power:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.eva1_power ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.eva1_power ? 'ON' : 'OFF'} </p>
                </div>
              </div>
              
              {/* EV1 Supply Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Supply:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.eva1_water_supply ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.eva1_water_supply ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>

              {/* EV1 Waste Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Waste:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.eva1_water_waste ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.eva1_water_waste ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>

              {/* EV1 Oxygen Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Oxygen:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.eva1_oxy ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.eva1_oxy ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>

              {/* O2 Vent Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>O2 Vent:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.oxy_vent ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.oxy_vent ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>
            </div>
            
            {/* Left Middle status block (EV2 UIA Values) */}
            <div className='status_block'>

              {/* EMU2 Power Value */}
              <div className='uia_pair lm_drop'>
                <div className='value_title'>
                <p>EMU2 Power:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.eva2_power ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.eva2_power ? 'ON' : 'OFF'}</p>
                </div>
              </div>
              
              {/* EV2 Supply Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Supply:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.eva2_water_supply ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.eva2_water_supply ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>

              {/* EV2 Waste Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Waste:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.eva2_water_waste ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.eva2_water_waste ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>

              {/* EV2 Oxygen Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Oxygen:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.eva2_oxy ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.eva2_oxy ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>

              {/* UIA Depress Pump Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>Depress Pump:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={UIA_JSON.uia.depress ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{UIA_JSON.uia.depress ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>
            </div>

            {/* Right Middle block (EV1 DCU Values) */}
            <div className='status_block' id='rm_status_block'>

              {/* EV1 Battery Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                <p>EV1 Battery:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva1.batt ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva1.batt ? 'SUIT BATT' : 'UMBILICAL'}</p>
                </div>
              </div>
              
              {/* EV1 Oxygen Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Oxygen:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva1.oxy ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva1.oxy ? 'PRIMARY' : 'SECONDARY'}</p>
                </div>
              </div>

              {/* EV1 Comms Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Comms:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva1.comm ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva1.comm ? 'Channel A' : 'Channel B'}</p>
                </div>
              </div>

              {/* EV1 Fan Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Fan:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva1.fan ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva1.fan ? 'PRIMARY' : 'SECONDARY'}</p>
                </div>
              </div>

              {/* EV1 Pump Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 Pump:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva1.pump ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva1.pump ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>

              {/* EV1 CO2 Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV1 CO2:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva1.co2 ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva1.co2 ? 'Scrubber A' : 'Scrubber B'}</p>
                </div>
              </div>
            </div>
            
            {/* Right status block (EV2 DCU Values) */}
            <div className='status_block'>

              {/* EV2 Battery Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                <p>EV2 Battery:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva2.batt ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva2.batt ? 'SUIT BATT' : 'UMBILICAL'}</p>
                </div>
              </div>
              
              {/* EV2 Oxygen Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Oxygen:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva2.oxy ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva2.oxy ? 'PRIMARY' : 'SECONDARY'}</p>
                </div>
              </div>

              {/* EV2 Comms Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Comms:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva2.comm? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva2.comm ? 'Channel A' : 'Channel B'}</p>
                </div>
              </div>

              {/* EV2 Fan Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Fan:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva2.fan ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva2.fan ? 'PRIMARY' : 'SECONDARY'}</p>
                </div>
              </div>

              {/* EV2 Pump Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 Pump:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva2.pump ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva2.pump ? 'OPEN' : 'CLOSED'}</p>
                </div>
              </div>

              {/* EV2 CO2 Value */}
              <div className='uia_pair'>
                <div className='value_title'>
                  <p>EV2 CO2:</p>
                </div>
                {/* Determine which value and subsequent styling to use */}
                <div className={DCU_JSON.dcu.eva2.co2 ? 'uia_value true_val' : 'uia_value false_val'}>
                  <p>{DCU_JSON.dcu.eva2.co2 ? 'Scrubber A' : 'Scrubber B'}</p>
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