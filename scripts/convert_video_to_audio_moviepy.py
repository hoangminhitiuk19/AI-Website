from moviepy.editor import VideoFileClip

def convert_video_to_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_video_to_audio_moviepy.py <video_path> <audio_path>")
        sys.exit(1)

    video_path = sys.argv[1]
    audio_path = sys.argv[2]
    convert_video_to_audio(video_path, audio_path)
