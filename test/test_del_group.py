# -*- coding: utf-8 -*-

from random import randrange
import random
import string
import pytest
from model.group import Group

def random_string(prefix, maxlen):
    symbols = f"{string.ascii_letters}{string.digits}" + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
    for i in range(5)
    ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_delete_some_group(app, group):

    if not app.group.count():
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_delete_all_group(app, group):
    if not app.group.count():
        app.group.create(group)
    app.group.delete_all_group()
    assert len(app.group.get_group_list()) == 0

