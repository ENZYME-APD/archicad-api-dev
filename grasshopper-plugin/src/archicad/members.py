#!/usr/bin/env python27
# -*- coding: utf-8 -*-

__all__ = ['Element']

# - - - - - - - - BUILT-IN IMPORTS


# - - - - - - - - LOCAL IMPORTS
from archicad.utility import dotNETBase, RuntimeHelper

# - - - - - - - - CLASS LIBRARY

class Element(dotNETBase):
    
    _TYPES = ['Wall', 'Column', 'Beam', 'Window', 'Door', 'Object', 'Lamp', 'Slab', 'Roof', 'Mesh', 'Zone', 'CurtainWall', 'Shell', 'Skylight', 'Morph', 'Stair', 'Railing', 'Opening']

    ELEMENT_TYPE = RuntimeHelper(_TYPES, 'ElementTypeEnumerator')

    def __init__(self, guid):
        self.guid = guid
    
    def ToDictionary(self):
        return {'elementId' : {'guid' : self.guid} }

    @classmethod
    def FromDictionary(cls, json_data):
        id = json_data.get('elementId', {}).get('guid', '')
        if id: return cls(id)
    
    @classmethod
    def from_command_result(cls, result):
        return [Element.FromDictionary(data) for data in result.get('elements', [])]

    def __str__(self):
        return '<{}:{}>'.format(self.GetType(), self.guid)

class ClassificationSystem(dotNETBase):

    def __init__(self, guid, name, description, source, version, date):
        self.guid = guid
        self.name = name
        self.description = description
        self.source = source
        self.version = version
        self.date = date
    
    @classmethod
    def FromDictionary(cls, json_data):
        json_data = json_data.get('classificationSystemId', {})
        id = json_data.get('guid')
        
        
        
        
        
        return super().FromDictionary(json_data)

    def from_command_result(self, result):
        pass

    def __str__(self):
        return '<{}:{}>'.format(self.GetType(), self.guid)