# self-driving-car-

```markdown
# Self-Driving Car Simulation with NLP & Computer Vision

A comprehensive self-driving car simulation that combines Natural Language Processing (NLP) and Computer Vision (CV) to enable dynamic command interpretation, precise steering control, and real-time obstacle recognition. Built with Python, TensorFlow, PyTorch, and powered by Streamlit for an interactive web interface, this project provides an end-to-end environment for developing and testing autonomous vehicle behaviors.

---

## 🚗 Project Overview

Modern autonomous vehicles must not only perceive their surroundings but also understand and respond to human instructions. This simulation integrates:

- **NLP Module**  
  - Leverages transformer-based models to parse driving commands and contextual cues  
  - Dynamically adjusts speed, steering, and route based on natural language inputs

- **Computer Vision Module**  
  - Implements Convolutional Neural Networks (CNNs) and the YOLO object detector to identify lanes, traffic signs, pedestrians, and obstacles  
  - Calculates object distances for safe navigation and collision avoidance

- **Control & Decision Fusion**  
  - Merges steering angle prediction (from lane detection) with distance-based safety checks  
  - Orchestrates multiple modules to produce smooth, realistic vehicle behaviors

- **Interactive Simulation Interface**  
  - Streamlit-based dashboard for real-time visualization of camera feeds, detected objects, and control signals  
  - User authentication and notification integration for collaborative testing

---

## 🔧 Key Features

- **Natural Language Command Processing**  
  Translate voice/text instructions into actionable control signals.
- **Real-Time Object Detection**  
  Detect and classify on-road elements using YOLOv8.
- **Lane Detection & Steering Prediction**  
  Estimate curvature and generate safe steering angles.
- **Distance Measurement**  
  Compute real-world distances to obstacles for collision avoidance.
- **Modular Architecture**  
  Separate, interchangeable components for NLP, CV, and control logic.
- **Web-Based Dashboard**  
  Streamlit app with login, live video stream, telemetry, and alert notifications.

---

## 🛠️ Tech Stack

- **Languages & Frameworks**  
  - Python 3.8+  
  - TensorFlow (CPU) 2.17.0  
  - PyTorch  
  - OpenCV  
  - Ultralytics YOLO  

- **Web & UI**  
  - Streamlit 1.35.0  
  - streamlit-login-auth-ui 0.2.0  

- **Utility & Authentication**  
  - trycourier 4.2.0 (notification delivery)  
  - argon2-cffi 23.1.0 (secure password hashing)

---

## 📥 Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/self-driving-nlp-cv.git
   cd self-driving-nlp-cv
   ```

2. **Create a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**  
   Create a `.env` file at the project root with:  
   ```dotenv
   COURIER_API_KEY=<your_trycourier_api_key>
   ```

---

## ▶️ Usage

1. **Run the Streamlit app**  
   ```bash
   streamlit run app.py
   ```

2. **Interact with the dashboard**  
   - **Login:** Enter your credentials.  
   - **Live Feed:** View camera stream with overlaid detections.  
   - **Command Panel:** Type or speak driving instructions.  
   - **Telemetry:** Monitor speed, steering angle, and obstacle distances.  

---

## 📄 Requirements

```text
tensorflow-cpu==2.17.0
opencv-python
ultralytics
streamlit==1.35.0
streamlit-login-auth-ui==0.2.0
trycourier==4.2.0
argon2-cffi==23.1.0
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Please:

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m 'Add some feature'`)  
4. Push to the branch (`git push origin feature/YourFeature`)  
5. Open a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---
```
