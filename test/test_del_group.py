# -*- coding: utf-8 -*-

from random import randrange
import random
from model.group import Group


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)



def test_delete_all_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    app.group.delete_all_group()
    assert len(db.get_group_list()) == 0

