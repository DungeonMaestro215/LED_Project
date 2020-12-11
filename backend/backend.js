const express = require('express');
const cors = require('cors');
const { exec } = require('child_process');
// const body_parser = require('body-parser');
const app = express();
const port = 3000;
// app.use(body_parser.json());
app.use(cors());

app.get('/', (req, res) => {
    // res.json(`Hello, World!`);
    console.log(`Effect: ${req.query.effect}`);
    
    exec("tskill python");
    exec("py main.py 0 fill 3 7 1 150 150", (error, stdout, stderr) => {
        // if (error) {
        //     console.log(`error: ${error.message}`);
        //     return;
        // }
        // if (stderr) {
        //     console.log(`stderr: ${stderr}`);
        //     return;
        // }
        // console.log(`stdout: ${stdout}`);
    }, { stdio: [0, 1, 2]});
});

app.listen(port, () => {
    console.log(`Listening at http://localhost:${port}`);
});