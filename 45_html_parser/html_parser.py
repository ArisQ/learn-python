#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser


class PythonEventParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tag = ''
        self.event_title = ''
        self.event_time = ''
        self.event_location = ''
        self.event = []

    def handle_starttag(self, tag, attrs):
        if tag == 'h3':
            for k, v in attrs:
                if k == 'class' and v == 'event-title':
                    self.tag = 'event-title'
                    break
        if tag == 'time':
            self.tag = 'time'
        if tag == 'span':
            for k, v in attrs:
                if k == 'class' and v == 'event-location':
                    self.tag = 'event-location'
                    break

    def handle_data(self, data):
        if self.tag == 'event-title':
            self.event_title = data
        elif self.tag == 'time':
            self.event_time = data
        elif self.tag == 'event-location':
            self.event_location = data
            self.event.append({'title': self.event_title,
                               'time': self.event_time,
                               'location': self.event_location})
        self.tag = ''


parser = PythonEventParser()
with open('python-events.html') as f:
    parser.feed(f.read())
    for e in parser.event:
        print('title: %s, time: %s, location: %s' % (e['title'], e['time'], e['location']))
