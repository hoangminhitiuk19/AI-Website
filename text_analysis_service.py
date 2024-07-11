from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scripts.text_analysis import analyze_text
import logging

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # Your frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class TextData(BaseModel):
    text: str

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.post("/analyze_text")
async def analyze_text_endpoint(data: TextData):
    try:
        text = data.text
        logging.info(f"Received text for analysis: {text}")
        result = analyze_text(text)
        logging.info(f"Analysis result: {result}")
        return result
    except Exception as e:
        logging.error(f"Error analyzing text: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
