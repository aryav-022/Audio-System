from tkinter import *
from playsound import playsound
from functools import partial
from threading import Thread
import numpy as np
import os, wave


def visualize(path :str):
    raw = wave.open(path)
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype="int16")
    signal = signal.tolist()
    
    f_rate = raw.getframerate()
    time = np.linspace(0, len(signal) / f_rate, num=len(signal))
    time = time.tolist()
    
    for i in range(1, len(time)):
        graph.create_line(int(time[i-1]*100), int(400+signal[i-1]/10), int(time[i]*100), int(400+signal[i]/10))
        graph.update()
    

def play(relative_path):
    path = "Audio System\\" + relative_path
    print(path)
    # Thread(target=playsound, args=(path, )).start()
    visualize(path)
    

if __name__ == '__main__':
    directory = os.listdir(".\Audio System")
    audio_files = []
    test = False
    
    for sub_directory in directory:
        if sub_directory.split(".")[-1] in ["wav", "mp3"]:
            audio_files.append(sub_directory)
        
    root = Tk()
    root.title("MP3 Player")
    
    button_frame = Frame(root)
    button_frame.pack(side=LEFT, anchor=NW)
    
    graph = Canvas(root, height=800, width=800)
    graph.pack(side=RIGHT, anchor=NE)

    for audio_file in audio_files:
        Button(button_frame, text=audio_file, width=30, cursor="hand2", command=partial(play, audio_file)).pack()

    root.mainloop()