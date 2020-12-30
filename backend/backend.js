const express = require('express');     // Using Express app for communications
const cors = require('cors');           // CORS
const { spawn } = require('child_process');      // Allows Node.js to call outside programs (python in this case)
// const body_parser = require('body-parser');
const app = express();
const port = 3000;
// app.use(body_parser.json());
app.use(cors());

// GET 
app.get('/', (req, res) => {
    // Kill any other python processes
    // spawn("tskill", ["python"]);
    const kill = spawn("pkill", ["-9", "-f", "main.py"]);

    // What information did we receive?
    console.log(`Effect: ${req.query.effect}`);
    console.log(`Args: ${req.query.args}`);
    
    // Start the effect animation
    console.log("python3", ["../effects/main.py", 0].concat(req.query.args));
    //const child = spawn("py", ["../effects/main.py", 0].concat(req.query.args));
    kill.on('close', () => {

    	const child = spawn("python3", ["../effects/main.py", 0].concat(req.query.args));
    child.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });
    child.stderr.on('data', (data) => {
        // console.error(`stderr: ${data}`);
        console.log(`stderr: ${data}`);
    });
    child.on('close', (code) => {
        console.log(`Child process exited with code ${code}.`);
    });

    res.json(`Request received`);
});

// Start listening
app.listen(port, () => {
    console.log(`Listening at http://localhost:${port}`);
});
