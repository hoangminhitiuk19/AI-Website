import speech_recognition as sr
import sys

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    try:
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.RequestError as e:
        return f"Error: {e}"
    except sr.UnknownValueError:
        return "Error: Could not understand audio"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_audio_speech_recognition.py <audio_path>")
        sys.exit(1)

    audio_path = sys.argv[1]
    transcription = transcribe_audio(audio_path)
    print(transcription)
