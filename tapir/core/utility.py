#!/usr/bin/env python27
# -*- coding: utf-8 -*-

__all__ = ['dotNETBase']

# - - - - - - - - CLASS LIBRARY

class dotNETBase(object):

    def __init__(self):
        raise NotImplementedError('Abstract base class cannot be instantiated.')
    
    def __str__(self):
        raise NotImplementedError('Abstract method cannot be called.')
    
    def __repr__(self):
        return self.__str__()
    
    def ToString(self):
        return self.__str__()
    
    def ToJSON(self):
        raise NotImplementedError('Abstract method cannot be called.')

    def FromJSON(self, json_data):
        raise NotImplementedError('Abstract method cannot be called.')

    def GetType(self):
        return self.__class__.__name__
    
    