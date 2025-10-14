import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    bs_userName = os.getenv('BS_USER_NAME')
    bs_accessKey = os.getenv('BS_ACCESS_KEY')
    bs_url = os.getenv('BS_URL', 'http://hub.browserstack.com/wd/hub')

settings = Settings()