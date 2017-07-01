# -*- coding: utf-8 -*-
from random import randrange
import random
import string
import re
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
def test_modify_group_name(app, group):
    if not app.group.count():
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

