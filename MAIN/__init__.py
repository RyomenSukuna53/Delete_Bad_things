import config 
from pyrogram import Client, filters 
import logging 
import os 
import sys


if not API_ID or API_HASH or TOKEN:
  print("❌ API_ID, HASH nad TOKEN must be in environment varaibles") 


Officer = Client(
  api_id=config.API_ID, 
  api_hash=config.API_HASH, 
  bot_token=config.TOKEN, 
  plugins=dict(root="COMMAND/")
) 
