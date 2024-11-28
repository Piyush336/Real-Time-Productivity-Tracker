import psutil
import time

def is_idle(threshold=300):
    """Detects if the system is idle."""
    idle_time = time.time() - psutil.boot_time()
    return idle_time > threshold
