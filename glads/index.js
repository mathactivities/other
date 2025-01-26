const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', (req, res) => {
    const uid = req.query.uid;
    const dataString = req.query.data;

    if (!uid) {
        return res.status(400).send('UID is required.');
    }

    if (dataString === undefined || dataString === null) {
      return res.status(400).send('Data is required.');
    }

    try {
        // Attempt to parse the incoming data as JSON
        JSON.parse(dataString); // This will throw an error if it's not valid JSON
    } catch (jsonError) {
        return res.status(400).send('Invalid data format. Must be valid JSON.');
    }

    fs.readFile('user_data.json', 'utf8', (err, fileData) => {
        let data = {};

        if (!err) {
            try {
                data = JSON.parse(fileData);
            } catch (parseError) {
                console.error("Error parsing existing JSON:", parseError);
                data = {};
            }
        } else if (err.code !== 'ENOENT') {
            console.error('Error reading file:', err);
            return res.status(500).send('Error reading data file.');
        }

        data[uid] = dataString; // Store the JSON string

        fs.writeFile('user_data.json', JSON.stringify(data), (writeErr) => {
            if (writeErr) {
                console.error('Error writing to file:', writeErr);
                return res.status(500).send('Error writing to data file.');
            } else {
                const currentDate = new Date();
                console.log(`Data for UID ${uid} written to user_data.json`);
                res.send(`At: ${currentDate} Data for UID ${uid} received and written to file.`);
            }
        });
    });
});

app.listen(port, () => {
    console.log(`Server listening on port http://localhost:${port}`);
});