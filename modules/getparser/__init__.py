#!/usr/bin/python3.6

import argparse

def get_parser():

    parser = argparse.ArgumentParser(
        prog='app',
        usage='./app [options]',
        description='Push Task is a bot designed to send notification whenever a new task is added to microlancer.io',
        epilog='\n< microlancer.io >\n'
    )

    parser.add_argument(
        '--token', action='store', type=str, dest='token', default=None,
        help='add the access token'
    )

    parser.add_argument(
        '--user', action='store', type=str, dest='user', default=None,
        help='add the group username'
    )

    parser.add_argument(
        '--proxy', action='store', type=str, dest='proxy', default=None,
        help='add a proxy to the bot'
    )

    return parser
