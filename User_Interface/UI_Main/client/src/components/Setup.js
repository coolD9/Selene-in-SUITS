import React, { useState } from 'react'; // Import useState hook to add state management to function components
import "./css/SetupCSS.css";
import "./css/MasterCSS.css";

/*
* Setup() - PAGE
*
* Description:
*      Page component where connectivity information will be
*      input, such as TSS and interoperability IP addresses.
*      Now wrapped in a page-wrapper div for full-height styling.
*      Includes validation for IP address inputs.
*
* Params:
*     None
*
* Returns:
*     A JSX object to be displayed.
*/

function Setup() {
  // Initialize state for form inputs with empty strings for each input field
  // inputs = current state values, setInputs = function to update this state
  const [inputs, setInputs] = useState({
    dustInput: '',
    tssInput: '',
    dust2Input: '',
    evaInput: '',
    eva2Input: '',
    ltvInput: ''
  });
  
  // Initialize state for error messages, matching each input field
  // errors = current error messages, setErrors = function to update errors
  const [errors, setErrors] = useState({
    dustInput: '',
    tssInput: '',
    dust2Input: '',
    evaInput: '',
    eva2Input: '',
    ltvInput: ''
  });

  // Function to validate IP address with port format: xxx.xxx.xxx.xxx:xxxx
  // Returns an error message string if invalid, empty string if valid
  const validateIpWithPort = (value) => {
    // Check if input is empty after removing whitespace
    if (!value.trim()) {
      return "IP address is required";
    }
    
    // Split input by colon to separate IP and port
    // Example: "192.168.1.1:8080" becomes ["192.168.1.1", "8080"]
    const parts = value.split(':');
    // Check if we have exactly 2 parts (IP and port)
    if (parts.length !== 2) {
      return "Format must be IP:PORT (e.g., 192.168.1.1:8080)";
    }
    
    // Destructure the parts array to separate variables
    const [ip, port] = parts;
    
    // Create regex to validate IP format (four groups of 1-3 digits separated by dots)
    // \d{1,3} means 1-3 digits, the pattern checks for 4 sets separated by dots
    const ipRegex = /^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/;
    // Test if IP matches the pattern and capture the segments
    const ipMatch = ip.match(ipRegex);
    
    // If no match found, IP format is invalid
    if (!ipMatch) {
      return "Invalid IP address format";
    }
    
    // Check if each segment is a valid number between 0-255
    // ipMatch.slice(1) gets the captured groups (the four segments)
    // .every() checks if all segments meet the condition
    const validSegments = ipMatch.slice(1).every(segment => {
      // Convert segment from string to number
      const num = parseInt(segment, 10);
      // Check if number is within valid IP range
      return num >= 0 && num <= 255;
    });
    
    // If any segment is outside 0-255 range, IP is invalid
    if (!validSegments) {
      return "IP segments must be between 0-255";
    }
    
    // Validate port number (must be 1-65535)
    const portNum = parseInt(port, 10);
    // Check if port isn't a number or outside valid range
    if (isNaN(portNum) || portNum < 1 || portNum > 65535) {
      return "Port must be between 1-65535";
    }
    
    return ""; // Empty string means valid input
  };

  // Handler function for input changes, runs whenever user types in any field
  const handleChange = (e) => {
    // Extract input field name and current value from the event
    const { name, value } = e.target;
    
    // Update the inputs state, keeping all other values the same
    // prev = previous state, ...prev = spread operator to copy all existing values
    // [name]: value = update just the changed field using computed property name
    setInputs(prev => ({
      ...prev,
      [name]: value
    }));
    
    // Validate the new input value
    const error = validateIpWithPort(value);
    // Update just this field's error in the errors state
    setErrors(prev => ({
      ...prev,
      [name]: error
    }));
  };

  // Handler function for form submission
  const handleSubmit = (e) => {
    // Prevent default form submission behavior (page refresh)
    e.preventDefault();
    
    // Validate all fields at submission time
    let formIsValid = true;  // Assume form is valid initially
    const newErrors = {};    // Object to collect all error messages
    
    // Loop through all input fields by name
    Object.keys(inputs).forEach(name => {
      // Validate each field's current value
      const error = validateIpWithPort(inputs[name]);
      // Store error message for this field
      newErrors[name] = error;
      // If any field has an error, mark the form as invalid
      if (error) {
        formIsValid = false;
      }
    });
    
    // Update errors state with all validation results
    setErrors(newErrors);
    
    // If form passes validation, proceed with submission
    if (formIsValid) {
      // Form is valid, you can proceed with submission
      console.log("Form is valid:", inputs);
      // Add your form submission logic here
    } else {
      console.log("Form has errors, please fix them");
    }
  };

  return (
    <div className="theme_background">
      <div className="">
        <h2 className="theme_heading"> Enter IP addresses</h2>

        {/* Form with onSubmit handler to process the form when submitted */}
        <form className="ip-form" onSubmit={handleSubmit}>
          {/* Form row for DUST IP */}
          <div className="form-row">
            <label>DUST IP:</label>
            {/* Container to group input and its error message */}
            <div className="input-container">
              <input 
                name="dustInput" 
                placeholder="192.168.1.1:8080" 
                value={inputs.dustInput}   // Controlled component: value comes from state
                onChange={handleChange}    // Call handler when input changes
                className={errors.dustInput ? "input-error" : ""}  // Add error class if error exists
              />
              {/* Conditional rendering: only show error if it exists */}
              {errors.dustInput && <div className="error-message">{errors.dustInput}</div>}
            </div>
          </div>

          <div className="form-row">
            <label>TSS IP:</label>
            <div className="input-container">
              <input 
                name="tssInput" 
                placeholder="192.168.1.1:8080" 
                value={inputs.tssInput}
                onChange={handleChange}
                className={errors.tssInput ? "input-error" : ""}
              />
              {errors.tssInput && <div className="error-message">{errors.tssInput}</div>}
            </div>
          </div>

          <div className="form-row">
            <label>DUST IP:</label>
            <div className="input-container">
              <input 
                name="dust2Input" 
                placeholder="192.168.1.1:8080" 
                value={inputs.dust2Input}
                onChange={handleChange}
                className={errors.dust2Input ? "input-error" : ""}
              />
              {errors.dust2Input && <div className="error-message">{errors.dust2Input}</div>}
            </div>
          </div>

          <div className="form-row">
            <label>EVA 1:</label>
            <div className="input-container">
              <input 
                name="evaInput" 
                placeholder="192.168.1.1:8080" 
                value={inputs.evaInput}
                onChange={handleChange}
                className={errors.evaInput ? "input-error" : ""}
              />
              {errors.evaInput && <div className="error-message">{errors.evaInput}</div>}
            </div>
          </div>

          <div className="form-row">
            <label>EVA 2:</label>
            <div className="input-container">
              <input 
                name="eva2Input" 
                placeholder="192.168.1.1:8080" 
                value={inputs.eva2Input}
                onChange={handleChange}
                className={errors.eva2Input ? "input-error" : ""}
              />
              {errors.eva2Input && <div className="error-message">{errors.eva2Input}</div>}
            </div>
          </div>

          <div className="form-row">
            <label>LTV:</label>
            <div className="input-container">
              <input 
                name="ltvInput" 
                placeholder="192.168.1.1:8080" 
                value={inputs.ltvInput}
                onChange={handleChange}
                className={errors.ltvInput ? "input-error" : ""}
              />
              {errors.ltvInput && <div className="error-message">{errors.ltvInput}</div>}
            </div>
          </div>

          {/* Submit button to trigger form validation and submission */}
          <button type="submit" className="submit-button">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default Setup;