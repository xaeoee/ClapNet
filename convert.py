from moviepy.editor import VideoFileClip

def convertMp4toMp3(video_path):
    # MP4 파일 경로
    mp4_file_path = video_path
    # 저장할 MP3 파일 경로
    mp3_file_path = 'audio.mp3'

    # 비디오 파일 읽기
    video = VideoFileClip(mp4_file_path)

    # 오디오 추출
    audio = video.audio

    # 오디오 파일로 저장
    audio.write_audiofile(mp3_file_path, codec='mp3')

    print(f"Audio has been successfully extracted and saved as {mp3_file_path}")

    return mp3_file_path