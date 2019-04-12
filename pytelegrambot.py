import config
import requests

get_me = config.common_api + "getMe"
get_updates = config.common_api + "getUpdates"

get_chat = config.common_api + "getChat?" + config.chat_id


# req = requests.get(get_me)
# print(req.json())

# req2 = requests.get(get_updates)
# print(req2.json())

# req3 = requests.get(get_chat)
# print(req3.json())


req2 = requests.get(get_updates)
# print(req2.json())
print(req2.json()["result"][len(req2.json()["result"])-1]["message"]["text"])
# print(len(req2.json()["result"][len(req2.json()["result"])-1]["message"]["entities"])-1)
print(req2.json()["result"][len(req2.json()["result"])-1]["message"]["entities"][len(req2.json()["result"][len(req2.json()["result"])-1]["message"]["entities"])-1]["type"])