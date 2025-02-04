import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


# 🔹 Initialize keyboard and media control
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
consumer_control = ConsumerControl(usb_hid.devices)

# 🔹 Delay settings
DELAY_TIMES = {
    "usb_connect": 3.0,
    "before_typing": 1.0,
    "browser_load": 5.0,
    "volume_step": 0.1,
}

# 🔹 Original Rickroll URL
ORIGINAL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 🔹 Mapping for Turkish Q keyboard to match US layout
TURKISH_Q_MAP = {":": "?", "/": "&", ".": "/", "?": "_", "=": ")"}


# 🔹 Function to convert original URL to match Turkish Q keyboard layout
def convert_to_turkish_q_layout(url):
    """Converts the original URL to match Turkish Q keyboard layout before sending it in US layout."""
    converted_url = ""
    for char in url:
        converted_url += TURKISH_Q_MAP.get(char, char)  # Convert only if needed
    return converted_url


# 🔹 Convert the original URL
RICKROLL_URL = convert_to_turkish_q_layout(ORIGINAL_URL)


# 🔹 Function to detect OS (Windows/macOS)
def detect_os():
    """Detects whether the target system is macOS or Windows."""
    for device in usb_hid.devices:
        if "Apple" in str(device).lower():
            return "mac"
    return "windows"


# 🔹 Function to quickly write the converted URL
def type_text(text):
    """Writes the converted URL using the US keyboard layout for speed."""
    keyboard_layout.write(text)
    time.sleep(0.1)  # Small delay after writing


# 🔹 Open browser and type URL
def open_browser(os_type):
    """Opens YouTube via the correct method for the detected OS."""
    print("🌐 Opening browser and typing URL...")
    if os_type == "mac":
        print("macOS detected: Opening URL via Spotlight search.")
        keyboard.send(Keycode.COMMAND, Keycode.SPACE)
    else:
        print("Windows detected: Opening URL via Run dialog.")
        keyboard.send(Keycode.WINDOWS, Keycode.R)

    time.sleep(DELAY_TIMES["before_typing"])
    type_text(RICKROLL_URL)  # Writes the converted URL quickly
    keyboard.send(Keycode.ENTER)


# 🔹 Make YouTube fullscreen
def fullscreen_video():
    """Waits for the browser to load and then makes YouTube fullscreen."""
    time.sleep(DELAY_TIMES["browser_load"])
    keyboard.send(Keycode.F)


# 🔹 Maximize system volume
def maximize_volume():
    """Increases system volume to the maximum level."""
    print("🔊 Increasing volume to maximum...")
    for _ in range(50):
        consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(DELAY_TIMES["volume_step"])


# 🔹 Main function
def execute_rickroll():
    """Executes the full Rickroll sequence based on detected OS."""
    print("🎵 Rickrolling the target system... 😈")
    time.sleep(DELAY_TIMES["usb_connect"])
    os_type = detect_os()

    open_browser(os_type)
    fullscreen_video()
    maximize_volume()

    print("🎵 Rickroll completed! 😈")


# 🔹 Run the script
execute_rickroll()
