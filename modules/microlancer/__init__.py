#!/usr/bin/python3.6

# /

import requests
import tinydb
import json

# /

class API:

    def __init__(self):

        self.api = self.get_api()

        self.tasks = self.api['tasks']
        self.sorts = sorted(self.api['sort'])

        self.database = tinydb.TinyDB('sorts.db')

        if len(self.database.all()) == 0:

            self.database.insert({'sorts' : []})
            self.latest_tasks()

    def __repr__(self):

        return '\n< @Dokefly >\n'

    def latest_tasks(self):

        data_all = self.database.all()[0]
        get_sorts = data_all['sorts']
        tasks_all = []

        for sort in self.sorts:

            if not (sort in get_sorts):

                get_sorts.append(sort)
                tasks_all.append(self.tasks[str(sort)])

        self.database.purge()
        self.database.insert({'sorts' : get_sorts})

        return tasks_all

    def get_api(self):

        while True:

            try:
                return json.loads(
                    requests.get('https://microlancer.io/api/task/list').text
                )
            except KeyboardInterrupt: break
            except: pass
