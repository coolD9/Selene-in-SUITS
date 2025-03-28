import React from 'react';
import DCU_Front from './../images/DCU_Front.jpg'
import SUITS_UIA_PANEL from "./../images/SUITS_UIA_PANEL.jpg";
import './../css/MasterCSS.css'
import './../css/UIACSS.css'
import './../css/UIASubpageCSS.css'
import Collapsible from "./../Collapsible";


/*
* Ingress() - **PAGE**
*
* Description:
*      Page component where specifically ingress operations will
*      be displayed 
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/
function Ingress() {
  return(

    
    <div className="container">
    <div className="text-container">
     <h2>Ingress Operations</h2>
     <p>
       This section showcases the Ingress operations involved in our system. 
     </p>


     <Collapsible title="Pending steps">
     <label className="checkbox-container">
         <span>Step 1 </span>
         <input type="checkbox" />
         <span class="checkmark"></span>
      </label>
     </Collapsible> 


     <Collapsible title="Pending steps">
     <label className="checkbox-container">
         <span>Step 1 </span>
         <input type="checkbox" />
         <span class="checkmark"></span>
      </label>

     </Collapsible>

     <Collapsible title="Pending steps">
     <label className="checkbox-container">
         <span>Step 1 </span>
         <input type="checkbox" />
         <span class="checkmark"></span>
      </label>
     
     </Collapsible>

     <Collapsible title="Pending steps">

     <label className="checkbox-container">
         <span>Step 1 </span>
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
  )
}

export default Ingress;