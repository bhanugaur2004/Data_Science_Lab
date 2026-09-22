import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

# -----------------------------
# Data storage
# -----------------------------

times = []
cpu_data = []
ram_data = []
disk_data = []
download_data = []
upload_data = []

# Previous network values
previous_net = psutil.net_io_counters()
previous_time = datetime.now()


# -----------------------------
# Create dashboard
# -----------------------------

fig = plt.figure(figsize=(14, 9))

fig.suptitle(
    "REAL-TIME LAPTOP SYSTEM MONITOR",
    fontsize=18,
    fontweight="bold"
)

# CPU graph
ax_cpu = plt.subplot(2, 2, 1)

# RAM graph
ax_ram = plt.subplot(2, 2, 2)

# Disk graph
ax_disk = plt.subplot(2, 2, 3)

# Network graph
ax_network = plt.subplot(2, 2, 4)


# -----------------------------
# Update function
# -----------------------------

def update(frame):

    global previous_net, previous_time

    # Current time
    current_time = datetime.now()

    time_label = current_time.strftime("%H:%M:%S")

    # -------------------------
    # CPU
    # -------------------------

    cpu = psutil.cpu_percent(interval=0.1)

    # -------------------------
    # RAM
    # -------------------------

    ram = psutil.virtual_memory().percent

    # -------------------------
    # Disk
    # -------------------------

    disk = psutil.disk_usage("/").percent

    # -------------------------
    # Network
    # -------------------------

    current_net = psutil.net_io_counters()

    elapsed = (current_time - previous_time).total_seconds()

    download_speed = (
        current_net.bytes_recv - previous_net.bytes_recv
    ) / elapsed

    upload_speed = (
        current_net.bytes_sent - previous_net.bytes_sent
    ) / elapsed

    # Convert bytes/sec to MB/sec
    download_speed = download_speed / (1024 * 1024)
    upload_speed = upload_speed / (1024 * 1024)

    previous_net = current_net
    previous_time = current_time

    # -------------------------
    # Store data
    # -------------------------

    times.append(time_label)

    cpu_data.append(cpu)
    ram_data.append(ram)
    disk_data.append(disk)

    download_data.append(download_speed)
    upload_data.append(upload_speed)

    # Keep only latest 30 readings
    if len(times) > 30:

        times.pop(0)

        cpu_data.pop(0)
        ram_data.pop(0)
        disk_data.pop(0)

        download_data.pop(0)
        upload_data.pop(0)


    # -------------------------
    # CPU GRAPH
    # -------------------------

    ax_cpu.clear()

    ax_cpu.plot(
        times,
        cpu_data,
        marker="o"
    )

    ax_cpu.fill_between(
        range(len(cpu_data)),
        cpu_data,
        alpha=0.3
    )

    ax_cpu.set_title(
        f"CPU Usage: {cpu:.1f}%"
    )

    ax_cpu.set_ylabel("Usage (%)")

    ax_cpu.set_ylim(0, 100)

    ax_cpu.grid(True)

    ax_cpu.tick_params(
        axis="x",
        rotation=45
    )


    # -------------------------
    # RAM GRAPH
    # -------------------------

    ax_ram.clear()

    ax_ram.plot(
        times,
        ram_data,
        marker="o"
    )

    ax_ram.fill_between(
        range(len(ram_data)),
        ram_data,
        alpha=0.3
    )

    ax_ram.set_title(
        f"RAM Usage: {ram:.1f}%"
    )

    ax_ram.set_ylabel("Usage (%)")

    ax_ram.set_ylim(0, 100)

    ax_ram.grid(True)

    ax_ram.tick_params(
        axis="x",
        rotation=45
    )


    # -------------------------
    # DISK GRAPH
    # -------------------------

    ax_disk.clear()

    ax_disk.plot(
        times,
        disk_data,
        marker="o"
    )

    ax_disk.fill_between(
        range(len(disk_data)),
        disk_data,
        alpha=0.3
    )

    ax_disk.set_title(
        f"Disk Usage: {disk:.1f}%"
    )

    ax_disk.set_ylabel("Usage (%)")

    ax_disk.set_ylim(0, 100)

    ax_disk.grid(True)

    ax_disk.tick_params(
        axis="x",
        rotation=45
    )


    # -------------------------
    # NETWORK GRAPH
    # -------------------------

    ax_network.clear()

    ax_network.plot(
        times,
        download_data,
        marker="o",
        label="Download"
    )

    ax_network.plot(
        times,
        upload_data,
        marker="o",
        label="Upload"
    )

    ax_network.set_title(
        "Network Speed"
    )

    ax_network.set_ylabel(
        "MB/s"
    )

    ax_network.grid(True)

    ax_network.legend()

    ax_network.tick_params(
        axis="x",
        rotation=45
    )


    # -------------------------
    # System information
    # -------------------------

    cores = psutil.cpu_count(logical=False)

    threads = psutil.cpu_count(logical=True)

    fig.text(
    0.5,
    0.025,
    f"CPU Cores: {cores}   |   "
    f"Logical Processors: {threads}   |   "
    f"Download: {download_speed:.2f} MB/s   |   "
    f"Upload: {upload_speed:.2f} MB/s",
    ha="center",
    fontsize=11
)

    plt.tight_layout(
    rect=[0, 0.08, 1, 0.95]
)


# -----------------------------
# Start animation
# -----------------------------

animation = FuncAnimation(
    fig,
    update,
    interval=1000,
    cache_frame_data=False
)

plt.show()