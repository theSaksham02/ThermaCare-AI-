# 🌡️ ThermaCare AI

NeoTherm AI is a low-cost, non-invasive thermoregulation monitoring system for neonatal care, developed for the **Incubate National MedTech Hackathon**. It combines thermal image processing with Google’s **Gemma AI** model to deliver dynamic clinical support, caregiver guidance, and automated shift handovers — especially optimized for **resource-limited environments**.

## 🧰 Tech Stack & Tools Used

<p align="center">
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  </a>
  <a href="https://opencv.org/" target="_blank">
    <img src="https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV Badge" />
  </a>
  <a href="https://aistudio.google.com/" target="_blank">
    <img src="https://img.shields.io/badge/Gemma%20AI-34a853?style=for-the-badge&logo=google&logoColor=white" alt="Gemma AI Badge" />
  </a>
  <a href="https://www.tensorflow.org/lite" target="_blank">
    <img src="https://img.shields.io/badge/TensorFlow%20Lite-ff6f00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TFLite Badge" />
  </a>
  <a href="https://www.flir.com/" target="_blank">
    <img src="https://img.shields.io/badge/FLIR%20Camera-1a1a1a?style=for-the-badge&logo=data:image/svg+xml;base64,&logoColor=white" alt="FLIR Badge" />
  </a>
</p>


## 🚀 Overview

> **NeoTherm AI** detects neonatal temperature abnormalities (e.g., **hypothermia** or **hyperthermia**) using a low-cost thermal camera and suggests **AI-powered clinical actions** in real time. It also provides:
- **Multi-lingual caregiver instructions**
- **Automated shift summaries**
- **In-app video tutorials**

**Team**  
- 👨‍💻 Saksham Mishra | University of Birmingham | Engineering Student  
- 🩺 Dr. Ashi Soni | Lady Hardinge Medical College | Medical Student  
📩 **Contact**: sakshammishra0205@gmail.com

---

## 🔧 Features
NeoTherm AI integrates real-time thermal monitoring, clinical intelligence, caregiver support, and automation in a compact, affordable system. Here’s what it does:

---

### 🌡️ Thermal Image Processing

- Captures thermal images using a **FLIR Lepton sensor** or simulated grayscale images.
- Uses **OpenCV** to process thermal maps, analyze heat distribution, and detect anomalies.
- Identifies key body regions (e.g., **chest, feet, hands**) and labels risks:
  ```json
  {
    "status": "Hypothermia Risk Detected",
    "affected_area": "feet and hands"
  }
Outputs structured diagnostic data in real time for further processing.

### 🤖 AI-Powered Clinical Action Plans (Gemma)
- Connects to Google’s Gemma model to dynamically generate 3-step action plans.
- Context-aware decision-making based on detected conditions (e.g., hypothermia, hyperthermia).
Example:
1. Initiate Kangaroo Mother Care.
2. Cover with thermal wrap.
3. Reassess in 30 minutes.
Ensures clinically guided interventions in resource-constrained environments.

### 🌍 Multi-Lingual Caregiver Communication
- Converts medical action plans into empathetic and simplified language for caregivers.
- Supports multiple local languages (e.g., Hindi, Tamil).
Example:
- Medical: Hypothermia Risk Detected.
- Translated: चिंता न करें। आपके बच्चे को थोड़ा ठंडा लग रहा है। कृपया उसे अपनी छाती से लगाकर गर्म रखें।

Bridges the gap between healthcare workers and families with culturally sensitive messaging.

### 📝 Automated Shift Handover Summaries
- Generates concise, timestamped summaries of each infant’s thermal status and treatment response.

Example:
- Shift Summary: Infant A1 stable. Hypothermia detected at 10:30 AM, resolved by 11:15 AM with Kangaroo Care.

Reduces manual reporting and streamlines clinical shift transitions.

### 🎥 Embedded Video Tutorials
- Includes five 30-second video guides on neonatal emergency procedures.
- Videos are accessible via GUI buttons or stored locally in the tutorials/ folder.
- Topics include:
    - Kangaroo Mother Care
    - Emergency temperature response
    - Device usage guide
Ideal for on-the-spot caregiver training in NICU settings

## 📁 Datasets
- Due to privacy laws, no real neonatal images are used. Instead:

### 🧪 Simulated Dataset
- 35 images generated using OpenCV colormaps on grayscale baby doll photos.

- Labels: Normal, Hypothermic, Early Hypothermic.

- Generated with create_dataset.py.

## 📚 Public Datasets Used
- Dataset	Use	License
- C3I Thermal Automotive (IEEE Dataport)	Torso/limb temperature proxies	Non-commercial
- Thermal Dogs & People (Roboflow)	Object detection training	Public Domain
- FLIR Thermal Dataset	Vision & thermal calibration	Teledyne FLIR (non-commercial)
- UNIRI-TID (IEEE Dataport)	Human thermal label reference	Non-commercial

## Install dependencies
**pip install -r requirements.txt**
**Dependencies:**
- opencv-python
- matplotlib
- requests
- numpy
- tkinter

🧾 Code Structure
File/Folder	Description
thermal_processor.py	Loads and processes thermal images with OpenCV
create_dataset.py	Generates simulated thermal dataset
gemma_integration.py	Connects to Google Gemma API
gui_display.py	Builds the Tkinter interface
main.py	Central controller to run everything
tutorials/	Stores instructional videos
datasets/	All training/testing thermal image data


## 📜 License
This project is licensed under the MIT License. See LICENSE for full terms.

## 🗂 Dataset Licenses
##### C3I Dataset: IEEE Dataport (Non-commercial)

##### Thermal Dogs/People: Roboflow (CC0)

##### FLIR Dataset: Teledyne FLIR (Non-commercial)

##### UNIRI-TID: IEEE Dataport (Non-commercial)

##### Simulated Dataset: © Team (MIT)

## 🖼 Image & Video Rights
All simulated images are team-created and under MIT License.
Tutorial videos are original and licensed under MIT.
No real neonatal data is used or included.

## ⚠️ Disclaimer
_**This system is a proof-of-concept for a Hackathon.**_
_**It is not certified for clinical or real-world use. AI-generated outputs (e.g., summaries, translations) must be validated by licensed professionals.**_

## 🙏 Acknowledgments
#### 🧪 Incubate Hackathon: Platform for innovation

#### 🧠 Google AI Studio: For access to Gemma

#### 📊 Dataset Providers: IEEE, Roboflow, Teledyne FLIR

## 📬 Contact
For questions, collaborations, or suggestions:
📧 sakshammishra0205@gmail.com
💻 GitHub: @theSaksham02
