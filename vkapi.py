import vk
import random
from settings import *
from flask import Flask, request, json
import time
import settings



session = vk.Session()
api = vk.API(session, v = 5.103)

def send_message(peer_id, random_id, keyboard, token, message, attachment):
    api.messages.send(access_token = "0421951555eb8b3ae1cf323657ebf025d9886064857bd9e411df8aa5050df7fd5f67837bed3f614dbd200", keyboard = keyboard, random_id = random.randint(1,100), peer_id=str(peer_id), message=message, attachment=attachment)
