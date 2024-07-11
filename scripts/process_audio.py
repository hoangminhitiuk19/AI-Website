import sys
import io
import speech_recognition as sr

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.RequestError as e:
        return f"API request error: {e}"
    except sr.UnknownValueError:
        return "Error: Could not understand audio"
    except Exception as e:
        return f"General error: {e}"

if len(sys.argv) != 2:
    print("Usage: python process_audio.py <audio_path>")
    sys.exit(1)

audio_path = sys.argv[1]

transcription = transcribe_audio(audio_path)
print(transcription)
