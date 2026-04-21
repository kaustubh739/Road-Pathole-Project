# Road Pothole Detection using CNN

## 📘 Description
This project detects potholes on roads using image processing and Convolutional Neural Networks (CNNs).  
It provides a Tkinter-based GUI for image selection, preprocessing, and prediction.  
The system integrates a login/registration module with SQLite for secure access.

## 🔑 Features
- User login and registration with SQLite database.
- Image selection and preprocessing (grayscale, thresholding).
- CNN-based classification of road images into "Pothole Detected" or "Normal Road".
- Tkinter GUI with buttons for image selection, preprocessing, prediction, and exit.
- Real-time video playback integration using `tkvideo`.

## ⚙️ Tech Stack
- **Language:** Python 3.11  
- **Libraries:** TensorFlow/Keras, Tkinter, Pillow (PIL), OpenCV, NumPy, scikit-learn, joblib, tkvideo, sqlite3  

## 🛠 Installation
Clone the repository and set up a virtual environment:
```bash
git clone <your-repo-link>
cd road_pothole_detection
python -m venv tf_env
tf_env\Scripts\activate
pip install -r requirements.txt

## 🚀 Usage
launch the main GUI:
python GUI_MASTER_old.py

📂 Dataset
~1300 pothole images collected for training and testing.

Images were preprocessed (resized, normalized) before CNN training to ensure consistent input.

Dataset balanced to address class imbalance between “pothole” and “normal road” categories.

📊 Results
Precision: 0.87

Recall: 0.89

Frames per second (FPS): 28

The modified CNN architecture outperformed Faster R-CNN baseline in accuracy and efficiency.
