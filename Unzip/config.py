import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6636023413:AAHMmRz5x48PbkGJuYItUmXKtU8RpjCkBRQ")
    API_ID = int(os.environ.get("API_ID", "25465082"))
    API_HASH = os.environ.get("API_HASH", "4a6b5e40c8bc08c8af09add6cca23b18")
    
    
