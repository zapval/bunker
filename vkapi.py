import vk
import random
from settings import *
from flask import Flask, request, json
import time
import settings



session = vk.Session()
api = vk.API(session, v = 5.103)

def send_message(peer_id, random_id, keyboard, token, message, attachment):
    api.messages.send(access_token = "d464a412ae97183736e77e0657c1827c342fee3635cf733bfa0333adbde63b16c5f4212abedde24fd26c5", keyboard = keyboard, random_id = random.randint(1,100), peer_id=str(peer_id), message=message, attachment=attachment)
