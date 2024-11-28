import pygetwindow as gw

def get_active_application():
    active_window = gw.getActiveWindow()
    return active_window.title if active_window else "Unknown"

PRODUCTIVE_APPS = ["Microsoft Word", "Google Docs", "Evernote", "Notion", "Trello", 
    "Slack", "Microsoft Teams", "Zoom", "Google Meet", "Outlook", 
    "Thunderbird", "VSCode", "PyCharm", "Jupyter Notebook", "Atom", 
    "Sublime Text", "IntelliJ IDEA", "Eclipse", "GitHub Desktop", 
    "GitLab", "Asana", "ClickUp", "Monday.com", "LibreOffice Writer", 
    "Google Calendar", "Microsoft Excel", "Google Sheets", "Power BI", 
    "Tableau", "RStudio", "MATLAB", "Anaconda", "Kaggle", "Coursera", 
    "edX", "Khan Academy", "Udemy", "YouTube (Educational Content)", 
    "Duolingo", "Grammarly", "Todoist", "Focus Booster", "Pomodone", 
    "Habitica", "Forest", "Pocket", "Readwise", "Dropbox", "Google Drive", 
    "OneDrive", "Adobe Acrobat Reader", "Bluebeam", "Xmind", "MindMeister"]
UNPRODUCTIVE_APPS = ["YouTube(Entertainment Content)", "Netflix", "Hulu", "Amazon Prime Video", 
    "Disney+", "HBO Max", "Spotify", "Apple Music", "TikTok", "Instagram", 
    "Facebook", "Twitter", "Snapchat", "Reddit", "WhatsApp", "Telegram", 
    "WeChat", "Discord (Non-work channels)", "Pinterest", "Twitch", 
    "PUBG Mobile", "Call of Duty Mobile", "Fortnite", "League of Legends", 
    "Among Us", "Roblox", "Minecraft", "Clash of Clans", "Candy Crush Saga", 
    "Subway Surfers", "8 Ball Pool", "Genshin Impact", "Apex Legends", 
    "Valorant", "Steam", "Epic Games Launcher", "Battle.net", "Xbox App", 
    "PlayStation App", "Spotify", "SoundCloud", "Gaana", "JioSaavn", 
    "MX Player", "VLC (Non-work usage)", "Snapseed", "Canva (Non-work usage)"]

def classify_app(app_name):
    if app_name in PRODUCTIVE_APPS:
        return "Productive"
    elif app_name in UNPRODUCTIVE_APPS:
        return "Unproductive"
    return "Neutral"

import sqlite3

def create_database():
    conn = sqlite3.connect('activity_logs.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            timestamp TEXT,
            application TEXT,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_activity(timestamp, application, category):
    conn = sqlite3.connect('activity_logs.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (timestamp, application, category) VALUES (?, ?, ?)", 
                   (timestamp, application, category))
    conn.commit()
    conn.close()


import matplotlib.pyplot as plt

def plot_productivity():
    conn = sqlite3.connect('activity_logs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT category, COUNT(*) FROM logs GROUP BY category")
    data = cursor.fetchall()
    conn.close()

    labels = [row[0] for row in data]
    counts = [row[1] for row in data]
    
    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title("Productivity Breakdown")
    plt.show()


import tkinter as tk

def show_dashboard():
    root = tk.Tk()
    root.title("Productivity Tracker")
    
    tk.Button(root, text="Show Productivity Chart", command=plot_productivity).pack(pady=20)
    tk.Label(root, text="Keep working smart!").pack(pady=10)
    
    root.mainloop()

show_dashboard()


import time
from datetime import datetime

create_database()

while True:
    app_name = get_active_application()
    category = classify_app(app_name)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_activity(timestamp, app_name, category)
    time.sleep(100)  # Log every 100 seconds

