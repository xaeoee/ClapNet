import argparse
from process_single_audio_file import *
from timestamps import *
from tensorflow import keras
from convert import *
from metadata import *

def main():
    parser = argparse.ArgumentParser(description='Clap Detection')
    # Adding a new argument '--video_path'.
    parser.add_argument('--video_path', type=str, default='video/head_banging_video/headbanging.mp4', help='Path to the video file (default: video/head_banging_video/headbanging.mp4)')
    # A variable that stores the parsed arguments.
    args = parser.parse_args()
    # Retreieve string from '--video_path'
    video_path = args.video_path
    # Pass the video path as an argument.
    
    audio_path = convertMp4toMp3(video_path)
    
    X_Data ,timestamps = process_single_audio_file(audio_path)

    timestamps = get_clap_timestamps('my_model.keras', X_Data, timestamps)

    file_generating(video_path, timestamps)

    print("Data has been generated.")

if __name__ == "__main__":
    main()
