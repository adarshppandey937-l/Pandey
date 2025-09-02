#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ
API_ID = int(environ.get("API_ID", "22865155"))
API_HASH = environ.get("API_HASH", "e430e3f61712616b926be959f1612c46")
BOT_TOKEN = environ.get("BOT_TOKEN", "8450724630:AAH0W-cAU4koT4iwLAIsffLtMuUvS-JihrE")
OWNER = int(environ.get("OWNER", "7265520264"))
CREDIT = environ.get("CREDIT", "pandey")
AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


