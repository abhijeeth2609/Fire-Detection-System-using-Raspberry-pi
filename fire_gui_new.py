import cv2
import numpy as np
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from datetime import datetime

fire_start_time = None
def detect_fire(frame, fire_threshold=0):
    global fire_start_time
    frame = cv2.resize(frame, (480, 270))  # Adjust size for full-screen or as needed
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv_frame = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    #lower_threshold = np.array([0, 74, 200],dtype="uint8")
    #upper_threshold = np.array([18, 166, 230],dtype="uint8")

    #lower_threshold = np.array([18, 30, 150],dtype="uint8")
    #upper_threshold = np.array([35, 255, 255],dtype="uint8")

    lower_threshold = np.array([5, 44, 228],dtype="uint8")
    upper_threshold = np.array([25, 255, 255],dtype="uint8")

    #lower_threshold = np.array([10, 100, 20],dtype="uint8")
    #upper_threshold = np.array([25, 255, 255],dtype="uint8")

    #lower_threshold = np.array([18, 50, 50],dtype="uint8")
    #upper_threshold = np.array([35, 255, 255],dtype="uint8")
    mask = cv2.inRange(hsv_frame, lower_threshold, upper_threshold)
    fire_coverage = np.count_nonzero(mask) / (mask.shape[0] * mask.shape[1])
    if fire_coverage > fire_threshold:
        if fire_start_time is None:
            fire_start_time = datetime.now()
        # Calculate the duration of continuous fire detection
        duration = datetime.now() - fire_start_time
        duration=int(duration.total_seconds())
        if duration == 10:
            fo=open(r"data.txt", "a")
            fo.write("\n FIRE ALARM ON! ")
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            fo.write(current_time)
            fo.close()
        elif duration == 20 :
            fo=open(r"data.txt", "a")
            fo.write("\n WATER SPRINKLER ON! ")
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            fo.write(current_time )
            fo.close()
        #elif duration == 30 :
           # fo=open(r"data.txt", "a")
           # fo.write("\n POWER OFF! ")
           #current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           #fo.write(current_time )
           #fo.close()
        elif duration == 30:
            fo = open(r"data.txt", "a")
            fo.write("\n CALL FOR FIRE AID! ")
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            fo.write(current_time)
            fo.close()
        else:
           status_label.config(text=f"Fire Detected! (Coverage: {fire_coverage * 100:.2f}%)", font=fire_font)
           current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           fo = open(r"data.txt", "a") # safer than w mode
           fo.write("\nfire detected : ")
           fo.write(current_time)
           fo.write("\n")
           fo.close()
    else:
        fire_start_time = None
        status_label.config(text="No Fire Detected.", font=default_font)

    result_frame = cv2.bitwise_and(frame, frame, mask=mask)
    return frame, result_frame

def update_display(original_frame, result_frame):
    rgb_original = cv2.cvtColor(original_frame, cv2.COLOR_BGR2RGB)
    img_original = ImageTk.PhotoImage(image=Image.fromarray(rgb_original))
    rgb_result = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)
    img_result = ImageTk.PhotoImage(image=Image.fromarray(rgb_result))

    original_video_label.img = img_original
    original_video_label.config(image=img_original)
    result_video_label.img = img_result
    result_video_label.config(image=img_result)

def capture_frame():
    ret, frame = cap.read()
    if ret:
        original_frame, result_frame = detect_fire(frame)
        update_display(original_frame, result_frame)
    else:
        status_label.config(text="Error: Could not read frame.", font=default_font)

def handle_detection():
    capture_frame()
    window.after(1000, handle_detection)  # Wait for 2 seconds before capturing the next frame

def start_detection(event):
    global cap
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        status_label.config(text="Error: Could not open camera.", font=default_font)
        return
    status_label.config(text="Fire detection started.", font=default_font)
    handle_detection()

def stop_detection(event):
    if cap.isOpened():
        cap.release()
    window.quit()



window = tk.Tk()
window.title("Fire Detection")




#def toggle_fullscreen(event=None):
    #window.attributes("-fullscreen", not window.attributes("-fullscreen"))

#def exit_fullscreen(event=None):
    #window.attributes("-fullscreen", False)
# Start in full-screen mode
#window.attributes("-fullscreen", True)
#window.bind("<F11>", toggle_fullscreen)
#window.bind("<Escape>", exit_fullscreen)



window.focus_set()
window.bind('<Return>', start_detection)
window.bind('<space>', stop_detection)

default_font = font.Font(family="Helvetica", size=30)
fire_font = font.Font(family="Helvetica", size=16, weight="bold")

original_video_label = tk.Label(window)
original_video_label.pack(side=tk.LEFT)

result_video_label = tk.Label(window)
result_video_label.pack(side=tk.RIGHT)

status_label = tk.Label(window, text="Press 'Enter' to start detection, 'Space' to exit.", font=default_font)
status_label.pack()

window.mainloop()
