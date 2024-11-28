import tkinter as tk
from threading import Thread
from activity_tracker import track_usage
from reporting_tools import generate_report

def start_tracking():
    """Start tracking in a separate thread."""
    thread = Thread(target=track_usage)
    thread.daemon = True
    thread.start()
    status_label.config(text="Tracking started...")

def show_report():
    """Generate and display the activity report."""
    generate_report()

# Build GUI
root = tk.Tk()
root.title("Productivity Tracker")

start_button = tk.Button(root, text="Start Tracking", command=start_tracking, width=20)
start_button.pack(pady=10)

report_button = tk.Button(root, text="Show Report", command=show_report, width=20)
report_button.pack(pady=10)

status_label = tk.Label(root, text="Status: Idle")
status_label.pack(pady=20)

root.mainloop()
