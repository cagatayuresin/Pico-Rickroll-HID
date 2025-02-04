# 🖥️ Raspberry Pi Pico HID Rickroll Script

🇬🇧 **[Türkçe okumak için tıklayın](#)**  

![License](https://img.shields.io/github/license/cagatayuresin/Pico-Rickroll-HID) ![Windows](https://img.shields.io/badge/Windows-Supported-brightgreen?logo=windows) ![macOS](https://img.shields.io/badge/macOS-Supported-brightgreen?logo=apple) ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Supported-red?logo=raspberrypi&logoColor=white) ![Pico](https://img.shields.io/badge/Pico-RP2040-orange?logo=raspberrypi&logoColor=white) ![RP2040](https://img.shields.io/badge/RP2040-Microcontroller-blue?logo=raspberrypi&logoColor=white) ![Adafruit](https://img.shields.io/badge/Powered%20by-Adafruit-red?logo=adafruit&logoColor=white) ![MicroPython](https://img.shields.io/badge/MicroPython-Compatible-orange?logo=micropython&logoColor=white)

![Pico Rickroll in Action](rickroll-roll.gif)

This project is a **HID (Human Interface Device) attack script** that uses **Raspberry Pi Pico as a keyboard** to automatically open a **Rickroll video** on the connected computer.  

✅ **Supports Windows and macOS.**  
✅ **Fully compatible with Turkish Q keyboard layout.**  
✅ **Automatically opens YouTube, switches to fullscreen, and maximizes volume.**  

---

## 📌 Requirements & Setup  

### 1️⃣ Required Hardware  

- **Raspberry Pi Pico**  
- **USB Type-C or micro USB cable**  

### 2️⃣ Required Software  

- **CircuitPython 8.x or 9.x** must be installed on the Pico.  
- **Adafruit HID Libraries** must be loaded.  

**📌 Step-by-Step Setup:**  

1. **Boot Raspberry Pi Pico in BOOTSEL mode.**  
   - Hold the `BOOTSEL` button before plugging in the Pico.  
   - Plug it into your computer, then release the button.  
   - A drive named `RPI-RP2` should appear.  

2. **Install CircuitPython Firmware**  
   - Download the latest version from: [https://circuitpython.org/board/raspberry_pi_pico/](https://circuitpython.org/board/raspberry_pi_pico/)  
   - Drag and drop the `.uf2` file onto the `RPI-RP2` drive.  

3. **Install Adafruit HID Libraries**  
   - Download **`adafruit_hid`** from: [https://github.com/adafruit/Adafruit_CircuitPython_HID/releases](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases)  
   - Copy the **`adafruit_hid`** folder into the `lib` directory inside `CIRCUITPY`.  

---

## 🔍 How It Works  

1. **The Pico automatically starts working when plugged in.**  
2. **It detects the operating system.**  
   - **If Windows:** Opens the Run dialog (`Win + R`).  
   - **If macOS:** Opens Spotlight (`Cmd + Space`).  
3. **Types the URL correctly based on the Turkish Q keyboard layout.**  
4. **Opens YouTube and starts playing the video.**  
5. **Switches to fullscreen and maximizes the volume.**  

📢 **Works instantly when plugged in, stops when unplugged!**  

---

## ⚙️ Keyboard Layout Support  

| **Keyboard Layout** | **Support Status** |
|-----------------|----------------|
| 🇹🇷 **Turkish Q** | ✅ Supported |
| 🇹🇷 **Turkish F** | ❌ Not Supported |
| 🇺🇸 **English Q (US)** | ✅ Supported |
| 🇬🇧 **English UK** | ❌ Not Supported |

**📢 NOTE:** This script is designed for **Turkish Q keyboard layout.**  

**If you are using a UK keyboard, switch your OS language settings to "English (US)".**  

---

## 🚀 Usage Instructions  

1️⃣ **Upload the Code to the Pico**  

- **Copy `code.py` to the `CIRCUITPY` drive on your Pico.**  

2️⃣ **Unplug and Replug the Pico**  

- **It will start working instantly!**  

3️⃣ **Did the Rickroll Start?**  

- If `https://www.youtube.com/watch?v=dQw4w9WgXcQ` opens and the volume is maxed out, EVERYTHING IS WORKING! 😈🎵  

---

## 🛠 Possible Issues & Solutions  

**1️⃣ Issue:** The URL is typed incorrectly, `/` appears as another character.  
**✅ Solution:**  

- Change your computer’s keyboard layout to **English (US).**  

**2️⃣ Issue:** YouTube opens but does not switch to fullscreen.  
**✅ Solution:**  

- The `F` key may not work on some systems. **Try replacing `Keycode.F` with `Keycode.CONTROL, Keycode.COMMAND, Keycode.F` in the code.**  

**3️⃣ Issue:** Volume is not increasing to the maximum.  
**✅ Solution:**  

- **Volume keys may behave differently depending on the OS.** Try replacing `ConsumerControlCode.VOLUME_INCREMENT` with `Keycode.VOLUME_UP`.  

---

## 📢 Legal Disclaimer  

This script is intended **for ethical cybersecurity purposes.** Unauthorized use **may be illegal.**  

🔹 **Use it for security testing and entertainment purposes only!**  
🔹 **Be mindful when Rickrolling someone!** 😆  

---

## 🤝 Contributing

All contributions, issue reports, and feature requests are welcome! You are free to fork this project, improve it, and submit fixes or enhancements.

If you find a bug or want to suggest a new feature, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

🔹 You are free to use, modify, and share this project.
🔹 Just make sure to follow the license terms! 📜

For more details, check the [LICENSE](LICENSE) file. 🚀

---
🎵 **"Never gonna give you up, never gonna let you down..."** 🎵
