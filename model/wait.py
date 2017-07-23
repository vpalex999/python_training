# -*- coding: utf-8 -*-

import time


class Wait(object):

    @staticmethod
    def condition(condition: bool, timeout=10, pause=1):
        must_end = time.time() + timeout
        while time.time() < must_end:
            if condition(bool):
                return
            time.sleep(pause)
        raise TimeoutError(f'Timeout {timeout} sec expired for condition')


def test_condition():
    check = False
    def check_true(check):
        return check

    if Wait.condition(lambda check_true: check):
        pass