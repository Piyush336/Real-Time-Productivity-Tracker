import pandas as pd
import matplotlib.pyplot as plt

def generate_report(log_file="data/usage_log.csv"):
    """Generate a daily activity report."""
    try:
        log_data = pd.read_csv(log_file)
    except FileNotFoundError:
        print("No activity log found.")
        return

    summary = log_data.groupby("Application")["Duration"].sum()
    summary.plot(kind="bar", figsize=(10, 5), title="Application Usage Report")
    plt.xlabel("Application")
    plt.ylabel("Total Time (seconds)")
    plt.show()
