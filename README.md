Project Documentation

Introduction

This document provides a comprehensive overview of the AI system designed to extract knowledge from various data sources (text, images, audio, and video) and build a comprehensive knowledge graph. The system is designed to enhance data retrieval processes through advanced analysis and visualization.

Project Overview

The primary goal of this project is to develop an AI-powered system that can process different file types, extract meaningful information, and build a knowledge graph to aid in data retrieval. The system supports text, image, audio, and video files, converting them into analyzable formats and displaying the results along with a visual knowledge graph.

Technology Stack

•	Frontend: HTML, CSS, JavaScript, Cytoscape.js
•	Backend: Python (FastAPI), Node.js (Express)
•	Database: Neo4j (for Knowledge Graph)
•	Libraries and Tools: spaCy, TextBlob, MoviePy, EasyOCR, SpeechRecognition, Multer, Mammoth, pdf-parse

System Architecture

The system follows a microservice architecture, divided into several key components:
1.	Frontend: Handles file uploads and displays results.
2.	Backend: Processes uploaded files and performs text analysis.
3.	Knowledge Graph Database: Stores entities and relationships extracted from the text.
   
Detailed Component Explanation

Frontend

•	index.html: Main interface for file upload and result display.
•	styles.css: Styling for the frontend components.
•	JavaScript Functions: Handles file upload, shows progress, and renders the knowledge graph.

Backend

•	upload.js: Node.js script to handle file uploads and pre-processing.
•	text_analysis_service.py: FastAPI service for analyzing text and interacting with the knowledge graph.
•	scripts/:
o	text_analysis.py: Contains functions for text entity extraction, sentiment analysis, and summarization.
o	process_image.py: Processes images and extracts text using EasyOCR.
o	process_audio.py: Transcribes audio files using Speech-to-Text.
o	process_audio_speech_recognition.py: Alternative script for audio transcription using SpeechRecognition library.
o	convert_video_to_audio_moviepy.py: Converts video files to audio format using MoviePy.

Data Flow

1.	File Upload: Users upload files through the frontend.
2.	Pre-processing: The backend processes the file based on its type (text, image, audio, video).
3.	Text Analysis: Extracted or uploaded text is analyzed for entities, sentiment, and summarization.
4.	Knowledge Graph: Entities and relationships are stored in Neo4j and visualized using Cytoscape.js.
   
Knowledge Graph

The knowledge graph represents entities and their relationships, enhancing data retrieval and providing visual insights into the analyzed text. It is built using:
•	Entities: Extracted from text using spaCy.
•	Relationships: Determined based on co-occurrence and context.

Installation and Setup

1.	Clone the Repository: git clone <repository-url>
2.	Install Dependencies:
o	Python: pip install -r requirements.txt
o	Node.js: npm install
3.	Run Neo4j: Ensure Neo4j is running on localhost:7687.
4.	Start Backend Services:
o	FastAPI: uvicorn text_analysis_service:app --host 0.0.0.0 --port 8000
o	Node.js: npm run start
5.	Access Frontend: Open index.html in a browser.
   
Usage Instructions

1.	Open the web interface.
2.	Upload a file (text, image, audio, video).
3.	Wait for the file to be processed.
4.	View the extracted text, analysis results, and the knowledge graph.
   
API Endpoints

•	/upload: Handles file uploads.
•	/analyze_text: Analyzes the provided text and returns entities, sentiment, and summary.

Challenges and Solutions

•	Slow Audio Processing: Optimized by providing progress feedback.
•	Knowledge Graph Rendering Errors: Ensured data validity and added error handling.

Future Enhancements

•	Support for More File Types: Expand to other formats like CSV, Excel.
•	Real-time Processing: Improve speed and feedback for users.
•	Advanced Relationship Extraction: Use NLP techniques for more accurate relationship mapping.

Conclusion

This AI system effectively processes various data types, extracts meaningful information, and builds a knowledge graph to enhance data retrieval. The microservice architecture and use of advanced libraries ensure scalability and efficiency.

