from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip

def get_video_quality_options(yt):
    video_streams = yt.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').desc()
    audio_streams = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc()
    quality_options = [(stream, stream.resolution) for stream in video_streams] + [(stream, f"{stream.abr} (audio only)") for stream in audio_streams]
    return quality_options

def download_stream(stream, output_path, filename):
    stream.download(output_path=output_path, filename=filename)

def download_and_merge(video_stream, audio_stream, output_path, output_name):
    video_path = f"{output_path}/{output_name}_video.mp4"
    audio_path = f"{output_path}/{output_name}_audio.mp4"

    video_stream.download(output_path=output_path, filename=f"{output_name}_video.mp4")
    audio_stream.download(output_path=output_path, filename=f"{output_name}_audio.mp4")

    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(f"{output_path}/{output_name}.mp4", codec='libx264')

    video_clip.close()
    audio_clip.close()
    final_clip.close()

    # Remove temporary files
    import os
    os.remove(video_path)
    os.remove(audio_path)

def main():
    url = input("Enter the YouTube video URL: ")
    yt = YouTube(url)
    
    print("Available options:")
    print("1. Video")
    print("2. Audio")
    option = int(input("Enter the number corresponding to the desired option: "))

    output_path = input("Enter the path to save the file (leave empty for current directory): ").strip() or "."
    output_name = input("Enter the desired name for the file (leave empty for default): ").strip() or yt.title

    if option == 2:
        # Audio option
        print("Available audio quality options:")
        audio_options = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc()
        for idx, stream in enumerate(audio_options, start=1):
            print(f"{idx}. {stream.abr}")

        choice = int(input("Enter the number corresponding to the desired quality: "))
        selected_stream = audio_options[choice - 1]

        download_stream(selected_stream, output_path, f"{output_name}.mp4")
        print("Audio downloaded successfully!")
    else:
        # Video option
        print("Available video quality options:")
        quality_options = get_video_quality_options(yt)
        for idx, (_, quality) in enumerate(quality_options, start=1):
            print(f"{idx}. {quality}")

        choice = int(input("Enter the number corresponding to the desired quality: "))
        selected_stream, selected_quality = quality_options[choice - 1]

        if 'audio only' in selected_quality:
            download_stream(selected_stream, output_path, f"{output_name}.mp4")
            print("Audio downloaded successfully!")
        else:
            video_stream = selected_stream
            audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
            download_and_merge(video_stream, audio_stream, output_path, output_name)
            print("Video downloaded successfully!")

if __name__ == "__main__":
    main()

