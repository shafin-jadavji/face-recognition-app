# Face Recognition Project

This project is a Python-based face recognition application designed to help learn machine learning and artificial intelligence concepts while adhering to best coding practices. The project follows an iterative approach to allow for future enhancements and features.

---

## **Project Goals**

- Learn and implement face detection and recognition.
- Utilize Python libraries like OpenCV and DLIB.
- Follow best coding practices, such as modularity and extensibility.
- Build a foundation for adding advanced features like emotion detection and multi-face tracking.

---

## **Features**

### Current Features
1. **Face Detection (Static Images):**
   - Detect faces in a single image using OpenCV's Haar Cascade or DLIB libraries.

2. **Face Detection (Video Feed):**
   - Detect faces in real-time video using a webcam.

### Future Enhancements
- Add face recognition functionality with a database of known faces.
- Implement learning of new faces dynamically.
- Add support for group face recognition, emotion detection, and cloud integration.

---

## **Project Structure**

```bash
face_recognition_project/
├── data/                           # Test images, known faces, etc.
│   └── test_image.jpg
├── src/                            # Source code for the project
│   ├── detectors/                  # Detection-related logic
│   │   ├── opencv_detector.py
│   │   └── dlib_detector.py
│   ├── utils/                      # Utility functions
│   │   └── display.py
│   └── main.py                     # Entry point for the application
├── requirements.txt                # Dependencies list
├── .gitignore                      # Files to ignore in Git
├── README.md                       # Documentation
├── LICENSE                         # Project license
└── README.md                       # Describes the project
```

---

## **Setup and Usage**

### **1. Clone the Repository**
```bash
git clone https://github.com/shafin-jadavji/face-recognition-app.git
cd face-recognition-app
```
### **2. Set Up the Environment**
Create a virtual environment and install dependencies:

```bash
python -m venv face_env
source face_env/bin/activate  # On Windows, use face_env\Scripts\activate
pip install -r requirements.txt
```
### **3. Run the Application**
Static Image Detection: Add a test image to the data/ directory and run:

```bash
python src/main.py
```

Follow the prompts to select the image detection mode.

Video Feed Detection: Run the application and select video mode to use your webcam:

```bash
python src/main.py
```

---

## **Dependencies**
This project uses the following libraries:

- opencv-python: For image and video processing.
- numpy: For numerical operations.
- dlib (planned): For advanced face detection and recognition.

Install dependencies using:

```bash
pip install -r requirements.txt
```
---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---
