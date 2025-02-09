const express = require("express");
const path = require("path");
const cors = require("cors");

const app = express();
const PORT = process.env.PORT || 5000;

console.log("Starting the server...");

// Enable CORS for all requests
app.use(cors());

// Middleware to parse JSON
app.use(express.json());

app.use(express.static(path.join(__dirname, "client/build")));

// Default route
app.get("/", (request, response) => {
  response.send("Hello World!");
});

app.get("/map", (request, response) => {
    response.sendFile(path.join(__dirname, "client/build", "map.html"));
  });

app.get("/eva", (request, response) => {
    response.sendFile(path.join(__dirname, "client/build", "eva.html"));
  });

// Sample API route
app.get('/api/message', (req, res) => {
    res.json({ message: 'Hello from Express!' });
});


// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
