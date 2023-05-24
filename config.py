from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "11360899"))
API_HASH = getenv("API_HASH", "b3a49413dfcaf0a16bd6d15e49772d70")

BOT_TOKEN = getenv("BOT_TOKEN", "6040800869:AAFOR9Gcd5Vvd15sNSb-Ag5HicUdfgE1c4E")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5542087374"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AQAiUW8XSpBT-JgWed49603RH_lUQl4spNLdotRzrkgoAuq4ewXE4NJSCmldB3XecOS-4ViFFkW436EpMIWDKO3s4qNXscBwkHp39nRsmDabjLLQ1qKl7lGfJQPd1RDUiKgQeZukPi0GkK230chK1ekZS1YB7Slnyr3ZND3f3rx3W4342wnmK8ISjr0i8il-9E6CdjDr3PVvf8b8QCr4SkicPbkjM97DzyX0UWv8RT4t22dn2RGy49x0kNIU4AnxwzRl9q4rn3kRrZzoiBkl9W0y6ni0JgrZOPIDB1BpaSYT9XrYzVggFNKomJyQ_QPo9L-5ef0umsjeOm5M5Mnpx3poAAAAAUpVis4A")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/beeeeeee007")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5542087374").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
