# -*- coding: utf-8 -*-
import typing
from typing import Dict
from typing import List
class COMPOUND(object):
    def __init__(self, name: str, compound_index: int):
        self.__name = name
        self.__id = compound_index     # compound index to match the name
