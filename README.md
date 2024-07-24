
# Clap Detection Using CNN
## **I.** Description
This project processes audio files to detect clapping sounds using Convolutional Neural Networks (CNN). Input video file will be converted into the audio files and then converted into mel-spectrograms and saved as numpy arrays for training the CNN model.
The output will be json format file contianing metadata of video file with timestamps of clap detected.
By using this programe, reviwer can easily find clapping which could be abnormal behaviour of ASD child.

## II. Environment Set-up

### Step1. Download this python script
Use `git clone` or directly download.
Go to https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=644 and download appropriate data(sound data for human)
Then you can get a below hierarchy.
```
CLAPNET/
├── data/
│   └── 174.자연 및 인공적 발생 비언어적 소리 데이터/
│       ├── 1.Training/
│           ├── 라벨링데이터/
│           ├── 원천데이터/
│               └── TS_3.사람/
│                   ├── 1.생리현상/
│                   ├── 2.신체를 이용한 인위적 소리/
│                   ├── 3.감정/
│                   └── 4.이동감지/
│                   └── TS_3.사람.zip
│       ├── 2.Validation/
│           ├── 라벨링데이터/
│           ├── 원천데이터/
│               └── VS_3.사람/
│                   ├── 1.생리현상/
│                   ├── 2.신체를 이용한 인위적 소리/
│                   ├── 3.감정/
│                   └── 4.이동감지/
│                   └── VS_3.사람.zip
│       ├── behavior_data.json
│       ├── combined_data.json
│       └── metadata.json
├── video/
├── .gitignore
├── convert.py
├── data_preprocessing.ipynb
├── environment.yml
├── main.py
├── metadata.py
├── my_model.keras
├── process_single_audio_file.py
├── README.md
├── timestamps.py
```

### Step2. Create anaconda virtual environment
```
conda env create -f environment.yml
```

### Step3. Run & test
```
(CLAPNET) python3 main.py --video_path video/your_video.mp4
```

## III. Requirements
```
python=3.12.4
opencv-python==4.10.0
numpy==1.26.4
tqdm==4.66.4
librosa==0.10.2.post1
matplotlib==3.8.4
pandas==2.2.2
tensorflow==2.16.2
scikit-learn==1.4.2
moviepy==1.0.3
```
