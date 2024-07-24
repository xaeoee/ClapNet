import json
import os
import moviepy.editor as mp

def extract_metadata(input_file):
    clip = mp.VideoFileClip(input_file)
    metadata = {
        "duration": clip.duration,
        "fps": clip.fps,
        "size": clip.size,
    }
    clip.close()
    return metadata

def save_metadata_as_json(metadata, output_file):
    output_path = os.path.join('data', output_file)

    with open(output_path, 'w') as file:
        json.dump(metadata, file, indent=4)

def initial_metadata_setup(video_path):
    metadata = extract_metadata(video_path)
    save_metadata_as_json(metadata, "metadata.json")
    return metadata

def file_generating(video_path, timestamps):
    metadata = initial_metadata_setup(video_path)
    behavior_data = []

    for time in timestamps:
        clap_detected_time = {
                                        "timestamp": time,
                                        "behavior_type": 'clap'
                                    }
        behavior_data.append(clap_detected_time)

    output_path = os.path.join('data', 'behavior_data.json')

    with open(output_path, 'w') as file:
        json.dump(behavior_data, file, indent=4)

    # merge metadta and behavior data.
    combined_data = {
        "metadata": metadata,
        "behavior_data": behavior_data
    }
    # save it under data directory.
    output_path = os.path.join('data', 'combined_data.json')
    with open(output_path, 'w') as file:
        json.dump(combined_data, file, indent=4)