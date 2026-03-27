import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading

# try sound (if it fails, just beep in console)
try:
    import pygame
    import numpy as np
    pygame.mixer.init()
    has_sound = True
except:
    has_sound = False


# simple sound generator
def make_beep():
    if not has_sound:
        return None

    sr = 44100
    dur = 0.3

    t = np.linspace(0, dur, int(sr * dur), False)
    tone = np.sin(2 * np.pi * 880 * t)

    # fade a bit so it doesn't sound harsh
    tone = tone * (1 - t / dur)

    tone = (tone * 32767).astype(np.int16)
    tone = np.column_stack((tone, tone))

    return pygame.sndarray.make_sound(tone)


def play_sound(flag):
    snd = make_beep()

    while True:
        if flag.is_set():
            break

        if snd:
            snd.play()
        else:
            print('\a', end='', flush=True)

        time.sleep(0.5)


class AlarmApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Alarm")

        self.alarms = []
        self.stop_flag = threading.Event()
        self.ringing = False

        # ---- clock labels ----
        self.time_lbl = tk.Label(root, font=("Arial", 40))
        self.time_lbl.pack(pady=10)

        self.date_lbl = tk.Label(root)
        self.date_lbl.pack()

        # ---- input section ----
        frame = tk.Frame(root)
        frame.pack(pady=10)

        self.h = tk.StringVar(value="07")
        self.m = tk.StringVar(value="00")
        self.s = tk.StringVar(value="00")

        tk.Spinbox(frame, from_=0, to=23, width=3,
                   textvariable=self.h, format="%02.0f").grid(row=0, column=0)

        tk.Spinbox(frame, from_=0, to=59, width=3,
                   textvariable=self.m, format="%02.0f").grid(row=0, column=1)

        tk.Spinbox(frame, from_=0, to=59, width=3,
                   textvariable=self.s, format="%02.0f").grid(row=0, column=2)

        # label entry
        self.msg_entry = tk.Entry(root)
        self.msg_entry.insert(0, "Wake up")
        self.msg_entry.pack(pady=5)

        tk.Button(root, text="Add Alarm", command=self.add_alarm).pack()

        # list of alarms
        self.box = tk.Listbox(root, height=5)
        self.box.pack(pady=10)

        # buttons
        btns = tk.Frame(root)
        btns.pack()

        tk.Button(btns, text="Delete", command=self.delete_alarm).pack(side="left")
        tk.Button(btns, text="Stop", command=self.stop_alarm).pack(side="left")

        self.status = tk.Label(root, text="No alarm set")
        self.status.pack(pady=5)

        # start loops
        self.update_time()
        self.check_alarm()

    def update_time(self):
        now = datetime.datetime.now()

        self.time_lbl.config(text=now.strftime("%H:%M:%S"))
        self.date_lbl.config(text=now.strftime("%d %b %Y"))

        self.root.after(1000, self.update_time)

    def add_alarm(self):
        try:
            t = datetime.time(int(self.h.get()),
                              int(self.m.get()),
                              int(self.s.get()))
        except:
            messagebox.showerror("Error", "Wrong time")
            return

        msg = self.msg_entry.get()
        if msg == "":
            msg = "Alarm"

        # storing as list instead of dict (simpler)
        self.alarms.append([t, msg, True])

        self.update_list()
        self.status.config(text="Alarm added")

    def update_list(self):
        self.box.delete(0, "end")

        for a in self.alarms:
            state = "ON" if a[2] else "OFF"
            self.box.insert("end", f"{a[0]}  {state}  {a[1]}")

    def delete_alarm(self):
        sel = self.box.curselection()
        if not sel:
            return

        self.alarms.pop(sel[0])
        self.update_list()

    def check_alarm(self):
        now = datetime.datetime.now().time().replace(microsecond=0)

        for a in self.alarms:
            if a[2] and a[0] == now:
                a[2] = False
                self.update_list()
                self.ring(a[1])

        self.root.after(1000, self.check_alarm)

    def ring(self, msg):
        self.ringing = True
        self.stop_flag.clear()

        self.status.config(text="Ringing...")

        threading.Thread(target=play_sound,
                         args=(self.stop_flag,),
                         daemon=True).start()

        messagebox.showinfo("Alarm", msg)
        self.stop_alarm()

    def stop_alarm(self):
        if self.ringing:
            self.stop_flag.set()
            self.ringing = False
            self.status.config(text="Stopped")


root = tk.Tk()
app = AlarmApp(root)
root.mainloop()