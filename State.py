# -*- coding: utf-8 -*-
from typing import Dict
from Compound import COMPOUND
from Model import MODEL
from Reaction import REACTION

class STATE(object):
    def __init__(self, time: float, biomass: Dict[MODEL, float], mu: Dict[MODEL, float],
                 compounds: Dict[COMPOUND, float]):
        self.__time = time
        self.__compounds = compounds
        self.__biomass = biomass
        self.__mu = mu
        self.__fluxes = Dict[MODEL, Dict[REACTION, float]]
