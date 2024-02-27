const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;
const filePath = '/home/snm/server/a.txt';

app.get('/', (req, res) => {
    // res.sendFile(__dirname + '/index.html');
    res.sendFile(__dirname + '/index.html');

});

app.get('/chart', (req, res) => {
    res.sendFile(__dirname + '/chart.js');
});

app.get('/updates', (req, res) => {
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');

    // Send SSE updates to the client 
    const interval = setInterval(() => {

        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
              console.error(`Error reading the file: ${err}`);
              return;
            }
          
            const lines = data.trim().split('\n');
            const integers = lines.map((line) => parseInt(line, 10));
          
            res.write(`data: ${JSON.stringify(integers)}\n\n`);
            console.log(integers)
          });        
        
        /* // To stop sending updates
        if (count > 20) {
            clearInterval(interval);
            res.end(); // End the SSE connection
        } */

    }, 300);
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
