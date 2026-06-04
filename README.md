# IPL-Live-Score-IoT-ESP32
IPL Live Score IoT ESP32

An IoT-based project that displays live IPL cricket scores on an OLED display using an ESP32 microcontroller. The project fetches real-time match data from an online API and presents it on a compact OLED screen, making it a simple and effective IoT application for cricket enthusiasts.

📌 Project Overview

This project demonstrates the integration of:

ESP32 Wi-Fi connectivity
Live sports data retrieval through APIs
OLED display interfacing
Real-time IoT applications

The system continuously connects to the internet, fetches IPL match information, and updates the OLED display with the latest score details.

🚀 Features
📡 Real-time IPL score updates
📶 Wi-Fi-enabled ESP32 connectivity
🖥 OLED display output
⚡ Lightweight and low-power design
🔄 Automatic score refresh
🌐 IoT-based live data monitoring
🛠 Hardware Requirements
Component	Quantity
ESP32 Development Board	1
SSD1306 OLED Display (128x64)	1
Jumper Wires	As required
USB Cable	1
Internet Connection	Required
💻 Software Requirements
MicroPython
Thonny IDE / uPyCraft
ESP32 Firmware
SSD1306 OLED Library
Cricket Score API
📂 Project Structure
IPL-Live-Score-IoT-ESP32/
│
├── README.md              # Project documentation
├── main.py                # Main application code
├── ssd1306.py             # OLED display driver
├── diagram.json           # Circuit diagram configuration
└── wokwi-project.txt      # Wokwi simulation project details
🔌 Circuit Connections
ESP32 ↔ SSD1306 OLED (I2C)
OLED Pin	ESP32 Pin
VCC	3.3V
GND	GND
SDA	GPIO 21
SCL	GPIO 22

Note: Pin numbers may vary depending on your implementation.

⚙️ Working Principle
ESP32 connects to a Wi-Fi network.
A cricket score API is accessed through the internet.
Live IPL score data is retrieved.
Score information is processed by the ESP32.
Updated score details are displayed on the SSD1306 OLED screen.
The process repeats periodically for continuous updates.
▶️ Installation Steps
1. Flash MicroPython Firmware

Install MicroPython firmware on the ESP32 board.

2. Upload Project Files

Upload the following files to ESP32:

main.py
ssd1306.py
3. Configure Wi-Fi

Open main.py and update:

SSID = "Your_WiFi_Name"
PASSWORD = "Your_WiFi_Password"
4. Configure API

Replace the API URL and key (if required) with your cricket score API details.

5. Run the Project

Execute:

main.py

The OLED display will start showing live IPL match information.

🧪 Wokwi Simulation

This project includes simulation files for testing in Wokwi.

To run:

Open Wokwi.
Import diagram.json.
Configure the project.
Start the simulation.
📈 Applications
Live sports score monitoring
IoT dashboard projects
ESP32 learning projects
OLED display interfacing practice
Real-time API integration demonstrations
🔮 Future Enhancements
Multiple match support
Team logos and graphics
Web dashboard integration
Mobile app notifications
Score history storage
Match statistics visualization
👨‍💻 Author

Samhita Mani

GitHub Repository: IPL-Live-Score-IoT-ESP32

📜 License

This project is open-source and available for educational and learning purposes.

⭐ If you found this project useful, consider giving the repository a star!
