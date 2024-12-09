#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""


import threading


class FiniteStateMachine(threading.Thread):
    """
    A classical FSM
    """
    def __init__(self):
        super().__init__()
        self.handlers = {}
        self.startState = None
        self.endStates = []
        self._run = True
        self._is_ended = False
        self._doi = None

    def add_state(self, name, handler, end_state=False):
        name = name.upper()
        self.handlers[name] = handler
        if end_state is True:
            self.endStates.append(name)

    def is_ended(self) -> bool:
        return self._is_ended

    def set_start(self, name):
        self.startState = name.upper()

    def quit(self):
        self._run = False

    def set_doi(self, doi):
        self._doi = doi

    def run(self):
        self._analyse(self._doi)

    def _analyse(self, doi):
        try:
            handler = self.handlers[self.startState]
        except:
            raise RuntimeError("must call .set_start() before .run()")
        if not self.endStates:
            raise RuntimeError("at least one state must be an end_state")

        while self._run:
            (newState, doi) = handler(doi)
            if newState.upper() in self.endStates:
            	# call the handler of the end state
                self.handlers[newState.upper()](doi)
                self._is_ended = True
                break
            else:
                handler = self.handlers[newState.upper()]
