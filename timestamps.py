from tensorflow import keras
import numpy as np

def get_clap_timestamps(model_path, X_Data, timestamps):
    model = keras.models.load_model(model_path)

    # Reshape X_Data to 4D if necessary (assuming it's a 3D array)
    X_Data = X_Data.reshape(X_Data.shape[0], X_Data.shape[1], X_Data.shape[2], 1)

    # Perform predictions
    predictions = model.predict(X_Data)

    # Predict classes for each window
    predicted_classes = np.argmax(predictions, axis=1)
    # Determine the final prediction based on the most common predicted class
    final_prediction = max(set(predicted_classes), key=list(predicted_classes).count)
    label_map = {0: 'clap', 1: 'non_clap'}  # Update this according to your label mapping used during model training
    final_label = label_map[final_prediction]

    # Assuming timestamps is a list of timestamps corresponding to X_Data
    if final_label == 'clap':
        # Create a new list excluding timestamps where the predicted class is 'non_clap'
        timestamps = [timestamp for idx, timestamp in enumerate(timestamps) if predicted_classes[idx] != 1]

        timestamps = [round(timestamp, 1) for timestamp in timestamps]
    else:
        return []    
    return timestamps