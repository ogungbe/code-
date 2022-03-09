#!/usr/bin/env python3


class Meeting(object):
    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)'

class Schedule(object):

    def __init__(self, schedule=None):
        self.schedule = ()
        self.ddd = {}

    def add(self, other):

        self.ddd[f'{other.hour:02d}:{other.minute:02d}'] = f'({other.duration} minutes)'

    def __str__(self):
        mylist = []
        for k, v in sorted(self.ddd.items()):
          mylist.append(f'{k} {v}')
        output = '\n'.join(mylist)
        return f'Schedule\n--------\n{output}\nMeetings today: {len(self.ddd)}'
    