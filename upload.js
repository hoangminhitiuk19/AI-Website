const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const { exec } = require('child_process');
const pdf = require('pdf-parse');
const mammoth = require('mammoth'); // For .docx files
const http = require('http');

const router = express.Router();
const upload = multer({ dest: 'uploads/' });

router.post('/', upload.single('file'), (req, res) => {
    const filePath = path.join(__dirname, 'uploads', req.file.filename);
    const fileExtension = path.extname(req.file.originalname).toLowerCase();

    switch (fileExtension) {
        case '.txt':
            processTextFile(filePath, res);
            break;
        case '.docx':
            processDocxFile(filePath, res);
            break;
        case '.pdf':
            processPdfFile(filePath, res);
            break;
        case '.jpg':
        case '.jpeg':
        case '.png':
        case '.gif':
            processImageFile(filePath, res);
            break;
        case '.wav':
            processAudioFile(filePath, res);
            break;
        case '.mp3':
        case '.mp4':
            processVideoFile(filePath, req, res); // Pass req and res
            break;
        default:
            res.status(400).json({ status: 'error', message: 'Unsupported file type' });
    }
});

function processTextFile(filePath, res) {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return res.status(500).json({ status: 'error', message: 'Error processing text file' });
        }
        analyzeText(data, res);
    });
}

function processDocxFile(filePath, res) {
    mammoth.extractRawText({ path: filePath })
        .then(result => {
            analyzeText(result.value, res);
        })
        .catch(err => {
            res.status(500).json({ status: 'error', message: 'Error processing .docx file' });
        });
}

function processPdfFile(filePath, res) {
    fs.readFile(filePath, (err, data) => {
        if (err) {
            return res.status(500).json({ status: 'error', message: 'Error reading PDF file' });
        }
        pdf(data).then(result => {
            analyzeText(result.text, res);
        }).catch(err => {
            res.status(500).json({ status: 'error', message: 'Error processing PDF file' });
        });
    });
}

function processImageFile(filePath, res) {
    exec(`python scripts/process_image.py ${filePath}`, (err, stdout, stderr) => {
        if (err) {
            return res.status(500).json({ status: 'error', message: 'Error processing image file' });
        }
        analyzeText(stdout.trim(), res);
    });
}

function processAudioFile(filePath, res) {
    exec(`python scripts/process_audio.py ${filePath}`, (err, stdout, stderr) => {
        if (err) {
            console.error('Error executing Python script:', stderr); // Log the error output
            return res.status(500).json({ status: 'error', message: 'Error processing audio file', details: stderr });
        }
        analyzeText(stdout.trim(), res, filePath); // Pass filePath to analyzeText
    });
}

function processVideoFile(filePath, req, res) {
    const audioPath = filePath + '.wav';
    exec(`python scripts/convert_video_to_audio_moviepy.py ${filePath} ${audioPath}`, (err) => {
        if (err) {
            return res.status(500).json({ status: 'error', message: 'Error converting video to audio' });
        }
        exec(`python scripts/process_audio_speech_recognition.py ${audioPath}`, (err, stdout, stderr) => {
            if (err) {
                return res.status(500).json({ status: 'error', message: 'Error processing audio file' });
            }
            fs.unlinkSync(audioPath);  // Clean up audio file
            analyzeText(stdout.trim(), res);
        });
    });
}

function analyzeText(text, res, filePath) {
    const postData = JSON.stringify({ text });

    const options = {
        hostname: '127.0.0.1', // Use IPv4 loopback address
        port: 8000,
        path: '/analyze_text',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': postData.length
        }
    };

    const request = http.request(options, (response) => {
        let data = '';

        response.on('data', (chunk) => {
            data += chunk;
        });

        response.on('end', () => {
            if (response.statusCode === 200) {
                res.json({ status: 'success', type: 'audio', content: path.basename(filePath), analysis: JSON.parse(data) });
            } else {
                res.status(response.statusCode).json({ status: 'error', message: 'Error analyzing text', details: data });
            }
        });
    });

    request.on('error', (e) => {
        res.status(500).json({ status: 'error', message: `Problem with request: ${e.message}` });
    });

    request.write(postData);
    request.end();
}

module.exports = router;
