# self-driving-car-

🚘 Self-Driving Car Simulation using NLP & Computer Vision
✨ An Intelligent Autonomous Driving System with Real-Time Decision Making & Natural Language Understanding
🔍 Project Description
This project demonstrates an advanced Self-Driving Car Simulation that blends the power of Natural Language Processing (NLP) and Computer Vision (CV) to create a smarter, more adaptive autonomous driving experience.

By interpreting user instructions through NLP, the vehicle can understand and respond to real-time commands like “slow down at the intersection” or “turn right after the stop sign.” Meanwhile, CV algorithms, powered by YOLO and CNNs, enable object recognition, lane detection, and obstacle avoidance — all orchestrated within a seamless driving simulation.

✅ Developed with Python, TensorFlow, PyTorch, and Streamlit, this system offers a fully interactive testing environment for research, education, and innovation.


🧠 Core Features
🗣 Natural Language Understanding
• Understands spoken/text instructions
• Converts language into real-time driving behaviors


👁 Computer Vision Intelligence
• Detects traffic signs, pedestrians, vehicles, and lanes
• Uses YOLO and CNNs for fast and accurate recognition


🛞 Smart Navigation & Steering
• Predicts optimal steering angle from lane data
• Measures distance to obstacles for safe maneuvering


📊 Interactive Dashboard (Streamlit)
• Live camera feed with object annotations
• Real-time telemetry, control logs, and command input


🔐 Secure Login + Alerts
• Authenticated access using streamlit-login-auth-ui
• Notifications sent via trycourier API


⚙️ Technology Stack
Programming Language: Python
Frameworks: TensorFlow (CPU), PyTorch
Computer Vision: OpenCV, YOLO (Ultralytics)
Dashboard: Streamlit
Security: Argon2-CFFI
Notification Service: TryCourier


📦 Dependencies
makefile
Copy
Edit
tensorflow-cpu==2.17.0  
opencv-python  
ultralytics  
streamlit==1.35.0  
streamlit-login-auth-ui==0.2.0  
trycourier==4.2.0  
argon2-cffi==23.1.0  

🚀 How to Run
Clone the repository
Create a virtual environment and activate it
Install dependencies using pip install -r requirements.txt

Run the application:
bash
Copy
Edit
streamlit run app.py
Access the dashboard and start giving driving commands!


💡 Use Case Scenarios
Simulate realistic urban driving with voice commands
Academic research on multi-modal AI (vision + language)

Teach and demonstrate core concepts of autonomous systems

Expand into real-world hardware for robotics or automotive platforms

📜 License & Contribution
This project is licensed under the MIT License. Contributions, forks, and feature suggestions are always welcome!
