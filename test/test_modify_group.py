# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_modify_group_name(app):
    if not app.group.count():
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id =  old_groups[index].id
    app.group.modify_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if not app.group.count():
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="New header")
    app.group.modify_group_by_index(group, index)
    group.id = old_groups[index].id
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

