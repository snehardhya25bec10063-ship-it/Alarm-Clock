# ⏰ Alarm Clock (Python Tkinter)

A simple alarm clock application built using Python and Tkinter.
This project was created to understand how GUI applications and time-based events work in Python.

---

## 📌 Features

* Shows current time and date in real-time
* Set multiple alarms
* Popup alert when alarm rings
* Sound alert (if pygame is available)
* Delete alarms
* Stop button to stop ringing

---

## 🛠️ Tech Used

* Python
* Tkinter (for GUI)
* datetime, time
* threading
* pygame + numpy (for sound, optional)

---

## ▶️ How to Run

1. Clone this repository

   ```bash
   git clone https://github.com/your-username/alarm-clock.git
   ```

2. Go into the project folder

   ```bash
   cd alarm-clock
   ```

3. Run the program

   ```bash
   python main.py
   ```

---

## ⚙️ How It Works

* The app continuously updates the current time using `after()` from Tkinter
* Alarms are stored in a list
* Every second, the program checks if current time matches any alarm
* When matched:

  * A popup appears
  * Sound starts playing (if available)
* Threading is used so the UI doesn't freeze during sound playback

---

## 📷 Preview

Screenshot 2026-03-27 220713.png

---

## 🚧 Limitations

* Alarms are not saved after closing the app
* No snooze feature
* Basic UI

---

## 📚 What I Learned

* Basics of GUI development using Tkinter
* Handling time-based conditions
* Using threading in Python
* Structuring a small project from scratch


