import param    # contiene il token
import telepot
import time
from telepot.loop import MessageLoop

# telepot is currently inactive and the repository is archived by the owner
# TODO: rewrite the application using another library. Evaluate python-telegram-bot or pyTelegramBotAPI

bot = telepot.Bot(param.token)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == "text":
        name = msg["from"]["first_name"]
        txt = msg["text"]
        if txt.startswith("/helloworld"):
            bot.sendMessage(chat_id, "Ciao {}!".format(name))
            bot.sendMessage(chat_id, "Hello World!")

MessageLoop(bot, handle).run_as_thread()
print ("Listening ...")

# Keep the program running.
while 1:
    time.sleep(10)