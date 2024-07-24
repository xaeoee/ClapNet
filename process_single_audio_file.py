import numpy as np
import librosa

# Window size and other settings
window_duration = 0.6  # seconds
hop_length = 512  # hop length
window_size = None
minimum_distance = None
sr = None  # sampling rate
timstamps = []
def process_single_audio_file(file_path):
    global window_size, sr, minimum_distance

    y, sr = librosa.load(file_path, sr=None)  # Load audio file
    y_db = librosa.amplitude_to_db(np.abs(y), ref=np.max)  # Convert amplitude to decibels

    threshold_db = -30  # Threshold for detecting sound above noise.
    indices = np.where(y_db > threshold_db)[0]  # Find indices where sound is above threshold
    
    if window_size is None:
        window_size = int(window_duration * sr)  # Calculate window size in samples
        minimum_distance = int(0.6 * sr)  # Minimum distance between windows

    last_index = -minimum_distance  # Initialize last index

    X_Data = []

    for idx in indices:  # Iterate over detected indices
        if idx - last_index >= minimum_distance:  # Ensure minimum distance between windows
            start_idx = max(0, idx - window_size // 2)  # Calculate start index of window
            end_idx = min(len(y), idx + window_size // 2)  # Calculate end index of window
            y_window = y[start_idx:end_idx]  # Extract windowed audio segment
            S_window = librosa.feature.melspectrogram(y=y_window, sr=sr, n_mels=128, hop_length=hop_length)  # Create Mel spectrogram
            S_window_dB = librosa.power_to_db(S_window, ref=np.max)  # Convert power spectrogram to decibel units
            S_window_dB_normalized = (S_window_dB - np.min(S_window_dB)) / (np.max(S_window_dB) - np.min(S_window_dB))  # Normalize spectrogram

            # Check the size of the spectrogram and apply padding
            target_width = (window_size // hop_length) + 1  # Calculate target width of spectrogram
            if S_window_dB_normalized.shape[1] >= target_width:  # If spectrogram is smaller than target width
                X_Data.append(S_window_dB_normalized)  # Append normalized spectrogram to data list
                last_index = idx  # Update last index
                timstamps.append(idx/sr)
    return np.array(X_Data), timstamps