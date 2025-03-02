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