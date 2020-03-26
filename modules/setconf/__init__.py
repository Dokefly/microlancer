#!/usr/bin/python3.6

from tinydb import TinyDB
import telepot

def add_conf(token=None, user=None, chatid=None, proxy=None):

    database = TinyDB('config.conf')

    if len(database.all()) == 0:
        database.insert({'token' : None, 'user' : None, 'chatid' : None, 'proxy' : None})

    data_all = database.all()[0]

    if token != None:
        data_all.update({'token' : token})

    if user != None:
        data_all.update({'user' : user})

    if proxy != None:
        data_all.update({'proxy' : proxy})

    if chatid != None:
        data_all.update({'chatid' : chatid})

    database.purge()
    database.insert(data_all)

def add_chatid():

    database = TinyDB('config.conf')
    data_all = database.all()[0]

    if data_all['proxy'] != None:
        telepot.api.set_proxy(data_all['proxy'])

    if data_all['chatid'] == None:

        Bot = telepot.Bot(data_all['token'])

        for update in Bot.getUpdates():

            if 'message' in update.keys():

                if 'new_chat_members' in update['message'].keys():
                    getchat = Bot.getChat(update['message']['chat']['id'])

                    if 'username' in getchat.keys():

                        if data_all['user'] == getchat['username']:
                            add_conf(chatid=getchat['id'])
                            return None
