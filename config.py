# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24299265")

API_HASH = os.environ.get("API_HASH", "ca3dc8c5351e4ba196df3305689e8e93")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7307135175:AAHp5h-tQhI9LvYHoAVCISk-InVXlF3MDdI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Botz") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://mansipatil2908:Mansipatil0101@cluster0.u4mdg3e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5947696425').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
