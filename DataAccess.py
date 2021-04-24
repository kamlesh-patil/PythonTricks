import socket #for ip address and hostname
#import speech_recognition as sr #to listen from mic
import pyautogui #for screen recording
import cv2 
import numpy as np 
import sounddevice as sd
from scipy.io.wavfile import write

    
def nameAndIP():
#it shows ip and hostname
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")

def recordAudio():
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('audiorecord.wav', fs, myrecording)  # Save as WAV file     
    
#def recordAudio():
#it takes microphone i/p input and returns string o/p
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#     print("Listening...")
#     r.pause_threshold = 1 # pause of number of seconds before completion of sentence
#     r.energy_threshold = 500 #loudness of i/p sound for silent room are 0 to 100, and typical values for speaking are between 150 and 3500.
#     audio = r.listen(source)
#     query = r.recognize_google(audio,language='en')
#     print(f"Usersaid: {query}\n")

def recordScreen():    
#to capture screen
    print(pyautogui.size()) #it shows resolution of your monitor
    resolution = (1366, 768) #my laptop resolution
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "screenrecord.avi" # Specify name of Output file
    fps = 60.0  #frame rate
    out = cv2.VideoWriter(filename, codec, fps, resolution) # Creating a VideoWriter object
#To display the recording in real-time, we have to create an Empty window and resize it.
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL) # Create an Empty window
    cv2.resizeWindow("Live", 480, 270) # Resize this window
#our screen recording will start it will run in infinite loop by taking screenshots continuesly and writing it in video file
    while True: #for linux we require scrot to use screenshot fucntions
        img = pyautogui.screenshot()# Take screenshot using PyAutoGUI
        frame = np.array(img)# Convert the screenshot to a numpy array
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert it from BGR(Blue, Green, Red) to RGB(Red, Green, Blue)
        out.write(frame) # Write it to the output file
        cv2.imshow('Live', frame)# Optional: Display the recording screen
        if cv2.waitKey(1) == ord('q'):# Stop recording when we press 'q'
            break
#after everything done
    out.release()# Release the Video writer
    cv2.destroyAllWindows()    # Destroy all windows

if __name__=="__main__":
    print("What do you want to do")
    print("1 for ip and user-name")
    print("2 for record voice")
    print("3 for capture screen")
    print("Enter any number between 1, 2 and 3")
    choice = input("Enter number: ")
    if(choice == "1"):
        nameAndIP()
    elif(choice == "2"):
        recordAudio()
    elif(choice=="3"):
        recordScreen()        
