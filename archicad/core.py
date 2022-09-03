#!/usr/bin/env python27
# -*- coding: utf-8 -*-

__all__ = ['Link', 'Parameter', 'Command', 'CommandResult']

# - - - - - - - - BUILT-IN IMPORTS
import json
import urllib2
import time

# - - - - - - - - LOCAL IMPORTS
from utility import dotNETBase
from members import Element

# - - - - - - - - CLASS LIBRARY

class Link(dotNETBase):

    _PORT = range(19723, 19743)
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
        return '{}:{}'.format(self.host, self.port)
    
    def __init__(self, port=19723):
        self.port = port

    @staticmethod
    def is_valid(port):
        return port in Link._PORT

    def is_alive(self):
        return Command(self).IsAlive()

    def post(self, data):
        connection_object = urllib2.Request(self.address)
        connection_object.add_header('Content-Type', 'application/json')
        
        start_time = time.time()
        response = urllib2.urlopen(connection_object, json.dumps(data).encode('utf8'))
        print('Completed in {:.3f} seconds'.format(time.time() - start_time))
        return CommandResult(response.read())

    def __str__(self):
        return 'TapirLink : {}'.format(self.address)

class CommandResult(dotNETBase):
    
    def __init__(self, response):
        self._data = json.loads(response) #TODO: Check if deepcopy is necessary here
        self.success = self._data.get('succeeded')
        self.result = self._data.get('result', {})
        self.error = self._data.get('error', {})

    def exception(self):
        if self.error is None:
            return ConnectionError('{}:\n{}'.format(self.error['code'], self.error['message']))

    def elements(self):
        return Element.from_command_result(self.result)
    
    def __str__(self):
        return '{} CommandResult'.format('Success' if self.success else 'Failed')

class Parameter(dotNETBase):

    @staticmethod
    def pack(self, parameters):
        if all([isinstance(param, Parameter) for param in parameters]):
            return {'parameter': parameters}
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return '<{} : {}>'.format(self.key, self.value)

class Command(dotNETBase):
    
    @classmethod
    def create(cls, port=19723):
        return cls(Link(port))
    
    def __init__(self, link):
        self.link = link

    def __str__(self):
        return 'Generic Command Object'

    def IsAlive(self):
        cmd = {'command' : 'API.IsAlive'}
        response = self.link.post(cmd)
        return response.success

    def GetAllElements(self):
        cmd = {'command' : 'API.GetAllElements'}
        response = self.link.post(cmd)
        if response.success:
            return response.elements()
        else:
            raise response.exception

    def GetElementsByType(self, elementType):
        
        for item in Element._TYPES:
            if item.lower() == elementType.lower():
                elementType = item
                break
        else:
            raise TypeError("Couldn't find element type: {}".format(elementType))
        
        cmd = { 'command' : 'API.GetElementsByType',
                'parameters' : {'elementType': elementType}
                }
        response = self.link.post(cmd)
        if response.success:
            return response.elements()
        else:
            raise response.exception
        
    def GetProductInfo(self):
        cmd = {'command' : 'API.GetProductInfo'}
        response = self.link.post(cmd)
        if response.success:
            return response.result["version"], response.result["buildNumber"], response.result["languageCode"]
        else:
            raise response.exception
