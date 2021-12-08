#!/usr/bin/env python3
"""
Created on Wed Dec  8 14:28:37 2021

@author: jgh
"""

from string import ascii_lowercase
import random

symbols = list(ascii_lowercase)


class game_states:
    LOSE = 0
    WIN = -1


class CodeMaker:
    def __init__(self, code=None, n_symbols=6, length=4, max_guesses=10):
        self.symbols = symbols[:n_symbols]
        self.length = length
        self.max_guesses = max_guesses
        if code is not None:
            if len(code) != self.length:
                raise ValueError("Code is the wrong length")
            for s in code:
                if s not in self.symbols:
                    raise ValueError("Bad symbol in code")
            self.code = code
        else:
            self.code = random.choices(self.symbols, k=length)
