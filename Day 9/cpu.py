import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# Store CPU usage and time
cpu_usage = []
time_values = []

# Create figure
fig, ax = plt.subplots()

def update(frame):

    # Get current CPU usage
    cpu = psutil.cpu_percent(interval=1)

    # Get current time
    current_time = datetime.now().strftime("%H:%M:%S")

    # Store values
    cpu_usage.append(cpu)
    time_values.append(current_time)

    # Keep only the latest 30 readings
    if len(cpu_usage) > 30:
        cpu_usage.pop(0)
        time_values.pop(0)

    # Clear previous graph
    ax.clear()

    # Plot CPU usage
    ax.plot(
        time_values,
        cpu_usage,
        marker="o"
    )

    # Fill area below graph
    ax.fill_between(
        range(len(cpu_usage)),
        cpu_usage,
        alpha=0.3
    )

    # Titles and labels
    ax.set_title("Real-Time CPU Usage")
    ax.set_xlabel("Time")
    ax.set_ylabel("CPU Usage (%)")

    # CPU ranges from 0 to 100
    ax.set_ylim(0, 100)

    # Grid
    ax.grid(True)

    # Rotate time labels
    plt.xticks(rotation=45)


# Update graph every 1 second
animation = FuncAnimation(
    fig,
    update,
    interval=1000
)

plt.tight_layout()
plt.show()