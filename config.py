from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/58117d21293813b59b5ba.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/744470e486a165762f7bd.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SSC_MAKER_QUIZ")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/QuizBot_Exampur")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6943682712").split()))


FAILED = "https://graph.org/file/58117d21293813b59b5ba.jpg"
