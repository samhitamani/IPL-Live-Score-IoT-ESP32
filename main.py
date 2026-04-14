import machine
import ssd1306
import time
import network
import random

# --- 1. CONFIGURATION ---
WIDTH = 128
HEIGHT = 64
SCL_PIN = 22
SDA_PIN = 21

# --- 2. HARDWARE INITIALIZATION ---
i2c = machine.I2C(0, scl=machine.Pin(SCL_PIN), sda=machine.Pin(SDA_PIN))
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

def connect_wifi():
    """Connects to Wokwi's virtual WiFi"""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("Wokwi-GUEST", "")
    print("Connecting to WiFi...", end="")
    while not wlan.isconnected():
        time.sleep(0.5)
        print(".", end="")
    print("\nConnected! IP:", wlan.ifconfig()[0])

# --- 3. UI FUNCTIONS ---
def draw_static_ui(t1, t2):
    """Draws the fixed layout elements"""
    oled.fill(0)
    # Header: Teams
    oled.rect(0, 0, 128, 16, 1)
    oled.text(f"{t1} vs {t2}", 22, 4)
    # Footer Line
    oled.hline(0, 48, 128, 1)
    oled.show()

def update_score(runs, wickets, overs, crr):
    """Updates only the dynamic areas to prevent flickering"""
    # Clear middle and bottom sectors
    oled.fill_rect(0, 17, 128, 30, 0)
    oled.fill_rect(0, 49, 128, 15, 0)
    
    # Render Score (Simulated Bold)
    score_text = f"{runs}/{wickets}"
    x_pos = (WIDTH - (len(score_text) * 8)) // 2
    oled.text(score_text, x_pos, 26)
    oled.text(score_text, x_pos + 1, 26) # Shadow effect
    
    # Render Stats
    stats = f"Ov:{overs}  CRR:{crr}"
    oled.text(stats, 10, 52)
    oled.show()

def wicket_alert():
    """Blinking animation for wickets"""
    for _ in range(4):
        oled.invert(True)
        time.sleep(0.15)
        oled.invert(False)
        time.sleep(0.15)
    
    # Alert Box
    oled.fill_rect(20, 20, 88, 24, 1)
    oled.text("WICKET!", 35, 28, 0)
    oled.show()
    time.sleep(1.5)

# --- 4. MAIN EXECUTION ---
connect_wifi()
team_a, team_b = "CSK", "RCB"
draw_static_ui(team_a, team_b)

# Simulation Variables
current_runs = 0
current_wickets = 0
current_balls = 0

while current_wickets < 10:
    # Random Match Logic
    ball_outcome = random.choice([0, 1, 2, 4, 6, 'W', 'W', 1, 2]) # Weighting for realism
    
    if ball_outcome == 'W':
        current_wickets += 1
        wicket_alert()
        draw_static_ui(team_a, team_b) # Redraw header after alert
    else:
        current_runs += ball_outcome
    
    current_balls += 1
    overs_display = f"{current_balls // 6}.{current_balls % 6}"
    crr = round(current_runs / (current_balls / 6), 2) if current_balls > 0 else 0.0
    
    update_score(current_runs, current_wickets, overs_display, crr)
    
    time.sleep(3) # Wait for the next 'ball'

oled.fill(0)
oled.text("MATCH OVER", 25, 28)
oled.show()