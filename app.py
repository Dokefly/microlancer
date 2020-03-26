#!/usr/bin/python3.6

# -

from html2text import html2text
from tinydb import TinyDB

from modules import *
from time import sleep
from re import findall

# -

from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import telepot

# -

def push():

    database = TinyDB('config.conf')
    data_all = database.all()[0]

    chatbot = telepot.Bot(data_all['token'])

    if data_all['proxy'] != None:
        telepot.api.set_proxy(data_all['proxy'])

    latest_task = microlancer.API().latest_tasks()

    if len(latest_task) != 0:

        chatid = data_all['chatid']

        for task in latest_task:

            print('Task #{0} send to @{1} group.'.format(task['id'], data_all['user']))

            title = html2text(task['title']).replace('\n','')
            linkt = 'https://microlancer.io/task/view/' + str(task['id'])

            sat = task['amount']
            usd = satstousd.sats_to_usd(sat)

            keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Earn now', url=linkt)],])

            message = '✴️ New Task'
            message += '\n\n{0}'.format(title)
            message += '฿ Earn {0} sats (≈${1} USD)'.format(sat, usd)
            message += '\n\n-x-\n\n'
            chatbot.sendMessage(data_all['chatid'], message, reply_markup=keyboard)

        print('\n- x -\n')

if __name__ == '__main__':

    setconf.add_conf()

    database = TinyDB('config.conf')

    args = getparser.get_parser().parse_args()

    if args.proxy != None:
        setconf.add_conf(proxy=args.proxy)

    if args.token != None:

        if findall('[\d]+\:[\w]+', args.token):
            setconf.add_conf(token=args.token)

    if args.user != None:

        if len(args.user) >= 5 and len(args.user) <= 32:
                setconf.add_conf(user=args.user)

    if database.all()[0]['token'] != None and database.all()[0]['user'] != None:

        if database.all()[0]['chatid'] == None:
            setconf.add_chatid()

        print('\n- Starting - \n')

        while True:

            push()
            sleep(60)
