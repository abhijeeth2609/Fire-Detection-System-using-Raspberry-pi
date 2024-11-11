
# Fire-Detection-System-using-Raspberry-Pi
# Overview
The Fire Detection System is designed to provide real-time fire monitoring using computer vision techniques implemented on a Raspberry Pi. This system aims to enhance safety by quickly detecting fires and triggering appropriate alerts and responses.

# Project Motivation
Detecting fires promptly is critical to minimizing risks to life and property. Traditional smoke detectors and thermistors often respond too slowly. Our project addresses this by using image processing to identify fire visually and react faster than conventional sensors.

#  Key Features
Real-time image capture and analysis using OpenCV.
Conversion of images to HSV color space for improved fire detection accuracy.
Adaptive thresholding to isolate and identify fire-like regions in images.
Event logging for monitoring and future analysis.
Tiered response strategy:
Fire alarm activated after 10 seconds of continuous detection.
Water sprinkler system triggered at 30 seconds.
Emergency services notified after 60 seconds.
# System Requirements

   Software
   
   Python with OpenCV: For image processing and analysis.
Raspberry Pi OS: The primary operating system for running the detection software.

   Hardware
   
Raspberry Pi 4B: Chosen for its processing power and versatility.
Web Camera: Captures images for analysis.
# How It Works
Initialization: The Raspberry Pi starts capturing frames at one-second intervals.
Image Processing: Captured images are converted from BGR to HSV color space. A binary mask is applied to highlight fire regions.
Detection Logic:
The system calculates fire coverage based on the binary mask.
If the fire persists, responses escalate from alarms to activating sprinklers and notifying fire services.
Logging: Events, including detection times and responses, are recorded for review.
# Challenges and Future Enhancements
  Current Challenges:
  
Determining optimal HSV thresholds for various fire conditions.
Ensuring reliable Raspberry Pi-to-computer interfacing.

Future Scope:

Integration of location and image transmission to aid responders.
Implementation of a rotating camera for broader coverage.
