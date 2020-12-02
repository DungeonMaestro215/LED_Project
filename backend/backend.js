const express = require('express');
const cors = require('cors');
// const body_parser = require('body-parser');
const app = express();
const port = 3000;
// app.use(body_parser.json());
app.use(cors());

app.get('/', (req, res) => {
    res.json(`Hello, World!`);
    console.log(`New Visitor ID:${req.query.id}`);
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});