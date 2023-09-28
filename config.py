from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "6468327533:AAEQoIT05Ocgfx36b3IqtaQStuPW52Rlz4s")
API_ID = int(getenv("API_ID", "21814744"))
API_HASH = getenv("API_HASH", "024ac6bfea2094f8e5e326d778fdcb54")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6381139369").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "6381139369").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001915718534"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "müzikturkey")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/cavres34/Video-M-zik"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "çavreş")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "@rahatsizetmeyiniz34":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1")).strip() == "BAAJQfs2hAvog7OHF17qDsirs0f7Sp8I1SzZVVO4gw94Xye1ahMweQzDyju0G5nkMDtIw_wTO1XwITLTtitPLIT374z8ZwfS3kFBGn3QL08kpehEsMJjvj0bBW6ZYbjgj8bH0su9qqRpdZ1lbepwl0aQ_Y2O1FNRndxcORx6FVcnHGMfhE8X2hrV2UpliCZnjKs9CrPCv4vTeMOA3rfSOmHpR3nv6zExJqOs7y-kmJGlCv4NoQhDZk0biGszefQLtOU2-z8a6eEgToibFsgGhKrVBKEJVX2lE_2pfFqFaHBP5WvKKf0T-LzEU43M8Ev1E410e5_eDbYtZJNYiETssLnOAAAAAXhSk8kA":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
