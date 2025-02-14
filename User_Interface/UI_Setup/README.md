### WIP - Need to add front end stuff

# UI Setup - Backend
## Installing Node.js and Express.JS
For the backend portion of our tech stack, we will be using Node and Express. Node.js helps run the local server on your machine which
you can edit and code on. Express.js is used for API functionality as it allows us to use HTTP requests such as `GET`, `POST`, `PUT`, `DELETE`, etc.
These backend portions are how we will coordinate all of the information to handle our app. As of right now, we decided to forego a database
framework, but that may be implemented later.

### 1. Update System
Update your apt using the following:
```
sudo apt update && sudo apt upgrade -y
```

### 2. Install Node.js and npm
> npm is a package manager

Download LTS npm version
```
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
```
Install Node.js and npm
```
sudo apt install -y nodejs
```

Check versions
```
node -v
npm -v
```
These should be at least `v22.13.1` and `10.9.2` respectively

### 3. Install Express
This is the framework that allows us to use HTTP commands
```
npm install express
```

### 4. Install Nodemon
This utility lets you actively change your server code and you don't have to restart the whole process again. 
```
npm install -g nodemon
```

## Basic server
I recommend creating your own server on your own and familiarize yourself with how hosting a local server can be achieved. Following the steps below is the framework for creating and hosting your own basic one.
**DO NOT** upload your own server to the GitHub, as a simple example one has already been created in [Example_Server](./../Example_Server/).

### 1. Create a new directory
Create a new foler/directory to store your server **on your own repo**

### 2. Setup Server Files
Create your own file to host the server code, ex:
```
touch server.js
```
Then you can run the following command to build the foundation files which are managed automatically for you.
```
npm init -y
```

### 3. Experiment
The following code is barebones, and does nothing except provide a home page with a simple `Hello World!` dialogue. Feel free to tweak and ask ChatGPT more about what you can do to add onto this server.
```js
const express = require("express");

const app = express();
const PORT = process.env.PORT || 5000;

console.log("Starting the server...");

// Middleware to parse JSON
app.use(express.json());

// Default route
app.get("/", (request, response) => {
  response.send("Hello World!");
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```
### 4. Run the server
Next, you can use the following command (assuming you installed nodemon) to start up your server. 
```
nodemon server.js
```
If you're using VSCode, you might recieve a popup indicating that your app is now running in the browser, you can click that.


Alternatively, go to a browser, and type in
```
http://localhost:5000/
```
You will then find the `Hello World!` statement.