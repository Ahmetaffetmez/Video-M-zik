from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "7552582768:AAFw4Z_dXQgwtbAaNSYF954Vm-JtO8hRw0g")
API_ID = int(getenv("API_ID", "21814744"))
API_HASH = getenv("API_HASH", "024ac6bfea2094f8e5e326d778fdcb54")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "http://www.mongodb.org/display/DOCS/Updating#Updating-ModifierOperations")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6049517588").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "6049517588").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001906045085"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "müzikturkey")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", 
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "kurucu_sahipp")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "@kurucu_sahipp":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1")).strip() == "BADNvmIAsGamczQ1CM_Rq9bteR1Gqwr5MdSV8f13GlqULpNHCRmlOoUn9Z7_2neJ5ZFj5EW90o6Jzc-XT6-PIsL9QPrefJ6XXeY9hEk_zrIc--20_i3bgFJjh9ooZYLXB6wGPMT0j5JuiW6OFgSENVNvdl_s7rhug69y2HfpWKITatIZndMKPVzI-qn61fb-CfclPPYyQa-nIZHm8OZ5WYmCvRXP-W_zwF2WhNPtqnPdBfFZYlVUCoJFZpiaZ1s8215KD7WfP32fLXi_BNJChYJ2_dzDvyTDb7Qv-qbBn_22p6tM5I9zK2JfDjWUsjPfn3dRh2DE1UOKaf2PcU3GginfwImfjAAAAAGJK7qIAA":
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
