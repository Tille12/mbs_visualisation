# -*- coding: utf-8 -*-
from argparse import ArgumentParser

parser = ArgumentParser(usage="Visualisation of cross-feeding networks of microbial communities")

parser.add_argument("-i", "--input", metavar="", nargs='*', help="Supply input path(s) of input file(s).")
parser.add_argument("syntax", nargs="?")

def parse_command_line():
    args = parser.parse_args()
    return args