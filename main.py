from seleniumbase import SB
from pathlib import Path
import threading


# ==============================
# CONFIGURACIÓN
# ==============================
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

BASE_DIR = Path(__file__).parent

BOT1_PROFILE = BASE_DIR / "sb-personas" / "Profile 1"
BOT2_PROFILE = BASE_DIR / "sb-personas" / "Profile 2"


# ==============================
# BOT 1
# ==============================
def abrir_bot_1():
    with SB(
        browser="chrome",
        binary_location=BRAVE_PATH,
        chromium_arg=f"--user-data-dir={BOT1_PROFILE}"
    ) as sb:
        sb.open("https://web.whatsapp.com")
        sb.sleep(9999)


# ==============================
# BOT 2
# ==============================
def abrir_bot_2():
    with SB(
        browser="chrome",
        binary_location=BRAVE_PATH,
        chromium_arg=f"--user-data-dir={BOT2_PROFILE}"
    ) as sb:
        sb.open("https://web.whatsapp.com")
        sb.sleep(9999)


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    t1 = threading.Thread(target=abrir_bot_1)
    t2 = threading.Thread(target=abrir_bot_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()