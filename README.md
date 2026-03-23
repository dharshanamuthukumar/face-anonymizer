# 🎭 Face Anonymizer (Real-Time)

A simple and efficient **real-time face anonymization system** that detects human faces using OpenCV and automatically blurs them to protect identity and privacy.

---

## 📌 Overview

This project captures live video from a webcam, detects faces in each frame, and applies a blur effect to anonymize them. It is lightweight, fast, and suitable for beginners exploring computer vision.

---

## 🚀 Features

- 📷 Real-time webcam capture
- 🧠 Face detection using Haar Cascade
- 🎭 Automatic face blurring
- ⚡ Fast and lightweight implementation
- 🛠 Easy to set up and run

---

## 🧰 Tech Stack

- **Language:** Python
- **Library:** OpenCV

---

## 📂 Project Structure

```
face-anonymizer/
│── main.py          # Main script for face detection and blurring
│── README.md        # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/face-anonymizer.git
cd face-anonymizer
```

### 2. Install dependencies

```bash
pip install opencv-python
```

---

## ▶️ Usage

Run the following command:

```bash
python main.py
```

### 🎮 Controls

- Press **`q`** to quit the application

---

## 🧠 How It Works

1. Captures video from the webcam
2. Converts each frame to grayscale
3. Detects faces using Haar Cascade classifier
4. Extracts face regions
5. Applies Gaussian blur to those regions
6. Displays the processed video in real-time

---

## ⚡ Customization

You can adjust the blur intensity in `main.py`:

```python
blurred_face = cv2.GaussianBlur(face, (99, 99), 30)
```

- Increase kernel size → stronger blur
- Decrease kernel size → lighter blur

---

## ⚠️ Requirements

- Python 3.x
- Working webcam
- OpenCV installed

---

## 🚧 Future Enhancements

- 🔍 Use deep learning models (DNN / YOLO) for better accuracy
- 🎨 Add pixelation instead of blur
- 🎥 Support video file input
- 🧑‍🤝‍🧑 Multi-face tracking improvements

---

## 👩‍💻 Author

**Dharshana**

---

## 📜 License

This project is open-source and free to use for learning purposes.
