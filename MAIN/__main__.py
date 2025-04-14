from MAIN import Officer

if __name__=="__main__":
  Officer.run() 
  with Officer:
    Officer.send_message(chat_id=config.OWNER_ID, 
                         text="I AM ON MASTER✅")


