const express = require('express');
const path = require('path');
const uploadRoutes = require('./upload');

const app = express();
const port = 3000;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));


app.use('/upload', uploadRoutes);

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});