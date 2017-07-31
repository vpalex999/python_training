# -*- coding: utf-8 -*-

from pytest_bdd import scenario
from .group_step import *


@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass


@scenario('groups.feature', 'Delete a group')
def test_delete_group():
    pass


@scenario('address.feature', 'Add new address')
def test_add_address():
    pass


@scenario('address.feature', 'Delete a address')
def test_delete_address():
    pass


@scenario('address.feature', 'Modify address')
def test_modify_address():
    pass
