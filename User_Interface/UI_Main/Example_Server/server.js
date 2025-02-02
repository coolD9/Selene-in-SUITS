const express = require("express");

const app = express();
const PORT = process.env.PORT || 5000;

console.log("Starting the server...");

// Middleware to parse JSON
app.use(express.json());

// Default route
app.get("/", (request, response) => {
  response.send("Hello Express!");
});

app.get("/status", (request, response) => {
    const status = {
       "Status": "Running"
    };
    
    response.send(status);
 });

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
