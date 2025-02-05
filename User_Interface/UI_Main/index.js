const express = require("express");
const path = require("path");


const app = express();
const PORT = process.env.PORT || 5000;

console.log("Starting the server...");

// Middleware to parse JSON
app.use(express.json());

app.use(express.static(path.join(__dirname, "public")));

// Default route
app.get("/", (request, response) => {
  response.send("Hello World!");
});

app.get("/map", (request, response) => {
    response.sendFile(path.join(__dirname, "public/html", "map.html"));
  });

app.get("/eva", (request, response) => {
    response.sendFile(path.join(__dirname, "public/html", "eva.html"));
  });


// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
