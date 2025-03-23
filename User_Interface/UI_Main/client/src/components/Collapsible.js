import React, { useState } from "react";

function Collapsible({ title, children }) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="collapsible">
      <button className="collapsible-header" onClick={() => setIsOpen(!isOpen)}>
        {title} {isOpen ? "▲" : "▼"}
      </button>
      {isOpen && <div className="collapsible-content">{children}</div>}
    </div>
  );
}

export default Collapsible;
