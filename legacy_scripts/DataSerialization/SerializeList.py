__author__ = 'Kaushik LS'
# - - - - - - - - BUILT-IN IMPORTS

# - - - - - - - - RHINO / GRASSHOPPER IMPORTS
import Rhino, System
# - - - - - - - - PACKAGE IMPORTS

# RunScript

if List:
    SerializedList = []
    for c in List:
        SerializedList.append("\"{0}\"".format(c))
    SerializedList = "[" + ','.join(SerializedList) + "]"