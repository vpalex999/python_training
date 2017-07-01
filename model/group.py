# -*- coding: utf-8 -*-
import re
from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def id_or_max(self):
        self.name = self.clear(self.name)
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return f"{self.name}:{self.header}:{self.footer}:{self.id}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.name is None or other.name is None or self.name == other.name)

    def clear(self, s):
        if s is not None:
            return re.sub(" ", "", s)