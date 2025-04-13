import config 
from pyrogram import Client, filters 
import logging 
import os 
import sys

logging.basicConfig(
  format="[KuroAI-Beta] %(name)s - %(levelname)s - %(message)s",
  handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
  level=logging.INFO,
)



HANDLERS = ["!", "/", ".", "?", "#", "$"]
VERSION = config.system_version
ABUSES = [
    # Hindi
    "chutiya", "madarchod", "bhosdi", "bhenchod", "lund", "gaand", "randi", "chut", "gandu", "bhosdike",
    "chod", "jhant", "maa ka", "behen ka", "teri maa", "maa chuda", "bhen chudai", "loda", "chutmar", "gaandfat",
    
    # English
    "fuck", "fucker", "motherfucker", "bitch", "asshole", "bastard", "shit", "dick", "pussy", "cock", "cunt",
    "slut", "jerk", "whore", "douchebag", "son of a bitch", "suck my dick", "nigga", "nigger", "retard",

    # Tamil
    "punda", "thuppari", "thevidiya", "thevidiya payal", "munda", "saniyan", "thayoli", "sambavane", "po da",
    "thaye kudi", "entha da", "mokka", "loosu", "sethupoya", "soothu", "sani", "thevudiya paiya", "chiya",

    # Mix & common variations
    "chutiyapa", "chodu", "maa chod", "bhen ke", "gand", "chodna", "gaand mara",
]

if not config.API_ID or not config.API_HASH or not config.TOKEN:
  print("❌ API_ID, HASH nad TOKEN must be in environment varaibles") 


Officer = Client("OFFICER_OF_JUSTICE", 
  api_id=config.API_ID, 
  api_hash=config.API_HASH, 
  bot_token=config.TOKEN, 
  plugins=dict(root="MAIN")
) 
