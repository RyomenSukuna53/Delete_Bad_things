from .__init__ import Officer 
from pyrogram import Client, filters 
from COMMANDS import * 
import config 

if __name__=="__main__":
  Officer.run() 
  with Officer:
    Officer.send_message(chat_id=config.OWNER_ID, 
                         text="I AM ON MASTER✅")


