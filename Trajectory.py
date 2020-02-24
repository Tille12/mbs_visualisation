# -*- coding: utf-8 -*-
from typing import Dict
from typing import List
from State import STATE
from Reactor import REACTOR
from TimePars import TIMEPARS
from Compound import COMPOUND
from Model import MODEL

class TRAJECTORY(object):
    def __init__(self, name: str, models: List[MODEL], timestamps: List[float], states: Dict[float, STATE],
                 reactor: REACTOR, time_pars: TIMEPARS, compounds: List[COMPOUND]):
        self.__name = name
        self.__models = models  # name of the model
        self.__states = states  # Dict{timestamp: STATE}
        self.__timestamps = timestamps  # all timestamps in chronological order
        self.__reactor = reactor
        self.__time_pars = time_pars
        self.__compounds = compounds
