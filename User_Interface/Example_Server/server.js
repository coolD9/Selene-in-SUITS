const express = require("express");

const app = express();
const PORT = process.env.PORT || 5000;

console.log("Starting the server...");

// Middleware to parse JSON
app.use(express.json());

// Default route
app.get("/", (request, response) => {
  response.send("Hello to Express!");
});

// typing `/status` onto the end of the url will show the status of the server
app.get("/status", (request, response) => {
    const status = {
       "Status": "Running"
    };
    
    response.send(status);
 });


app.post("/api/register", (req, res) => {
  // Get data sent in the request body
  const { username, email, password } = req.body;

  // Simulate saving the user to a database (in real life, you'd use a DB)
  if (username && email && password) {
    res.status(201).json({ message: `User ${username} registered successfully!` });
  } else {
    res.status(400).json({ error: "Missing required fields (username, email, password)" });
  }
});


// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
