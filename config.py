import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5098573891:AAG0npXiVaJKJXC4J1S-2qOG-5Gh_2IKmR8")

    APP_ID = int(os.environ.get("APP_ID", 8064991))

    API_HASH = os.environ.get("API_HASH", "9c1ef35f4339c2153f3f6254eee60691")
