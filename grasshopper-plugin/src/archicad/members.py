#!/usr/bin/env python27
# -*- coding: utf-8 -*-

__all__ = ['Element', 'ClassificationSystem']

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
    
    @staticmethod
    def from_command_result(result):
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
    
    def ToDictionary(self):
        return {"classificationSystemId" : {"guid" : self.guid},
                "name" : self.name,
                "description" : self.description,
                "version" : self.version,
                "date" : self.date}

    @classmethod
    def FromDictionary(cls, json_data):
        if isinstance(json_data, dict):
            guid = json_data.get('classificationSystemId', {}).get('guid')
            name = json_data.get('name')
            description = json_data.get('description')
            source = json_data.get('source')
            version = json_data.get('version')
            date = json_data.get('date')
            return cls(guid, name, description, source, version, date)
        else:
            raise ValueError('json_data must be a dictionary')

    @staticmethod
    def from_command_result(result):
        return [ClassificationSystem.FromDictionary(data) for data in result.get('classificationSystems', [])]

    def __str__(self):
        return '<{}:{}>'.format(self.GetType(), self.name)
