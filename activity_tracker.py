import psutil
import time
import pandas as pd

def get_active_window():
    """Get the title of the currently active window."""
    try:
        import win32gui
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except ImportError:
        return "Unknown Window"

def track_usage(log_file="data/usage_log.csv", interval=60):
    """Track application usage and log into a file."""
    columns = ["Timestamp", "Application", "Duration"]
    try:
        log_data = pd.read_csv(log_file)
    except FileNotFoundError:
        log_data = pd.DataFrame(columns=columns)

    start_time = time.time()
    prev_app = None

    while True:
        current_app = get_active_window()
        if prev_app != current_app:
            end_time = time.time()
            duration = end_time - start_time
            if prev_app:
                log_data = pd.concat([log_data, pd.DataFrame(
                    [[time.strftime("%Y-%m-%d %H:%M:%S"), prev_app, duration]],
                    columns=columns
                )])
                log_data.to_csv(log_file, index=False)
            prev_app = current_app
            start_time = end_time
        time.sleep(interval)
