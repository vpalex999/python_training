# -*- coding: utf-8 -*-

from random import randrange
from model.group import Group


def test_delete_some_group(app):

    app.group.open_groups_page()
    if not app.group.count():
        app.group.create(Group(name="Create group"))
        app.group.return_to_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[index:index+1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
