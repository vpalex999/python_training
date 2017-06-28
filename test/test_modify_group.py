# -*- coding: utf-8 -*-
from random import randrange
import random
import string
import re
import pytest
from model.group import Group


def random_string(prefix, maxlen):
    symbols = f"{string.ascii_letters}{string.digits}{string.punctuation}" + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
        Group(name=name, header=header, footer=footer)
        for name in ["", random_string("name", 10)]
        for header in ["", random_string("header", 20)]
        for footer in ["", random_string("footer", 20)]
    ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_modify_group_name(app, group):
    group.name = clean_other_char(group.name)
    if not app.group.count():
        # app.group.create(Group(name="Test"))
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    # group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    group.name = del_space_for_end_string(group.name)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if not app.group.count():
#         app.group.create(Group(name="Test test "))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="Test test ", header="New header")
#     app.group.modify_group_by_index(group, index)
#     group.id = old_groups[index].id
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == app.group.count()
#     group.name = del_space_for_end_string(group.name)
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def clean_other_char(s):
    return re.sub("[']", "", s)


def del_space_for_end_string(s):
    str = s.split(" ")
    if str[-1] == "":
        str[-1:] = []
    return " ".join(str)
