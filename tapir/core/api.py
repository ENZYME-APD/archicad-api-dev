#!/usr/bin/env python27
# -*- coding: utf-8 -*-

__all__ = [ 'Link',
            'Command']

# - - - - - - - - BUILT-IN IMPORTS
import json
import urllib2

# - - - - - - - - LOCAL IMPORTS
from utility import dotNETBase

# - - - - - - - - CLASS LIBRARY

class Link(dotNETBase):

    _PORT = range(19723, 19726)
    _HOST = 'http://127.0.0.1'
    
    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if Link.is_valid(port):
            self._port = port
        else:
            raise Exception('Invalid port')
    
    @property
    def host(self):
        return self._HOST

    @property
    def address(self):
        return '{}:{}'.format(self._host, self.port)

    @property
    def is_valid(self):
        return self.port in self._PORT
    
    @property
    def is_alive(self):
        data = {'command' : 'API.IsAlive'}
        response = json.loads(self.post(data))
        return bool(response['succeeded'])
    
    def __init__(self, port):
        self.port = port

        if not self.is_alive:
            raise Exception('Script Error: Unable to create port.')

    def post(self, data):
        connection_object = urllib2.Request(self.address)
        connection_object.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(connection_object, json.dumps(data))
        return response.read()

    def __str__(self):
        return 'TapirLink : {}'.format(self.address)


class Command(dotNETBase):
    
    def __init__(self, link):
        self.link = link

    @staticmethod
    def create(command_name):
        return {'command' : 'API:{}'.format(command_name)}

    def get_elements(self):
        cmd = Command.create('GetAllElements')
        response = self.link.post(cmd)

        data = json.loads(response.read())

        elements = []

        for element in data['result']['elements']:
            elements.append(element)

        return elements

    def __str__(self):
        return 'Generic Command Object'
