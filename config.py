from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13916313"))
API_HASH = getenv("4ced9f94162d9bbe1d3829a9fb601847")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("5365851389:AAFGZ1VvuEBZoIBqhcFSPCBSQS2n8MxcRUM")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
LOGGER_ID = int(getenv("-1001644049633"))
MONGO_DB_URI = getenv("mongodb+srv://kskop:kakujai253@cluster0.ew9p1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("2102097596", "").split()))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/855679eca3bca0bb1806f.jpg")
START_IMG = getenv("https://te.legra.ph/file/ad5988ac08ec86468e35b.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://BGMIxCHATS")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/KSKxCHEATS")

STRING_SESSION = getenv("BQBgD_WudallmzkqObBk6fb1cra9VjEF_vIFTGFPQyoF8o_5OGvEHvtzFrSa10hZhyzXSl7vRSTfoHwa48jtjdYf42gKzRU7vV2LBIpYl_1NyKEnRcGfDSwk0Nd76noRaTCMOs9WPH8jbSTgZmNc_eZ5Q-MKHLPgt498crb0gqa_eP1i9tf79Dq9sum85fnRxh9l0TheLOvClSBkOxbtnRN9R3pCvP2Of1MLWC0HMWaOx8RMrwGW5YOdT9iio_xPtMIJO4qbmHZQQI9JrLBJMv00Bpf5azpB4NXsTzXW7Jefi2NAxm10uoa05OpLb5GsupYet_pwX3SiDiLYUWWzdr2NAAAAAToe46wA", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
