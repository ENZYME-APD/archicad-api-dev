#!/usr/bin/env python27
# -*- coding: utf-8 -*-

__all__ = ['Element']

# - - - - - - - - BUILT-IN IMPORTS


# - - - - - - - - LOCAL IMPORTS
from utility import dotNETBase, RuntimeHelper

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
