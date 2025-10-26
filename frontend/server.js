const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');


const app = express();
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));


app.get('/', (req, res) => {
res.sendFile(path.join(__dirname, 'public', 'index.html'));
});


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Frontend listening on ${PORT}`));
