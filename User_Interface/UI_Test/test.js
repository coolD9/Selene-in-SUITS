const express = require('express');
// app will use express
const app = express();
// checks to see if there's an environmental variable, if not sets port default to 3000
// **avoid hardcoding the port**
const PORT = process.env.PORT || 3000;

// configuration for express to use JSON
app.use(express.json())

// starts the server and listens to incoming requests
app.listen(PORT, () => {
    // can use ${var name} to call for a string literal and include that information
    // can also just call variable outside to be printed
    console.log(`Server is listening on http://localhost:${PORT}, PORT`, PORT);
})

// send response of Hello World when visiting homepage
app.get('/', (request, response) => {
    response.send('Hello World!');
});

app.get('/status', (request, response) => {
    const status = {
        "Status" : "Running"
    }

    response.send(status)
})



