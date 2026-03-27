# Alarm Clock Application (Python - Tkinter)

## Project Statement

This project is a simple Alarm Clock application developed using Python and Tkinter. The main idea behind this project was to understand how real-time systems work and how a graphical user interface (GUI) can be built using basic Python libraries.

The application allows users to set alarms by specifying the hour, minute, and second. Once the system time matches the set alarm time, a notification is displayed along with a sound alert. The user can also manage multiple alarms and stop them when needed.

## Purpose

The purpose of this project is to:
- Learn GUI development using Tkinter  
- Understand how time-based conditions are handled in programs  
- Explore basic concepts of threading  
- Build a small but practical real-world application  

## Key Features

- Displays current time and date  
- Allows setting multiple alarms  
- Popup notification when alarm rings  
- Sound alert (if supported)  
- Option to delete alarms  
- Stop button to stop ringing  

## Approach

The project was built step by step:
1. First, the clock display was implemented using system time.
2. Then, input fields were added to set alarm time.
3. A checking mechanism was created to compare current time with alarm time.
4. Threading was used so that the alarm sound does not freeze the interface.

## Learning Outcomes

Through this project, I learned:
- How Tkinter works for building GUI applications  
- How to handle time and scheduling in Python  
- Basics of threading and parallel execution  
- Structuring a small application from scratch  

## Limitations

- Alarms are not saved after closing the application  
- No snooze feature is implemented  
- User interface is basic  
