# -*- coding: utf-8 -*-

import re

name = "test test "
rr = name.split(" ")
if rr[-1] == "":
    rr[-1:] = []
ss = (" ".join(rr))
pass