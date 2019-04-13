import config
import requests


hw = "Hello world!"    # da cancellare

get_me = config.common_api + "getMe"    # da cancellare
get_updates = config.common_api + "getUpdates"    # creare funzione

get_chat = config.common_api + "getChat?" + config.chat_id    # da cancellare

send_message = config.common_api + "SendMessage?" + config.chat_id + "&text=" + hw    # creare funzione


# req = requests.get(get_me)
# print(req.json())

# req2 = requests.get(get_updates)
# print(req2.json())

# req3 = requests.get(get_chat)
# print(req3.json())


req2 = requests.get(get_updates)
# print(req2.json())
message = req2.json()["result"][len(req2.json()["result"])-1]["message"]["text"]    # da sistemare
try:
    if "bot_command" in req2.json()["result"][len(req2.json()["result"])-1]["message"]["entities"][len(req2.json()["result"][len(req2.json()["result"])-1]["message"]["entities"])-1]["type"]:    # da sistemare
        is_bot_command = True
except:
    pass

if "/helloworld" in message and is_bot_command:
    req4 = requests.get(send_message)